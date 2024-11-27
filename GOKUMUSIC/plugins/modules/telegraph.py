from telegraph import upload_file
from pyrogram import filters
from GOKUMUSIC import app
from pyrogram.types import InputMediaPhoto


# /tgm command for uploading to Telegraph
@app.on_message(filters.command(["tgm", "telegraph", "link"]))
async def ul(_, message):
    reply = message.reply_to_message
    if reply and reply.media:
        i = await message.reply("𝐌𝙰𝙺𝙴 𝐀 𝐋𝙸𝙽𝙺...")
        path = await reply.download()
        
        try:
            fk = upload_file(path)  # Upload the file to Telegraph
            if isinstance(fk, dict) and 'url' in fk:
                url = "https://telegra.ph" + fk['url']  # Extract the URL from the response
                await i.edit(f'Yᴏᴜʀ ʟɪɴᴋ sᴜᴄᴄᴇssғᴜʟ Gᴇɴ {url}')
            else:
                await i.edit("Error generating link. Please try again.")
        except Exception as e:
            await i.edit(f"Error occurred: {str(e)}")
        finally:
            os.remove(path)  # Clean up the downloaded file


# /graph command for uploading to Graph.org
@app.on_message(filters.command(["graph", "grf"]))
async def ul(_, message):
    reply = message.reply_to_message
    if reply and reply.media:
        i = await message.reply("𝐌𝙰𝙺𝙴 𝐀 𝐋𝙸𝙽𝙺...")
        path = await reply.download()
        
        try:
            fk = upload_file(path)  # Upload the file to Graph.org
            if isinstance(fk, dict) and 'url' in fk:
                url = "https://graph.org" + fk['url']  # Extract the URL from the response
                await i.edit(f'Yᴏᴜʀ ʟɪɴᴋ sᴜᴄᴄᴇssғᴜʟ Gᴇɴ {url}')
            else:
                await i.edit("Error generating link. Please try again.")
        except Exception as e:
            await i.edit(f"Error occurred: {str(e)}")
        finally:
            os.remove(path)  # Clean up the downloaded file
