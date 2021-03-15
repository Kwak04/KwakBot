import discord
import json

from discord import colour
from discord import embeds
from discord import channel


# Load token from secrets.json
with open('secrets.json') as secrets_file:
   secrets = json.load(secrets_file) 

# Set up
class MyClient(discord.Client):

    # When KwakBot successfully logged in
    async def on_ready(self):
        print('Logged on as {0}'.format(self.user))

    # Main codes are here
    async def on_message(self, message):
        
        message_content = message.content
        channel = message.channel
        
        # Don't reply to yourself
        if message.author == client.user: return

        # Swear words detector
        swear_words = ["씨발", "싸발", "ㅅㅂ", "좆", "ㅈ같네", "병신", "ㅂㅅ", "ㅄ", "쌍", "썅", "ㅆ", "새끼"]
        for word in swear_words:
            if word in message_content:
                try: await message.delete()
                except: print("<Unable to delete message>")
                else:
                    swear_detector_detects = "<@{0.author.id}>님 욕하지 마세요~~^^"

                    swear_detector_embed = discord.Embed(
                            title='욕설이 감지되었습니다.',
                            description=swear_detector_detects.format(message),
                            colour=0xff0000)

                    await channel.send(embed=swear_detector_embed)
         
        
client = MyClient()
client.run(secrets["token"])

