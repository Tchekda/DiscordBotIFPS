# Bot Discord by Tchekda for "Team MLN208"
Streaming the server chat for flight plans with IFPS format to check them and add a "reaction" if it passes, either the error message will be sent in private message to the sender.
## Builds
 * Master : [![Build Status](https://travis-ci.com/Tchekda/DiscordBotIFPS.svg?branch=master)](https://travis-ci.com/Tchekda/DiscordBotIFPS)
 * Dev : [![Build Status](https://travis-ci.com/Tchekda/DiscordBotIFPS.svg?branch=dev)](https://travis-ci.com/Tchekda/DiscordBotIFPS)
## Getting started
### Prerequisites
 * Python 3.6
 * pip
 * Discord App Secret [Get here](https://discordapp.com/developers/applications/)
### Installing
 * Clone the repository :
```
git clone https://github.com/Tchekda/DiscordBotIFPS.git
``` 
 * Install dependencies
```
pip install -r requirements.txt
```
 * Set the Discord App Secret as **DISCORD_TOKEN** environnement variable
 * Run the bot
```
python bot.py
```
## Running Tests
To run tests, modify the name of your bot in the *test.py* file isthe setUp function at the *name* variable.
```
self.name = "Your bot Name"
``` 
instead of 
```
self.name = "BotIFPS"
```
## Todo
 * Stats per user by correct flight plans
 * Automatic messages when a member stats a flight or open an ATC position
## Authors

* **Tchekda** - [Github](https://github.com/Tchekda) - [Twitter](https://twitter.com/Tchekda) - [Mail](mailto:contact@tchekda.fr)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
