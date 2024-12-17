import discord 
import random 
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"Zalogowano jako {bot.user.name}")

@bot.command()
async def plastyka(ctx,):
    wybor1 = random.choice(['Dynia hallowen'
                            , 'Kartka na walentynki'
                            ,'Ludziki z kasztanów'
                            ,'Ludziki z plasteliny'
                            ,'Makieta swojego pokoju'])
    await ctx.send(f"Według mnie powinieneś zrobić: {wybor1}")

sort_dictionry = {
        "bio" : ["jedzenie","Ogryzek"],
        "plastik": ["butelka", "puszka"],
        "papier" : ["karton,papier"],
        "szklo" : ["ekran","słoiki","szklanki"] }
    
@bot.command()
async def sort(ctx,product):
    for key,value in sort_dictionry.items():
        if product in value:
            await ctx.send(f'Wrzuć do pojemnika na {key}')
        else:
            await ctx.send("Brak w  bazie danych")


rozklad = {
    "plastik": '1000 lat',
    "szkło": "1000 lat",
    "bio": "2 tygodnie",
    "papier": "2-5 miesiecy",
    'metal' : 'Sto lat',
}
@bot.command()
async def rozklad(ctx,product):
    if product in rozklad.keys():
        await ctx.send(f"Czas rozkładu {product}: {rozklad[product]}")
    else:
        await ctx.send('nie rozumiem')

















bot.run("MTI4NTYzNTA0MjQ2MjI2OTUyMA.GB5iBa.fRh7QWEUvSJbbaLd07yXF93KzBCmW5tG7ZDnuk")





