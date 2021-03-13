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
        print('Message from {0.author}: {0.content}'.format(message))
        
client = MyClient()
client.run(secrets["token"])

