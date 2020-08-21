# PicSaver by wireless (ROMZiLLA) 
import os, sys, stat
import requests
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix="#")


@bot.event
async def on_ready():
    print ("Ready boi!")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

@bot.command(pass_context = True)
async def ping(ctx):
    await bot.say(":ping_pong: ping!!")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("The username is: {}".format(user.name))
    await bot.say("The users ID is: {}".format(user.id))
    await bot.say("The users status is: {}".format(user.status))
    await bot.say("The user joined at: {}".format(user.joined_at))


@bot.event
async def on_message(message):
    mainCh = bot.get_channel('channel id here')
    if message.channel == mainCh:
        imgURL = message.attachments[0]['url']
        imgNAME = message.attachments[0]['filename']
        if imgURL:
            img_data = requests.get(imgURL).content
            with open(imgNAME, 'wb') as handler:
                handler.write(img_data)
            channel = bot.get_channel('477153925976424449')
            x = open(imgNAME, mode = 'r' + 'b')
            await bot.send_file(channel,x,filename = imgNAME)



bot.run(process.env.BOT_TOKEN)
