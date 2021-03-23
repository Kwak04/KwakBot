import discord
from discord.ext import commands

import json


# Setting up discord.ext.commands
bot = commands.Bot(command_prefix=': ')

# Load token from secrets.json
with open('secrets.json') as secrets_file:
   secrets = json.load(secrets_file) 

# When the Bot successfully loggedd in
@bot.event
async def on_ready():
    print('Logged on as {0}'.format(bot.user.name))

# Commands without prefixs are here
@bot.event
async def on_message(message):
    await swear_detector(message)
    
    await bot.process_commands(message)


@bot.command()
async def change(ctx, new_string: str):
    print('cherrycherrychange!!')

    # Make 'settings' object from 'settings.json'
    with open('settings.json', 'r', encoding='utf-8') as settings_file:
        settings = json.load(settings_file)

    # Write data to 'settings' object
    settings['temp'] = new_string 
    print(new_string)

    # Write and update settings.json
    with open('settings.json', 'w', encoding='utf-8') as settings_file:
        json.dump(settings, settings_file, indent='\t', ensure_ascii=False)


# Swear words detector
async def swear_detector(message):
    swear_words = ['씨발', '싸발', 'ㅅㅂ', '시발', '좆', 'ㅈ같네', '병신', 'ㅂㅅ', 'ㅄ', '쌍', '썅', 'ㅆ', '새끼']
    for word in swear_words:
        if word in message.content:
            try: await message.delete()
            except: print('<Unable to delete message>')
            else:
                swear_detector_message = '''<@{0.author.id}>님 욕하지 마세요~~^^
                삭제된 메시지: ||{0.content}||'''

                swear_detector_embed = discord.Embed(
                      title='욕설이 감지되었습니다.',
                      description=swear_detector_message.format(message),
                      colour=0xff0000)

                await message.channel.send(embed=swear_detector_embed)  


bot.run(secrets['token'])

