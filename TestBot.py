# client id : 590936733785522205
# client secret : iXr8dowBXR2w_76XaBMGbnbGwg8Axb5H
# token : NTkwOTM2NzMzNzg1NTIyMjA1.XQpfOA.2655fVoRtNpa52RcIn-AoGqGOcA

import discord
import asyncio

client = discord.Client()
token = "NTkwOTM2NzMzNzg1NTIyMjA1.XQpfOA.2655fVoRtNpa52RcIn-AoGqGOcA"


@client.event
async def on_ready():
    game = discord.Game("Just testing")
    await client.change_presence(activity=game)


@client.event
async def on_message(message):

    channel = message.channel

    if message.author.bot:
        return None

    if message.content == "테스트":
        await channel.send("테스트입니다!")


client.run(token)