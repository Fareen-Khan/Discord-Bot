import discord
import os
# from discord import channel
from discord.ext import commands
# from discord.ext.commands.core import _CaseInsensitiveDict
import requests
from bs4 import BeautifulSoup
import pandas as pd
import random 

client = commands.Bot(command_prefix='>', case_insensitive=True)

# ----- EVENTS -----
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# ----- COMMANDS ------
@client.command(aliases = ['c'])
async def covid(ctx):
    dfs = pd.read_html('https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data/Canada_medical_cases_by_province')
    embed = discord.Embed(color=discord.Colour.blue())
    embed.set_author(name='Total Cases Canada')
    embed.add_field(name= 'Cases:', value = str(dfs[0].iloc[14,4]), inline=False)
    embed.add_field(name= 'Recovered:', value = str(dfs[0].iloc[14,6]), inline=False)
    embed.add_field(name= 'Deaths:', value = str(dfs[0].iloc[14,7]), inline=False)
    await ctx.send(embed=embed)

@client.command()
async def byebye(ctx):
    await ctx.send('Bye!')
    await client.logout()

@client.command()
async def blep(ctx):
    embed = discord.Embed(color=discord.Colour.blue())
    source = requests.get('https://www.google.com/search?q=blep+cat&sxsrf=ALeKk038P6HibR5kMNy6Ry2D1aUdCUJsAg:1621623149666&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjtiK7-uNvwAhXUHDQIHdONBj4Q_AUoAXoECAEQAw&biw=1504&bih=860').text
    soup = BeautifulSoup(source, 'lxml')
    icon = soup.find_all('img')
    image = []
    for link in icon:
        image.append(link.get('src'))
    post = random.choice(image)
    embed.set_author(name = 'Blep')
    embed.set_image(url = post)
    await ctx.send(embed=embed)


client.run('NzM5OTQwNDI4MDk4NTY4MzE0.XyhxOQ.ucZczqG1SYigm8DsiL_K2EZsIUA')