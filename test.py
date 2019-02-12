import os
import random

from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("?", "!")
TOKEN = os.environ['DISCORD_TOKEN']

client = Bot(command_prefix=BOT_PREFIX)


@client.command(name='8ball')
async def eight_ball():
    responses = ['Yes',
                 'Maybe',
                 'No',
                 'Never',
                 'Forever',
                 'Definitively']
    await client.say(random.choice(responses))

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="communiquer avec EuroFPL"))
    print("Logged in as " + client.user.name)

client.run(TOKEN)
