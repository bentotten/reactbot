#!/usr/bin/python3

# Authors: Ben Hurricane, Amber Jennings
# Origin: 14 Feb 2022
# Modified: 22 Sep 2024

# This bot responds to the "pushpin" reaction with more pushpins, specifically to
# get around Discord's pin limits but Pinbot's hardcoded requirement for 3 pins.

# Takes token file as an argument

# References:
# - https://realpython.com/how-to-make-a-discord-bot-python/
# - discordpy.readthedocs.io/en/latest/api.html#discord.User.mention

from discord.ext import commands
import argparse
import discord
import os
import time

# Parse argument as token file
parser = argparse.ArgumentParser()
parser.add_argument("token_file", type=str)
args = parser.parse_args()

with open(args.token_file) as f:
    token = f.readline().strip()

# Bot Setup
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!",
                   intents=intents,
                   description="\
This bot was created by Ben Hurricane in 2022 \
and modified by Amber Jennings in 2024 \
to respond to the \"pushpin\" reaction with more pushpins, \
specifically to get around Discord's pin limits + \
Pinbot's hardcoded requirement for 3 pins",
                   help_command=commands.DefaultHelpCommand(
                       no_category="Help Menu:")
                   )

# Log
@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")

# Shutdown bot (admin)
@bot.command(name="sleep", help="Shuts down bot")
@commands.has_permissions(administrator=True)
async def close(ctx):
    await bot.close()

# Ping (debug)
@bot.command(name="ping", help="Checks bot is online.")
async def ping(ctx):
    msg = ctx.author.mention + " pong!"
    await ctx.send(msg)
    print(f"{ctx.author} has pinged!")

# Duplicate pin reactions (the whole point)
@bot.event
async def on_reaction_add(reaction, user):
    emoji = reaction.emoji
    if emoji == "📌":
        time.sleep(5)
        await reaction.message.add_reaction(emoji)
    else:
        return

bot.run(token)
