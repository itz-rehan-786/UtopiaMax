from pyrogram import Client
import config
from ..logging import LOGGER

assistants = []
assistantids = []

class Userbot(Client):
    def __init__(self):
        self.assistant = Client(
            name="Utopia",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING_SESSION),  # Only using one session string
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info(f"Starting Assistant...")
        
        if config.STRING_SESSION:  # Checking for the single session
            await self.assistant.start()
            
            try:
                await self.assistant.join_chat("Kayto_Official")
                await self.assistant.join_chat("Anime_Chat_Group_Community")
            except Exception as e:
                LOGGER(__name__).error(f"Error joining chat: {e}")
            
            assistants.append(1)  # Only one assistant, so we add it here
            
            try:
                await self.assistant.send_message(config.LOGGER_ID, "Assistant Started")
            except:
                LOGGER(__name__).error(
                    "Assistant has failed to access the log group. Make sure that you have added your assistant to your log group and promoted as admin!"
                )
                exit()
            
            self.assistant.id = self.assistant.me.id
            self.assistant.name = self.assistant.me.mention
            self.assistant.username = self.assistant.me.username
            assistantids.append(self.assistant.id)
            LOGGER(__name__).info(f"Assistant Started as {self.assistant.name}")

    async def stop(self):
        LOGGER(__name__).info(f"Stopping Assistant...")
        try:
            if config.STRING_SESSION:
                await self.assistant.stop()
        except Exception as e:
            LOGGER(__name__).error(f"Error stopping assistant: {e}")
