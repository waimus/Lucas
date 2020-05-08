# LucasTheSadRetard
basic Discord.py bot for fun.

## Prerequisites:
1. Python 3.7 or higher: https://www.python.org/downloads/
2. Git: https://git-scm.com/downloads
3. Discord.py: https://github.com/Rapptz/discord.py
4. Giphy API: https://github.com/Giphy/giphy-python-client

## API Keys
#### Discord API Key: 
Login to Discord and create Discord application/bot in the [Discord Developer Portal](https://discord.com/developers/applications)<br>
Image:
![Imgur](https://i.imgur.com/rP3bY7y.png)

#### Giphy API Key: 
Log in to Giphy Account and create an App in the [Giphy Developer Dashboard](https://developers.giphy.com/dashboard/)<br>
Image:
![Imgur](https://i.imgur.com/LsZoOtF.png)

## Installation:
1. Download and install Python and Git from the link above.
2. Open Git Bash console, or in Windows Explorer right click -> `Git Bash Here`
3. Install Discord.py in Git Bash by typing `py -3 -m pip install -U discord.py`. *More information on how to install it is available on its Github page linked above*.
4. Install Giphy API Python in Git Bash by typing `pip install giphy_client`. *More information on how to install it is available on its Github page linked above*.

## Bot Setup
Now in the `lucas-cleaned.py` file assign your Discord bot token and Giphy API token in the file line 16. A reminder that you have to keep your token secret.
```python
#token
discord_token = 'your-discord-api-token-here'
giphy_token = 'your-giphy-api-token-here'
```

## Running the Bot
A. Double click the `lucas-cleaned.py` file. <br>
B. Open Git Bash console in the folder where `lucas-cleaned.py` file located and run `python lucas-cleaned.py` in the console.
