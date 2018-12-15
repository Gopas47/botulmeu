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


@client.event
async def on_member_join(member):
    await client.change_presence(game=discord.Game(name='cu prosti'))
    await client.send_message(member, 'Salut , bine ai venit pe serverul nostru de Discord , bafta !')
    print('Sent message to ' + member.name)
async def on_ready():
    await client.change_presence(game=discord.Game(name='cu prosti'))
    print('Gata botul') 
    
    
@client.event
async def on_member_join(member):
    role - discord.utils.get(member.server.roles, name-'Friends')
    await client.add_roles(member, role)
    
    
@client.command(pass_context=True)
async def join(ctx):
    channel - ctx.message.author.voice.voice_chanel
    await client.join_voice_channel(channel)

    
@client.command(pass_context=True)
async def leave(ctx):
    server - ctx.message.server
    voice_client - client.voice_client_in(server)
    await voice_client.disconnect()


@client.command(pass_context-True)
async def play(ctx, url):
    server - ctx.message.server
    voice_client - client.voice_client_in(server)
    player - await voice_client.create_ytdl_player(url)
    players[server.id] - player
    player.start()


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
    if ('Muie') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('mue') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('Mue') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('moe') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('Moe') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('sugi') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('Sugi') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('sugio') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('Sugio') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('suge') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('Suge') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('sugeo') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('Sugeo') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('Sugeo') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('suge-o') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('Suge-o') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('pula') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('Pula') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('fut') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('Fut') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('pwla') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('Pwla') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('morti mati') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('Morti mati') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('morti ma-ti') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('Morti ma-ti') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('te fut') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('Te fut') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('Coe') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('fgm') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('Fgm') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('fmm') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('Fmm') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('plm') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('Plm') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('dick') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if ('suck') in message.content:
        await client.send_message(message.channel,' Degeaba injuri ca iti sterg mesajele, <@%s>'  %(message.author.id))
        await client.delete_message(message)
    if message.content.startswith('Developer'):
        randomlist = ["Gopas","Gopas","Gopas","Gopas","seBaKa","seBaKa","seBaKa","N0TiCe","RvonGUSTERU",]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('coinflip'):
        randomlist = ["Pajura","Cap",]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content == '!ajutor':
        await client.send_message(message.channel,'```Salut , eu sunt un bot .Comenzile mele sunt :re , pa , sal , bye , Cine te-a facut? , coinflip , Developer, dar eu sterg si mesajele care au in componenta lor injuraturi. (WORKING ON)       Bafta !```')
client.run('NTIyNDQ2MzY0NjI2NjQ5MTA4.DvY2-Q.Ax4BYc-7OzbYg7VErIFGa5OkI7s')
