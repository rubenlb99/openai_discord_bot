import discord
import os
import asyncio

from gpt import generate_text

intents = discord.Intents().all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print('OpenAi bot arrived, {0.user}'.format(client))
  print(os.path.realpath(__file__))
  await client.get_channel(877569672340471830).send(
    'OpenAi bot arrived, {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$chatgpt'):
    prompt = message.content.replace('$chatgpt ', '')
    msg = generate_text(prompt)

    await message.channel.send(msg)
    
    return


client.run(os.environ['BOT_TOKEN'])
