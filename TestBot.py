# client id : 590936733785522205
# client secret : iXr8dowBXR2w_76XaBMGbnbGwg8Axb5H
# token : NTkwOTM2NzMzNzg1NTIyMjA1.XQpfOA.2655fVoRtNpa52RcIn-AoGqGOcA


import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        channel = message.channel

        if message.content == "ㅎㅇ":
            await channel.send('안녕!')


client = MyClient()
client.run("NTkwOTM2NzMzNzg1NTIyMjA1.XQpfOA.2655fVoRtNpa52RcIn-AoGqGOcA")
