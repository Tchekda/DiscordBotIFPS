import os

import discord

if not os.environ['DISCORD_TOKEN']:
    print('No defined Token in environnement : DISCORD_TOKEN')
    exit(0)
TOKEN = os.environ['DISCORD_TOKEN']
client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        print("Received Message from {0.author}".format(message))
        await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    print('Logged in as %s with ID %s' % (client.user.name, client.user.id))


client.run(TOKEN)
