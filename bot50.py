import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()
async def change_status(self):
    await self.bot.change_presence(game=discord.Game(name="seBaKa", type=0))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content.startswith('re'):
        await client.send_message(message.channel,' Salut ,<@%s>'  %(message.author.id))
    if message.content.startswith('sal'):
        await client.send_message(message.channel,' Salut  <@%s>'  %(message.author.id))
    if message.content.startswith('pa'):
        await client.send_message(message.channel,' Paa, <@%s>'  %(message.author.id))
    if message.content.startswith('bye'):
        await client.send_message(message.channel,' Paa,<@%s>'  %(message.author.id))
    if message.content == 'Cine te-a facut?':
        await client.send_message(message.channel,'Gopas (Scripter,Owner) ,seBaKa (Co-Owner).')
    if ('muie') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('mue') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('moe') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('sugi') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('sugio') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('suge') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('sugeo') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('suge-o') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('pula') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('fut') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('pwla') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('morti mati') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('morti ma-ti') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('te fut') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('Coe') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('fgm') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('fmm') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('plm') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('plm') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('dick') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('suck') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if message.content.startswith('Developer'):
        randomlist = ["Gopas","seBaKa","N0TiCe",]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('coinflip'):
        randomlist = ["Pajura","Cap",]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content == '!ajutor':
        await client.send_message(message.channel,'```Salut , eu sunt un bot .Comenzile mele sunt :re , pa , sal , bye , Cine te-a facut? , coinflip , Developer, dar eu sterg si mesajele care au in componenta lor injuraturi. (WORKING ON)       Bafta !```')
client.run('NTIyNDQ2MzY0NjI2NjQ5MTA4.DvY2-Q.Ax4BYc-7OzbYg7VErIFGa5OkI7s')
