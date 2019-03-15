import os
import unittest
import datetime
import discord

import bot


class BotTest(unittest.TestCase):

    def setUp(self):
        self.name = "BotIFPS"

    def test_environ(self):
        self.assertIn('DISCORD_TOKEN', os.environ)

    def test_login(self):
        client = discord.Client()

        @client.event
        async def on_ready():
            await client.close()
            self.assertEqual(client.user.name, self.name)

        client.run(os.environ['DISCORD_TOKEN'])

    def test_validator(self):
        today = datetime.datetime.now()
        date = today.strftime("%y%m%d")
        good_fpl = "(FPL-AFR17DT-IS\
            -A321/M-SDE3FGHIRWY/LB1\
            -LFMH2000\
            -N0374F180 BELEP4 BELEP A3 MOU MOU8W\
            -LFPO0032 EBBR\
            -PBN/A1B1C1D1O1S1 DOF/%s REG/N321SB EET/LFFF0012 OPR/AFR PER/C\
             RMK/TCAS)" % date
        wrong_fpl = "(FPL-AFR17DT-IS\
            -A321/M-SDE3FGHIRWY/LB1\
            -LFMH2000\
            -N0374F180 BELEP4 BELEP A3 MOU MOU8W\
            -LFPO0032 EBBR\
            -PBN/A1B1C1D1O1S1 DOF/021117 REG/N321SB EET/LFFF0012 OPR/AFR PER/C\
             RMK/TCAS)"
        self.assertTrue(bot.validate_fpl(good_fpl))
        self.assertNotEqual(bot.validate_fpl(wrong_fpl), True)


if '__main__' == __name__:
    unittest.main()
