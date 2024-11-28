# <======================================= IMPORTS ==================================================>
from telegraph import upload_file
from pyrogram import filters
from GOKUMUSIC import app
from pyrogram.types import Message

# <======================================= Helper Function ==========================================>
def upload_to_platform(message: Message, base_url: str):
    reply = message.reply_to_message
    if not reply or not reply.media:
        return message.reply("⚠️ Please reply to a media file (photo/video/document).")
    
    status = message.reply("🔄 Uploading your file...")
    try:
        path = reply.download()
        file_link = upload_file(path)
        for uploaded in file_link:
            url = f"{base_url}{uploaded}"
        status.edit(f"✅ Link generated successfully: `{url}`")
    except Exception as e:
        status.edit(f"❌ Failed to generate link. Error: {e}")

# <======================================= Commands ================================================>
@app.on_message(filters.command(["tele", "telegraph"]))
def upload_to_telegraph(_, message):
    upload_to_platform(message, "https://telegra.ph")

@app.on_message(filters.command(["graph", "grf"]))
def upload_to_graph(_, message):
    upload_to_platform(message, "https://graph.org")
