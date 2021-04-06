# bot.py
import os

from pprint import pprint
from character import make_character
import discord
from dotenv import load_dotenv

resp = """
{}
Name: {}

{}
{}
{}
"""

if __name__ == "__main__":
    load_dotenv()
    TOKEN = os.getenv("DISCORD_TOKEN")
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f"{client.user} has connected to Discord!")

    @client.event
    async def on_message(message):
        if " ".join(message.content.split()[1:]).lower() == "make character":
            name, image, traits = make_character()
            response = resp.format(image, name, traits[0], traits[1], traits[2])
            await message.channel.send(response)

    client.run(TOKEN)
