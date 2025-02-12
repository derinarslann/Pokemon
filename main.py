import discord
from discord.ext import commands
from config import token
from logic import Pokemon, Wizard, Fighter
import random

# Bot için niyetleri (intents) ayarlama
intents = discord.Intents.all()  # Varsayılan ayarların alınması
intents.messages = True              # Botun mesajları işlemesine izin verme
intents.message_content = True       # Botun mesaj içeriğini okumasına izin verme
intents.guilds = True                # Botun sunucularla (loncalar) çalışmasına izin verme

# Tanımlanmış bir komut önekine ve etkinleştirilmiş amaçlara sahip bir bot oluşturma
bot = commands.Bot(command_prefix='!', intents=intents)

# Bot çalışmaya hazır olduğunda tetiklenen bir olay
@bot.event
async def on_ready():
    print(f'Giriş yapıldı:  {bot.user.name}')  # Botun adını konsola çıktı olarak verir

# '!go' komutu
@bot.command()
async def go(ctx):
    author = ctx.author.name  # Mesaj yazarının adını alma
    # Kullanıcının zaten bir Pokémon'u olup olmadığını kontrol edin. Eğer yoksa, o zaman...
    if author not in Pokemon.pokemons.keys():
        x = random.randint(1,3)
        if x == 1:
            pokemon = Pokemon(author)  # Yeni bir Pokémon oluşturma
        elif x == 2:
            pokemon = Fighter(author)  # Yeni bir Pokémon oluşturma
        elif x == 1:
            pokemon = Wizard(author)  # Yeni bir Pokémon oluşturma
        else:
            print("HATAAA!")
        await ctx.send(await pokemon.info())  # Pokémon hakkında bilgi gönderilmesi
        image_url = await pokemon.show_img()  # Pokémon resminin URL'sini alma
        if image_url:
            embed = discord.Embed()  # Gömülü mesajı oluşturma
            embed.set_image(url=image_url)  # Pokémon'un görüntüsünün ayarlanması
            await ctx.send(embed=embed)  # Görüntü içeren gömülü bir mesaj gönderme
            await ctx.send(Pokemon.pokemons)
        else:
            await ctx.send("Pokémonun görüntüsü yüklenemedi!")
    else:
        await ctx.send(Pokemon.pokemons)
        await ctx.send("Zaten kendi Pokémonunuzu oluşturdunuz!")  # Bir Pokémon'un daha önce yaratılıp yaratılmadığını gösteren bir mesaj

@bot.command()
async def attack(ctx ,enemy):
    if enemy in Pokemon.pokemons:
        saldıran= Pokemon.pokemons[ctx.author.name]
        savunan= Pokemon.pokemons[enemy]
        sonuç= await saldıran.saldır(savunan)
        await ctx.send(sonuç)
    else:
        await ctx.send("düşman bulunamadı")

@bot.command()
async def feed(ctx):
    pass


# Botun çalıştırılması
bot.run(token)
