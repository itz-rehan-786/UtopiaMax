import time
import requests
from pyrogram import filters
from pyrogram.enums import ChatAction, ParseMode
from GOKUMUSIC import app

@app.on_message(filters.command(["chatgpt", "ai", "ask", "gpt", "solve"], prefixes=["+", ".", "/", "-", "", "$", "#", "&"]))
async def chat_gpt(bot, message):
    """Fetch a response from ChatGPT-like API and reply to the user."""
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)

        # Check if the command has a query
        if len(message.command) < 2:
            return await message.reply_text(
                "Please provide a question.\n\nExample:\n`/chatgpt Where is Hastinapur?`",
                parse_mode=ParseMode.MARKDOWN
            )

        # Extract the query
        query = message.text.split(' ', 1)[1]

        # Call the API
        api_url = f"https://chatgpt.apinepdev.workers.dev/?question={query}"
        response = requests.get(api_url, timeout=10)

        # Check for a successful HTTP response
        if response.status_code != 200:
            return await message.reply_text(
                f"Error: Unable to fetch a response. API returned status code {response.status_code}."
            )

        # Parse the JSON response
        data = response.json()
        answer = data.get("answer")

        if not answer:
            return await message.reply_text(
                "The API did not return an answer. Please try again later."
            )

        # Measure the response time
        end_time = time.time()
        response_time = round((end_time - start_time) * 1000, 2)

        # Reply with the answer
        await message.reply_text(
            f"**Question:** `{query}`\n\n**Answer:** {answer}\n\nResponse time: `{response_time} ms`\n\nAnswered by: [@{BOT_USERNAME}](https://t.me/{BOT_USERNAME})",
            parse_mode=ParseMode.MARKDOWN
        )

    except requests.exceptions.Timeout:
        await message.reply_text("Error: The request timed out. Please try again later.")
    except requests.exceptions.RequestException as e:
        await message.reply_text(f"Error: An error occurred while making the request.\n\nDetails: {e}")
    except Exception as e:
        await message.reply_text(f"Unexpected Error: {e}")
