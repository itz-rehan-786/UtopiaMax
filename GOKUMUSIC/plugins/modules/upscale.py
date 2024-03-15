import base64
import httpx
import os
import requests 
from pyrogram import filters
from config import BOT_USERNAME
from GOKUMUSIC import app
from pyrogram import filters
import pyrogram
from uuid import uuid4
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup

import cv2
import numpy as np

@app.on_message(filters.reply & filters.command("upscale"))
async def upscale_image(app, message):
    try:
        if not message.reply_to_message or not message.reply_to_message.photo:
            await message.reply_text("**Please reply to an image to upscale it.**")
            return

        image = message.reply_to_message.photo.file_id
        file_path = await app.download_media(image)

        # Read the image
        img = cv2.imread(file_path)

        # Upscale the image
        upscaled_img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

        # Apply sharpening filter
        kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        sharpened_img = cv2.filter2D(upscaled_img, -1, kernel)

        # Save the sharpened image
        sharpened_file_path = "sharpened.png"
        cv2.imwrite(sharpened_file_path, sharpened_img)

        # Send the sharpened image
        await app.send_photo(
            message.chat.id,
            photo=sharpened_file_path,
            caption="**Here is the upscaled and sharpened image!**",
        )

        # Clean up files
        os.remove(file_path)
        os.remove(sharpened_file_path)

    except Exception as e:
        print(f"Failed to upscale and sharpen the image: {e}")
        await message.reply_text("**Failed to upscale and sharpen the image. Please try again later.**")



@app.on_message(filters.command("smooth"))
async def smooth_image(app, message):
    try:
        # Check if the replied message is an image
        if not message.reply_to_message or not message.reply_to_message.photo:
            await message.reply_text("Please reply to an image to smooth it.")
            return

        # Download the image
        image = await app.download_media(message.reply_to_message.photo.file_id)

        # Read the image
        img = cv2.imread(image)

        # Apply Gaussian blur for smoothing
        smoothed_img = cv2.GaussianBlur(img, (15, 15), 0)

        # Save the smoothed image
        smoothed_file_path = "smoothed_image.png"
        cv2.imwrite(smoothed_file_path, smoothed_img)

        # Send the smoothed image
        await app.send_photo(
            chat_id=message.chat.id,
            photo=smoothed_file_path,
            caption="Here is the smoothed image!",
        )

        # Clean up files
        os.remove(image)
        os.remove(smoothed_file_path)

    except Exception as e:
        print(f"Failed to smooth the image: {e}")
        await message.reply_text("Failed to smooth the image. Please try again later.")

