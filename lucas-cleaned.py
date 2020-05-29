#bot.py
#basic discord.py
import sys
import asyncio
import random
import urllib.request
import json
import discord
from discord.ext import commands
from random import choice

#giphy
import giphy_client
from giphy_client.rest import ApiException
from pprint import pprint


#token
discord_token = 'your-discord-api-token-here'
giphy_token = 'your-giphy-api-token-here'

game = discord.Game("with a paranoid mind")
gifrating = 'g'

#discord bot definition
client = discord.Client()
bot = commands.Bot(command_prefix='!')

# Create an instance of the Giphy API class
api_instance = giphy_client.DefaultApi()

#giphy functions
def search_gifs(query):
    global gifrating

    try:
        return api_instance.gifs_search_get(giphy_token, query, limit=5, rating = gifrating)
        pprint(api_response)

    except ApiException as e:
        return "Exception when calling DefaultApi->gifs_search_get: %s\n" % e


def gif_response(keyword):
    gifs = search_gifs(keyword)
    lst = list(gifs.data)
    gif = random.choices(lst)

    #return gif[0].url
    return gif[0].images.downsized.url
    #return gif[0].images.original_still.url

def contains_word(s, w):
    return f' {w} ' in f' {s} '

#discord functions
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))    
    await client.change_presence(status=discord.Status.idle, activity=game)
    
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    message.content = message.content.lower()

    if message.content.startswith('!greet'):
        await message.channel.send('Hello, {}!'.format(message.author.mention))
        
    if message.content.startswith ('hi lucas') or message.content.startswith('hello lucas'):
        await message.channel.send('Hi {}'.format(message.author.mention))
        
    if 'how do you turn this on' in message.content:
        embed = discord.Embed(title="vroomm", description=">how do you turn this on", color=0x00ff00)
        embed.set_image(url="https://cdn.discordapp.com/attachments/684039836503506944/690166049617870848/images6.jpg")
        
        await message.channel.send(embed=embed)
        
    if 'say the f word' in message.content or 'bully aku waktu smp' in message.content or 'rizky' in message.content or 'rizki' in message.content or 'riski' in message.content or 'risky' in message.content or 'rezki' in message.content or 'reski' in message.content or 'resky' in message.content or 'rezky' in message.content or 'reznov' in message.content or 'ruski' in message.content or 'russian' in message.content:
        print ('someone got bullied and he blamed rizki')
        await message.channel.send('╭∩╮（￣へ￣）╭∩╮ FUCEK ╭∩╮（￣へ￣）╭∩╮')
        
    if contains_word(message.content, 'nice') or contains_word(message.content, '69'):
        print('someone said nice in the middle of a sentence')
        await message.channel.send('Nice')
        
    if contains_word(message.content, '420'):
        await message.channel.send('Blaze it!')
        
        
    if 'ngakak' in message.content or 'wk' in message.content or 'kw' in message.content:
        await message.channel.send('AHAHHAHAHAHAHAHHAHAHAHAHAHAHAHAH LMAO')
        
    if contains_word(message.content, 'asw') or contains_word(message.content, 'asu') or contains_word(message.content, 'aso'):
        await message.channel.send('artinya ANJING')
        
    if contains_word(message.content, 'ok') or 'okey' in message.content or 'oke' in message.content or 'okay' in message.content:
        await message.channel.send('sip')
        
    if 'sip' in message.content:
        await message.channel.send('Ok')
        
    if 'anjay' in message.content:
        await message.channel.send ('mabar')
        
    if 'mabar' in message.content:
        await message.channel.send('Anjay mabar')
        
    if 'euy' in message.content:
        await message.channel.send('e u y   m o m e n t')
        
    if 'bruh' in message.content:
        await message.channel.send ('b r u h   m o m e n t')
        
    if 'anjing' in message.content:
        await message.channel.send ('Lu juga ANJING')
        
    if 'fri' in message.content:
        await message.channel.send ('All hail lord FRI')
        
    if 'unexpect' in message.content or 'expecting that' in message.content:
        await message.channel.send ('Nobody expects the SPANISH INQUISITION')
        
    if contains_word(message.content, 'uwu'):
        await message.channel.send('wibu lu')
        
    if contains_word(message.content, 'wibu'):
        await message.channel.send('bau bawang')
        
    if 'lol' in message.content:
        await message.channel.send('What the lol did you just loling say about me, you little lol? I’ll have you lol that I graduated top of my lol class in the Navy LOLs, and I’ve been involved in numerous secret raids on Al-Lolita, and I have over 300 confirmed lols. I am trained in lol warfare and I’m the top loller in the entire US armed lollers...If only you could have known what unloly retribution your little “loller” comment was about to bring down upon you, maybe you would have lolled your fucking tongue. But you couldn’t, you didn’t, and now you are paying the price, you goddamn lol. I will lol fury all over you and you will lol in it. You’re loling dead, lol.')
      
    
@bot.command()
async def introduce(ctx):
    """Introducing this bot."""
    await ctx.send('Hi! I am Lucas from Kampus Biru. I am also slightly retarded. Just like my creator :)')
        
