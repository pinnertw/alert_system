import asyncio
import discord
from fastapi import FastAPI
from contextlib import asynccontextmanager
from dc_config import discord_bot, alert_channel, pinner

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

@app.post("/alert/{content}")
async def send_alert(content, channel_id: int=alert_channel, role: int=pinner, person: bool=True):
    content = "\n".join(content.split(","))
    content = f"<@{'' if person else '&'}{role}> {content}"
    channel = await client.fetch_channel(channel_id)
    await channel.send(content=content)
