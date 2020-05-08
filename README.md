# LucasTheSadRetard
Basic Discord.py bot for fun. Responses to a word in a sentence, commands, and GIF search commmand. But this is a one-file-mess. Created using Discord.py by Rapptz, Python 3, and Giphy Python API.

## Prerequisites:
1. Python 3.5 or higher: https://www.python.org/downloads/
2. Git: https://git-scm.com/downloads
3. Discord.py: https://github.com/Rapptz/discord.py
4. Giphy API: https://github.com/Giphy/giphy-python-client

## Installation:
1. Download and install Python and Git from the link above.
2. Open Git Bash console, or in Windows Explorer right click -> `Git Bash Here`
3. Install Discord.py in Git Bash by running the command: `py -3 -m pip install -U discord.py`. 
>*More information on how to install Discord.py is available on its Github page:*. <br>
https://github.com/Rapptz/discord.py/blob/master/README.rst
4. Install Giphy API Python in Git Bash by running the command: `pip install giphy_client`. 
>*More information on how to install Giphy API Python is available on its Github page*. <br>
https://github.com/Giphy/giphy-python-client/blob/master/README.md

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

#### Token Setup
Now in the `lucas-cleaned.py` file assign your Discord bot token and Giphy API token in the file line 16. A reminder that you have to keep your token secret.
```python
#token
discord_token = 'your-discord-api-token-here'
giphy_token = 'your-giphy-api-token-here'
```

## Running the Bot
You can run the bot in some ways:<br>
A. Double click the `lucas-cleaned.py` file. <br>
B. Open Git Bash console in the folder where `lucas-cleaned.py` file located and run `python lucas-cleaned.py` in the console.
<br>

You have to keep it running in order the bot to be online in Discord. I think you can host it in a hosting service so it can run forever without having it running in your computer. But I personally have never host bot in a hosting service ever so I don't know how to do it.
