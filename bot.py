#!/usr/bin/python3

# Author: Ben Hurricane
# Origin: 14 Feb 22
# bot.py
# This bot responds to the "pin" react with more pin reacts, specifically to
# get around discords pin limits but pinbots hardcoded requirement for 3 pins
# Referenced:
# - https://realpython.com/how-to-make-a-discord-bot-python/
# - discordpy.readthedocs.io/en/latest/api.html#discord.User.mention

import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
import time


print('Loading...')
with open('my_name.txt', 'r') as f:
    me = f.read().strip('\n\r')
    f.close()
    print(me + ' set as Owner')


# Bot Setup
image_types = ["png", "jpeg", "gif", "jpg"]
bot_id = 'Jack#1847'
bot = commands.Bot(command_prefix='!',
                   description='\
This bot was created by Ben Hurricane in 2022 \
to respond to the "pin" react with more pin reacts, \
specifically to get around discords pin limits but \
pinbots hardcoded requirement for 3 pins',
                   help_command=commands.DefaultHelpCommand(
                       no_category='Help Menu:')
                   )
with open('token.txt') as f:
    token = f.readline().strip()  # Read in token from file
load_dotenv()

# Shutdown bot
@bot.command(name='sleep', help='Shutsdown bot')
@commands.has_permissions(administrator=True)
async def close(ctx):
    await bot.close()


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# Ping
@bot.command(name='ping', help="Checks bot is online.")
async def ping(ctx):
    # Attempt to ping user
    msg = ctx.author.mention + ' pong!'
    await ctx.send(msg)
    print(f'{ctx.author} has pinged!')

# Add react
@bot.event
async def on_reaction_add(reaction, user):
    emoji = reaction.emoji
    #if user.bot:
    #    return
    if emoji == "📌":
        time.sleep(5)
        await reaction.message.add_reaction(emoji)
    else:
        return

bot.run(token)  # Launch bot
