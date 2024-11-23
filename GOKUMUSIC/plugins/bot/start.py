import time
import random
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.__future__ import VideosSearch

from config import BANNED_USERS, SUPPORT_CHAT, LOGGER_ID
from GOKUMUSIC import app
from GOKUMUSIC.music import _boot_
from GOKUMUSIC.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
    is_on_off,
)
from GOKUMUSIC.utils.decorators.language import LanguageStart
from GOKUMUSIC.utils.formatters import get_readable_time
from GOKUMUSIC.utils.inline import help_pannel, private_panel, start_panel
from Strings import get_string

NEXI_VID = [
    "https://telegra.ph/file/1a3c152717eb9d2e94dc2.mp4",
    "https://graph.org/file/ba7699c28dab379b518ca.mp4",
    "https://graph.org/file/83ebf52e8bbf138620de7.mp4",
    "https://graph.org/file/82fd67aa56eb1b299e08d.mp4",
    "https://graph.org/file/318eac81e3d4667edcb77.mp4",
    "https://graph.org/file/7c1aa59649fbf3ab422da.mp4",
    "https://graph.org/file/2a7f857f31b32766ac6fc.mp4",
]


async def send_start_video(chat_id):
    """Send a random start video."""
    try:
        video_url = random.choice(NEXI_VID)
        sent_video = await app.send_video(chat_id=chat_id, video=video_url, supports_streaming=True)
        return sent_video
    except Exception as e:
        print(f"Error sending video: {e}")
        return None


@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    caption = _["start_2"].format(message.from_user.mention, app.mention)

    # Send the start video first
    video_message = await send_start_video(message.chat.id)

    if video_message:
        await asyncio.sleep(1)  # Wait briefly before sending the next message

    # Send the text and buttons in a separate message
    try:
        await app.send_message(
            chat_id=message.chat.id,
            text=caption,
            reply_markup=InlineKeyboardMarkup(private_panel(_)),
        )
    except Exception as e:
        print(f"Error sending start message: {e}")

    # Log the start event
    if await is_on_off(2):
        await app.send_message(
            chat_id=LOGGER_ID,
            text=f"{message.from_user.mention} started the bot.\n\n"
                 f"<b>User ID:</b> <code>{message.from_user.id}</code>\n"
                 f"<b>Username:</b> @{message.from_user.username}",
        )


@app.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def start_gp(client, message: Message, _):
    out = start_panel(_)
    uptime = int(time.time() - _boot_)
    caption = _["start_1"].format(app.mention, get_readable_time(uptime))

    # Send the start video first
    video_message = await send_start_video(message.chat.id)

    if video_message:
        await asyncio.sleep(1)  # Wait briefly before sending the next message

    # Send the text and buttons in a separate message
    try:
        await app.send_message(
            chat_id=message.chat.id,
            text=caption,
            reply_markup=InlineKeyboardMarkup(out),
        )
    except Exception as e:
        print(f"Error sending start message in group: {e}")

    await add_served_chat(message.chat.id)


@app.on_message(filters.new_chat_members, group=-1)
async def welcome(client, message: Message):
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)

            if await is_banned_user(member.id):
                try:
                    await message.chat.ban_member(member.id)
                except:
                    pass

            if member.id == app.id:
                if message.chat.type != ChatType.SUPERGROUP:
                    await message.reply_text(_["start_4"])
                    return await app.leave_chat(message.chat.id)

                if message.chat.id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_5"].format(
                            app.mention,
                            f"https://t.me/{app.username}?start=sudolist",
                            SUPPORT_CHAT,
                        ),
                        disable_web_page_preview=True,
                    )
                    return await app.leave_chat(message.chat.id)

                out = start_panel(_)

                # Send the start video first
                video_message = await send_start_video(message.chat.id)

                if video_message:
                    await asyncio.sleep(1)  # Wait briefly before sending the next message

                # Send the text and buttons in a separate message
                await app.send_message(
                    chat_id=message.chat.id,
                    text=_["start_3"].format(
                        message.from_user.mention,
                        app.mention,
                        message.chat.title,
                        app.mention,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )

                await add_served_chat(message.chat.id)

        except Exception as ex:
            print(f"Error welcoming new members: {ex}")
