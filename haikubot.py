from dis import dis
import os
import discord
from dotenv import load_dotenv
import re


load_dotenv()
token = os.getenv("DISCORD_TOKEN")



client = discord.Client()


def count_syllables(message):
    total_count = 0
    for word in message.split():
        word = word.lower()
        count = 0
        vowels = "aeiouy"
        if word[0] in vowels:
            count += 1
        for index in range(1, len(word)):
            if word[index] in vowels and word[index - 1] not in vowels:
                count += 1
        if word.endswith("e"):
            count -= 1
        if count == 0:
            count += 1
        total_count += count
    return total_count







@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    
    print(
        f'{client.user} is connected to the following server:\n'
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    new_message = re.sub(r"[^a-zA-Z0-9 ]", "", message.content)

    if 19 >= count_syllables(new_message) >= 14:
        await message.reply(f"""
        {message.content}\n haiku detected from @{message.author}.\n
        --HaikuBot(Sometimes I make mistakes)
        
        """, mention_author=True)    
    




client.run(token)