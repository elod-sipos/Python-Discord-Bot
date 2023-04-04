from discord.ext import commands
import discord
import time
import random
import requests
import asyncio


BOT_TOKEN = ""
CHANNEL_ID = 

bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all())



# On start
@bot.event
async def on_ready():
    print("hewwo :3")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("new commwands :3")
    while True:
        await reminder()

# Lists all active commands
@bot.command()
async def commands(ctx):
    await ctx.send("``` hello\n add\n seconds\n guess```")

########################## DOES NOT WORK #################################
def random_anime():
    resp = requests.get("https://api.myanimelist.net/v2")
    anime_list = resp.json()["top"]
    anime = random.choice(anime_list)
    return anime

@bot.command()
async def animerec(ctx):
    anime = random_anime()
    anime_url = f"https://myanimelist.net/anime/{anime['mal_id']}"
    await ctx.send(f"okway: {anime['title']} ({anime_url})")
########################## DOES NOT WORK #################################

# Basic hello command
@bot.command()
async def hello(ctx):
    await ctx.send("hewwo :3")

# 5 min reminder #########DOES NOT WORK ###################
async def reminder():
    await asyncio.sleep(600)
    await ctx.send ("Ullmano dessa notter :3")
################### DOES NOT WORK #########################

# Command that allows users to add two numbers
@bot.command()
async def add(ctx, x, y):
    if x == '9' and y == '10':
        await ctx.send(f"{x} + {y} = 21 :3")
    elif not x.isdigit() or not y.isdigit():
        await ctx.send(f"awe u stwoopid? :3")
    else:
        result = int(x) + int(y)
        await ctx.send(f"{x} + {y} = {result} :3")

# Counts in seconds up to ten
@bot.command()
async def seconds(ctx, i: int):
    i = int(i)
    if i <= 10:
        for n in range(1, i+1):
            await ctx.send(f"{n}")
            time.sleep(1)
    else:
        await ctx.send("sowwy i only go to 10 :3")

# Number guessing game
@bot.command()
async def guess(ctx):
    random_number = random.randint(1, 10)
    await ctx.send("Pick a number between 1-10 :3 ")
    guess = None
    while True:
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel and message.content.isdigit()
        guess1 = await bot.wait_for('message', check=check)
        guess = int(guess1.content)
        if guess < random_number:
            await ctx.send("low :3")
        elif guess > random_number:
            await ctx.send("high :3")
        else:
            await ctx.send("nice :3")
            await ctx.send("again???:3 (y/n) ")
            def check2(message):
                return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() in ['y', 'n']
            msg = await bot.wait_for('message', check=check2)
            if msg.content.lower() == "y":
                random_number = random.randint(1, 10)
                await ctx.send("pick again :3 ")
                
            elif msg.content.lower() == "n":
                await ctx.send("okway")
                break
            

bot.run(BOT_TOKEN)
