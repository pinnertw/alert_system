import asyncio
import discord
from fastapi import FastAPI
from contextlib import asynccontextmanager
from dc_config import discord_bot

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


# where the magic happens
# register an asyncio.create_task(client.start()) on app's startup event
#                                        ^ note not client.run()
@asynccontextmanager
async def lifespan(app: FastAPI):
  asyncio.create_task(client.start(discord_bot))
  yield
  print("help")

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def read_root():
  return {"Hello": str(client.user)}
