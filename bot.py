import os
import re

import discord
import requests

from aiohttp.connector import ProxyConnector, BaseConnector
from bs4 import BeautifulSoup


def run():
    if not os.environ['DISCORD_TOKEN']:
        print('No defined Token in environnement : DISCORD_TOKEN')
        exit(0)
    if 'PROD' in os.environ:
        connector = ProxyConnector(proxy="http://proxy.server:3128")
    else:
        connector = None
    TOKEN = os.environ['DISCORD_TOKEN']
    client = discord.Client(connector=connector)

    @client.event
    async def on_message(message):
        # we do not want the bot to reply to itself
        if message.author == client.user:
            return

        regex = re.compile(r'\(FPL-(.|\s)*\)')
        search = regex.search(message.content)
        if search:
            print("Received Message from {0.author} with FPL : ".format(message), search[0])
            validate = validate_fpl(search[0])
            if validate is True:
                await client.add_reaction(message, '✅')
            else:
                await client.add_reaction(message, '❎')
                await client.send_message(message.author,
                                          "Le plan de vol que vous venez d'envoyer dans le channel %s"
                                          " est incorrect : %s" % (message.channel.mention, validate))
        else:
            # print("Didn't parse the message....")
            pass

    @client.event
    async def on_ready():
        print('Logged in as %s with ID %s' % (client.user.name, client.user.id))
        await client.change_presence(game=discord.Game(name='Vérifier vos plans de vols'))

    def validate_fpl(text):
        req = requests.post("http://validation.eurofpl.eu/", data={'freeEntry': text})
        data = BeautifulSoup(req.text, features="html.parser")
        for span in data.find_all('span', 'ifpuv_result'):
            if span.get_text() == 'NO ERRORS':
                print('Success : No Errors')
                return True
            else:
                print("Error : ", span.get_text())
                return span.get_text()

    client.run(TOKEN)


if '__main__' == __name__:
    run()
