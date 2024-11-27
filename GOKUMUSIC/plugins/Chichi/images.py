import logging
import aiohttp
from pyrogram import filters
from pyrogram.types import InputMediaPhoto
from GOKUMUSIC import app

# Set up logging
logging.basicConfig(level=logging.INFO)

BASE_URL = "https://lexica.qewertyy.dev"
SESSION_HEADERS = {"Host": "lexica.qewertyy.dev"}

class ImageSearchClient:
    """Handles API requests to the Lexica image search service."""
    
    def __init__(self):
        self.url = BASE_URL
        self.session = aiohttp.ClientSession()

    async def search_images(self, query):
        """
        Fetch images from the Lexica API for a given query.
        
        Args:
            query (str): The search term provided by the user.
        
        Returns:
            dict: The API response containing image URLs or None if the request fails.
        """
        try:
            async with self.session.get(f"{self.url}/?q={query}", headers=SESSION_HEADERS) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    logging.error(f"Invalid status code {response.status} from API.")
                    return None
        except Exception as e:
            logging.error(f"Error while fetching images: {str(e)}")
            return None

    async def close(self):
        """Closes the aiohttp session."""
        await self.session.close()

async def fetch_and_send_images(message, query):
    """
    Fetch images from the API and send them to the chat.
    
    Args:
        message (pyrogram.types.Message): The Pyrogram message object.
        query (str): The search term provided by the user.
    """
    client = ImageSearchClient()

    # Get images from Lexica API
    images = await client.search_images(query)

    if not images or "images" not in images or not images["images"]:
        await message.reply("No images found for the given query.")
        await client.close()
        return

    # Prepare the media group to send images
    media_group = []
    count = 0
    msg = await message.reply("sᴄʀᴀᴘɪɴɢ ɪᴍᴀɢᴇs ғʀᴏᴍ ʟᴇxɪᴄᴀ...")

    for url in images["images"][:6]:  # Limit to the first 6 images
        media_group.append(InputMediaPhoto(media=url))
        count += 1
        await msg.edit(f"=> ᴏᴡᴏ sᴄʀᴀᴘᴇᴅ ɪᴍᴀɢᴇs {count}")

    # Send the images in a media group
    try:
        await app.send_media_group(
            chat_id=message.chat.id,
            media=media_group,
            reply_to_message_id=message.id
        )
        await msg.delete()  # Delete the "scraping..." message
    except Exception as e:
        await msg.delete()
        logging.error(f"Error sending media group: {str(e)}")
        await message.reply(f"ᴇʀʀᴏʀ: {str(e)}")
    
    await client.close()

@app.on_message(filters.command(["image"], prefixes=["/", "!", "%", ",", ".", "@", "#"]))
async def pinterest(_, message):
    """
    Command handler for the `/image` command.
    Extracts the query from the message and fetches images.
    
    Args:
        message (pyrogram.types.Message): The Pyrogram message object.
    """
    try:
        query = message.text.split(None, 1)[1].strip()  # Extract query after the command
        if not query:
            raise IndexError  # Trigger exception if query is empty
    except IndexError:
        return await message.reply("**ɢɪᴠᴇ ɪᴍᴀɢᴇ ɴᴀᴍᴇ ғᴏʀ sᴇᴀʀᴄʜ 🔍**")

    # Fetch and send images for the given query
    await fetch_and_send_images(message, query)
