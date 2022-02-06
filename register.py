from dotenv import load_dotenv
import discord
from discord.ext import commands
import os
from discord.ext.commands import has_permissions



load_dotenv()
token = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="$")


@bot.command()
@has_permissions(administrator=True)
async def register(ctx, arg):
    channel_id = arg
    if ctx.author == ctx.author:
        print(f"{channel_id} registered!")
        with open("/usr/bin/channels.txt", "a") as f:
            with open("/usr/bin/channels.txt", "r") as r:
                if str(channel_id) not in r.readlines():
                    f.write(f"{channel_id}~")
                    await ctx.send(f"you registered {channel_id}")





bot.run(token)
