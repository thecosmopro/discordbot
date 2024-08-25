# discordbot

# This example requires the 'message_content' intent.

import discord
from botmantik import sifre_olusturucu, double_letter, sayi_tahmin

intents_discord = discord.Intents.default()
intents_discord.message_content = True


client = discord.Client(intents=intents_discord)

# @ başlarsa dekaratördür. dekartörler fonksiyonların çalışma işemini belirli olaylara göre değiştirir.
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!selam'):
        await message.channel.send('Merhaba Nasılsın?')
    elif message.content.startswith('!iyiyim'):
        await message.channel.send('İyi olduğuna sevindim!')
    elif message.content.startswith('!kötüyüm'):
        await message.channel.send('Senin için ne yapabilirim?')
    elif message.content.startswith('!şifre oluştur'):
        await message.channel.send(f'Senin için 10 Haneli Şifre Oluşturdum: {sifre_olusturucu(10)}')
    elif message.content.startswith('!çift_harf'):
        await message.channel.send(f'Hello Kelinmesini senin için 2 kez yazdım: {double_letter("hello")}')
    elif message.content.startswith('!sayı tahmin etmece oynayalım'):
        await message.channel.send('1 ile 10 arasında sayı tuttum tahmin et')
    elif message.content.startswith(x):
        await message.channel.send("Doğru Bildin")
    else:
        await message.channel.send("Yanlış")



client.run('token')
