from dotenv import load_dotenv
import discord
from discord.ext import commands
import os

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="$")


@bot.command()

async def register(ctx, arg):
    channel_id = arg
    await ctx.send(f"you registered {channel_id}")
    print(f"{channel_id} registered!")
    os.system(f"""cd && echo -n "{str(channel_id)} " >> /haikubot/.env""")
 
bot.run(token)