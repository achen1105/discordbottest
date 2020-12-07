#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 17:36:41 2020

@author: anitachen
"""

import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix=".")
token = os.getenv('DISCORD_BOT_TOKEN')

@client.event
async def on_ready() :
    print("I am online")

@client.event
async def on_message(message):
    # Hello uncle roger
    if message.content.find("hello uncle roger") != -1:
        await message.channel.send(f'Hallo nieces and nephews! :rice:');
    if message.content.find("egg fried rice") != -1:
        await message.channel.send(f'Make sure to use wok for the wok hei :cooking:');

""" 
@client.command(aliases=['addmats', 'add mats'])
async def mats(ctx, *, materials):
    await ctx.send(f'test added {materials}');
    print("added mats");
    
@client.command()
async def materials(ctx, arg1: int, arg2: int):
    #add reaction to message
    await ctx.send(f'added mats {arg1} and {arg2} :heart:');
    print("added mats");
"""

client.run(token)

