import discord
import json


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
        
        # Swear words detector
        swear_words = ["씨발", "싸발", "ㅅㅂ", "좆", "ㅈ같네", "병신", "ㅂㅅ", "ㅄ", "쌍", "썅", "ㅆ", "새끼"]
        for word in swear_words:
            if word in message.content:
                try: await message.delete()
                except: print("<Unable to delete message>")
                else:
                    swear_detector_detects = "{0.author}님 욕하지 마세요~~^^"
                    await message.channel.send(swear_detector_detects.format(message))
         
        # Settings test
        if message.content.startswith(': change'):
            print('change!!')

            new_string = message.content[9:]  # Text without prefixs

            # Make 'settings' object from 'settings.json'
            with open('settings.json', 'r', encoding='utf-8') as settings_file:
                settings = json.load(settings_file)

            # Write data to 'settings' object
            settings['temp'] = new_string 
            print(new_string)

            # Write and update settings.json
            with open('settings.json', 'w', encoding='utf-8') as settings_file:
                json.dump(settings, settings_file, indent='\t', ensure_ascii=False)
                
        
client = MyClient()
client.run(secrets["token"])

