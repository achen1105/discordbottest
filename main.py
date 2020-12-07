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

