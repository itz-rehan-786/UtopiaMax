import imghdr
import os
from asyncio import gather
from traceback import format_exc

from pyrogram import filters
from pyrogram.errors import (
    PeerIdInvalid,
    ShortnameOccupyFailed,
    StickerEmojiInvalid,
    StickerPngDimensions,
    StickerPngNopng,
    UserIsBlocked,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from GOKUMUSIC import app
from config import BOT_USERNAME
from GOKUMUSIC.utils.errors import capture_err

from GOKUMUSIC.utils.files import (
    get_document_from_file_id,
    resize_file_to_sticker_size,
    upload_document,
)

from GOKUMUSIC.utils.stickerset import (
    add_sticker_to_set,
    create_sticker,
    create_sticker_set,
    get_sticker_set_by_name,
)

# Constants
MAX_STICKERS = 120  # Maximum stickers per pack
SUPPORTED_TYPES = ["jpeg", "png", "webp"]  # Supported sticker formats


@app.on_message(filters.command("get_sticker"))
@capture_err
async def sticker_image(_, message: Message):
    """Reply to a sticker to send it back as both photo and document."""
    r = message.reply_to_message
    if not r or not r.sticker:
        return await message.reply("Reply to a sticker.")

    m = await message.reply("Sending...")
    file_path = await r.download(f"{r.sticker.file_unique_id}.png")

    try:
        await gather(
            message.reply_photo(file_path),
            message.reply_document(file_path),
        )
    finally:
        await m.delete()
        if os.path.isfile(file_path):
            os.remove(file_path)


@app.on_message(filters.command("kang"))
@capture_err
async def kang(client, message: Message):
    """Kang a sticker and create a sticker pack."""
    if not message.reply_to_message:
        return await message.reply_text("Reply to a sticker/image to kang it.")
    if not message.from_user:
        return await message.reply_text("You are anon admin, kang stickers in my PM.")

    msg = await message.reply_text("Kanging Sticker...")
    sticker_emoji = "🤔"
    args = message.text.split()
    
    # Determine sticker emoji
    if len(args) > 1:
        sticker_emoji = args[1]
    elif message.reply_to_message.sticker and message.reply_to_message.sticker.emoji:
        sticker_emoji = message.reply_to_message.sticker.emoji

    # Handle sticker/image kanging
    try:
        doc = message.reply_to_message.photo or message.reply_to_message.document

        if message.reply_to_message.sticker:
            sticker = await create_sticker(
                await get_document_from_file_id(message.reply_to_message.sticker.file_id),
                sticker_emoji,
            )
        elif doc:
            if doc.file_size > 10_000_000:  # Max file size of 10MB
                return await msg.edit("File size too large.")

            temp_file_path = await app.download_media(doc)
            image_type = imghdr.what(temp_file_path)
            
            if image_type not in SUPPORTED_TYPES:
                return await msg.edit(f"Format not supported! ({image_type})")

            try:
                temp_file_path = await resize_file_to_sticker_size(temp_file_path)
                sticker = await create_sticker(
                    await upload_document(client, temp_file_path, message.chat.id),
                    sticker_emoji,
                )
            finally:
                if os.path.isfile(temp_file_path):
                    os.remove(temp_file_path)
        else:
            return await msg.edit("Nope, can't kang that.")

        # Create or get sticker pack
        packnum = 0
        limit = 0
        packname = f"f{message.from_user.id}_by_{BOT_USERNAME}"

        while limit < 50:
            stickerset = await get_sticker_set_by_name(client, packname)

            if not stickerset:
                # Create a new sticker set if one does not exist
                stickerset = await create_sticker_set(
                    client,
                    message.from_user.id,
                    f"{message.from_user.first_name[:32]}'s kang pack",
                    packname,
                    [sticker],
                )
            elif stickerset.set.count >= MAX_STICKERS:
                # If the pack is full, create a new pack
                packnum += 1
                packname = f"f{packnum}_{message.from_user.id}_by_{BOT_USERNAME}"
                limit += 1
                continue
            else:
                await add_sticker_to_set(client, stickerset, sticker)
            break

        await msg.edit(
            f"Sticker Kanged To [Pack](t.me/addstickers/{packname})\nEmoji: {sticker_emoji}"
        )
    except (PeerIdInvalid, UserIsBlocked):
        keyboard = InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="Start", url=f"t.me/{BOT_USERNAME}")]]
        )
        await msg.edit(
            "You Need To Start A Private Chat With Me.",
            reply_markup=keyboard,
        )
    except StickerPngNopng:
        await message.reply_text("The provided image is not a valid PNG.")
    except StickerPngDimensions:
        await message.reply_text("The sticker PNG dimensions are invalid.")
    except StickerEmojiInvalid:
        await message.reply_text("[ERROR]: INVALID_EMOJI_IN_ARGUMENT")
    except ShortnameOccupyFailed:
        await message.reply_text("Change your name or username.")
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")
        print(format_exc())
