import os
from time import sleep
from dotenv import load_dotenv

load_dotenv()

import discord


client = discord.Client()
low = 10


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):

    if message.author == client.user:
        return
    channel = message.channel

    message_text = str(message.content).lower()
    print(message_text)

    if message_text.startswith("!test"):

        await channel.send("Hello you <@!" + str(message.author.id) + ">")

    if message_text.startswith("!num"):
        spaces = message_text.split(" ")

        val = spaces[1]
        print(val)

        if int(val) < low:
            for i in range(int(val)):
                print("sending")
                await channel.send(
                    "https://tenor.com/view/buchini-scalise-sdg-vermepiatto-bouchini-gif-16911294"
                    + " "
                    + str(i + 1)
                )
                sleep(1)
        else:
            await channel.send("only lower than " + str(low) + " allowed")

    if message_text.startswith("!stop"):
        await client.logout()


client.run(os.environ["BOT_SECRET"])