@bot.command()
async def repeat(ctx, times : int, content: str):
    """Repeats a message multiple times."""            
    if times < 70:
        #repeats
        for i in range(times):
            await ctx.send(content)
    elif times > 69:
        #notices
        await ctx.send('repeatnya ga bisa lebih dari 69 anjir gila anjir gua cape anjir')
        
@bot.command()
async def addnum(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)
    
@bot.command()
async def merge(ctx, word1, word2):
    """Merges two words."""
    await ctx.send(word1 + word2)
    
@bot.command()
async def ping(ctx):
    """Pings the bot."""
    await ctx.send('pong')
    
@bot.command(pass_context=True)
async def say(ctx, *args):
    """Tell the bot to say something"""
    msg = " ".join(args[:])
    await ctx.message.delete()
    await ctx.send(msg) 
       
@bot.command(pass_context=True)
async def sendfile(ctx, *filepath):
    """send file"""
    targetpath = " ".join(filepath[:])
    pprint('sending {}'.format(targetpath))
    await ctx.send(file=discord.File(targetpath))
        
@bot.command()
async def testembed(ctx):
    """This is a fucking test command."""
    # file = discord.File("https://i.imgur.com/2WmBJjp.png", filename="...")
    # await ctx.send("content", file=file)
    
    roll = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    
    embed = discord.Embed(title="Title", description="Desc", color=0x00ff00)
    embed.add_field(name="Something if you curious like a catt", value="[You are a cat]({})".format(roll), inline=False)
    embed.add_field(name="Field2", value="hi2", inline=False)
    embed.set_image(url="https://i.imgur.com/cgFz5NX.gif")
    
    await ctx.send(embed=embed)
    
@bot.command(pass_context = True)
async def cat(ctx, *args):
    """get a random cat pic from the internet"""
    url = "https://cataas.com/cat"

    if (len(args) > 0):
        url = url + "/" + args[0]

    embed = discord.Embed(color=0x00ff00)
    embed.set_image(url=url)

    await ctx.send(embed=embed)
    
@bot.command()
async def xkcd(ctx, arg):
    """Get an xkcd comic from entered number or random"""
    url = "https://xkcd.com/"
    
    if arg == "random":
        num = random.randint(1, 2313)
        url = url + str(num)
    else:
        url = url + arg 
        
    info = url + "/info.0.json"
    
    try:
        with urllib.request.urlopen(info) as xkcdjson:
            xkcddata = json.loads(xkcdjson.read())
    
            embed = discord.Embed(title="{}".format(xkcddata["safe_title"]), description="[{0}]({1})".format(xkcddata["alt"], url), color=0x00ff00)
            embed.set_image(url=xkcddata["img"])
    
            await ctx.send(embed=embed)
    except:
        await ctx.send("cannot retrieve data from " + url)
    finally:
        pprint(ctx.message.author.name + "=> xkcd: " + url)
        pprint("image: " + xkcddata["img"])
        
@bot.command()
async def gif(ctx, *keywords):
    """Send gif as embed from Giphy."""
    searchkey = " ".join(keywords[:])
    searchkey.lower()
    gifurl = gif_response(searchkey)
    
    embed = discord.Embed(title=">{}".format(searchkey.replace('_', ' ')), description="[Source to the giphy site]({})".format(gifurl), color=0x00ff00)
    embed.set_image(url=gifurl)
    
    await ctx.send(embed=embed)
    
@bot.command()
async def currentgifrating(ctx):
    """Shows current gif rating set."""
    global gifrating
    await ctx.send(gifrating)    
    
@bot.command()
async def setgifrating(ctx, inputrating: str):
    """Set a gif rating. Ratings: y, g, pg, pg-13, and r."""
    global gifrating
    inputrating.lower()
    gifrating = inputrating
    await ctx.send('Rating has been set to {}'.format(gifrating))
    
@bot.command()
async def mocktext(ctx, *texts):
    """Converts input into a mocking sentence"""
    sentence = " ".join(texts[:])
    sentence.lower()
    msg = "".join(choice((str.upper, str.lower))(c) for c in sentence)
    
    await ctx.send(msg)
    
@bot.command()
async def iii(ctx, *texts):
    """Cinvirt i nirmil sintincis ti simthing liki this"""
    word = " ".join(texts[:])
    #word.lower()
    
    vowels = ('a', 'e', 'o', 'u')
    bigvowels = ('A', 'E','O', 'U')
    for c in word:
        if c in vowels:
            word = word.replace(c,"i")
        if c in bigvowels:
            word = word.replace(c,"I")
        
    msg = word
    
    await ctx.send(msg)
    
@bot.command()
async def micktixt(ctx, *texts):
    """CInVirT i nIRMIL siNtInCIS TI SImtHiNg Liki THiS"""
    word = " ".join(texts[:])
    word.lower()
    
    vowels = ('a', 'e', 'o', 'u')
    for c in word:
        if c in vowels:
            word = word.replace(c,"i")
        if c in bigvowels:
            word = word.replace(c,"I")
    
    sentence = word
    
    sentence.lower()
    msg = "".join(choice((str.upper, str.lower))(c) for c in sentence)
    
    await ctx.send(msg)
    

loop = asyncio.get_event_loop()
loop.create_task(client.start(discord_token))
loop.create_task(bot.start(discord_token))

try:
    loop.run_forever()
finally:
    loop.stop()
