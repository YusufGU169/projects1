import discord
from discord.ext import commands
from bilgiler import *
import random 
import os
img_name = random.choice(os.listdir("images"))
img_name2 = random.choice(os.listdir("images2"))
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='#', intents=intents)
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')
@bot.command()
async def merhaba(ctx):
    await ctx.send(f'hello! Ben {bot.user}, bir Discord sohbet botuyum!')
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def assalamualaikum(ctx):
    await ctx.send("عليكم السلام!")
@bot.command()
async def السلامعليكم(ctx):
    await ctx.send("عليكم السلام!")
@bot.command()
async def turkiyedekacilvardir(ctx):
    await ctx.send("Türkiye'de 81 il vardır.")
@bot.command()
async def turkiyeninencoknufusasahipolanilihangisidir(ctx):
    await ctx.send("İstanbul en çok nüfusa sahip olan ildir. 31 Aralık 2020'de nüfusu 15,46 milyondur.")
@bot.command()
async def sifre(ctx):
    karakter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    sifrem = ""

    for i in range(8):
        sifrem = sifrem + random.choice(karakter)
        await ctx.send(sifrem)
@bot.command()
async def hi(ctx):
    await ctx.send("Hi!")
@bot.command()
async def salam(ctx):
    await ctx.send("Salam!")
@bot.command()
async def gmail(ctx):
    hk = "abcdefghijklmnopqrstuvwxyz"
    sk = "1234567890"

    mail = ""

    for i in range(8):
        mail = mail + random.choice(hk)
    for i in range(4):
        mail = mail + random.choice(sk)
    mail = mail + "@gmail.com"
    await ctx.send(mail)
@bot.command()
async def mem(ctx):
    with open(f'images/{img_name}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)
@bot.command()
async def animal_mem(ctx):
    with open(f'images2/{img_name2}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)
bot.run(token)
