import os
import discord
from dotenv import load_dotenv
import re


load_dotenv()
token = os.getenv("DISCORD_TOKEN")



client = discord.Client()


def count_syllables(message):
    total_count = 0
    syllables = []
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
        syllables.append((word, count))
    print(syllables)
    sections = [ []for i in range(3) ]
    temp = 0
    for i in syllables:
        temp += i[1]
        if temp <= 6:
            sections[0].append(f"{i[0]} ")
        elif temp <= 14:
            sections[1].append(f"{i[0]} ")
        elif temp <= 19:
            sections[2].append(f"{i[0]} ")
    for i in sections:
         print(f"{''.join([b for b in i])}\n")
    return total_count, sections







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

    if 19 >= count_syllables(new_message)[0] >= 14:
        await message.reply(f"""
        {''.join([i for i in count_syllables(new_message)[1]])}\n haiku detected from @{message.author}.\n
        --HaikuBot(Sometimes I make mistakes)
        
        """, mention_author=True)    
    




client.run(token)