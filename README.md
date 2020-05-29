# LucasTheSadRetard
Basic Discord.py bot for fun. I wrote this script for a bot I named "Lucas the Sad Retard". Responses to a word in a sentence, commands, and GIF search commmand powered by Giphy. But this is a one-file-mess. 

Created using Discord.py by Rapptz, Python 3, and Giphy Python API. This bot script can be used to your own Discord bot by just using your bot API token, and the bot is not necessarily named "Lucas the Sad Retard".

With the stuff that are already written in the code, you can expand it by following how things were written or by however you like. And when all the stuff that are required for this bot to be able to run installed, you can also create more Discord.py bot by yourself from scratch.

## Prerequisites:
1. Python 3.5 or higher: https://www.python.org/downloads/
2. Git: https://git-scm.com/downloads
3. Discord.py: https://github.com/Rapptz/discord.py
4. Giphy API: https://github.com/Giphy/giphy-python-client
5. python-dotenv: https://pypi.org/project/python-dotenv/
6. Discord and Giphy account.

## Installation:
This would use the PIP command to install some of the API. Make sure you have PIP. When Python is intalled you may want to try to use command `python -m pip install --upgrade pip` or search a hint over the internet on how to install PIP.

1. Download and install Python and Git from the link above.
2. Open Git Bash console, or in Windows Explorer right click -> `Git Bash Here`
3. Install Discord.py in Git Bash by running the command: `python3 -m pip install -U discord.py`. 
>*More information on how to install Discord.py is available on its Github page:*. <br>
https://github.com/Rapptz/discord.py/blob/master/README.rst
4. Install Giphy API Python in Git Bash by running the command: `python3 -m pip install -U giphy_client`. 
>*More information on how to install Giphy API Python is available on its Github page*. <br>
https://github.com/Giphy/giphy-python-client/blob/master/README.md
5. Install python-dotenv in Git Bash by running the command: `python3 -m pip install -U python-dotenv`. 
>*More information about python-dotenv is available on its site*. <br>
https://pypi.org/project/python-dotenv/

## API Token
These tokens connect your bot to the Discord and Giphy service. The bot wouldn't be able to be online if you do not have token.

#### Discord API Token: 
Login to Discord and create Discord application/bot in the [Discord Developer Portal](https://discord.com/developers/applications)<br>
> *More detailed information on how to setup and invite a Discord bot can be found here:*  <br>
https://discordpy.readthedocs.io/en/latest/discord.html <br>

Then in this menu you can see your API token, a reminder that you have to keep your token secret.
<img src="https://i.imgur.com/WWS806e.png" width="768" align="center">

#### Giphy API Token: 
Log in to Giphy Account and create an App in the [Giphy Developer Dashboard](https://developers.giphy.com/dashboard/)<br>
Then in this menu you can see your API token, a reminder that you have to keep your token secret.
<img src="https://i.imgur.com/LsZoOtF.png" width="768" align="center">

## Bot Setup

#### Creating a Discord Bot
If you haven't created a bot in the [Discord Developer Portal](https://discord.com/developers/applications) use the following link to read how to setup and invite your Discord bot to your server: <br>
> https://discordpy.readthedocs.io/en/latest/discord.html <br>

Feel free to name your bot whatever you like.

#### Token Setup
See [API Token](#api-token) to read how to get your Discord and Giphy API token. <br>
Now in the `.env` file assign your Discord bot token and Giphy API token in the file line 4. 
```python
# .env
#enter your secrets and token here, and load them to your scripts

DISCORD_TOKEN='input-your-token-here'
GIPHY_TOKEN='input-your-token-here'
```
A reminder that you have to keep your token secret.

## Running the Bot
You can run the bot in some ways:<br>
A. Double click the `lucas-cleaned.py` file. <br>
B. Open Git Bash console in the folder where `lucas-cleaned.py` file located and run `python lucas-cleaned.py` in the console.
<br>

You have to keep it running in order the bot to be online in Discord. To do that, you can use some Platform as a Service provider to host your bot. [glitch.com](https://glitch.com/) is one easy service to host your bot.
