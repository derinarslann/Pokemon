import aiohttp  # Eşzamansız HTTP istekleri için bir kütüphane
import random
import asyncio

class Pokemon:
    pokemons = {}
    # Nesne başlatma (kurucu)
    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = random.randint(1, 1000)
        self.name = None
        if pokemon_trainer not in Pokemon.pokemons:
            Pokemon.pokemons[pokemon_trainer] = self
        else:
            self = Pokemon.pokemons[pokemon_trainer]

    async def get_name(self):
        # PokeAPI aracılığıyla bir pokémonun adını almak için eşzamansız bir yöntem
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API'si
        async with aiohttp.ClientSession() as session:  # Bir HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtının alınması ve kodunun çözülmesi
                    return data['forms'][0]['name']  # Bir Pokémon'un adını döndürme
                else:
                    return "Pikachu"  # İstek başarısız olursa varsayılan adı döndürür

    async def info(self):
        # Pokémon hakkında bilgi döndüren bir metot
        if not self.name:
            self.name = await self.get_name()  # Henüz yüklenmemişse bir adın geri alınması
            self.attack = await self.get_attack()
            self.hp = await self.get_hp()
            self.height = await self.get_height()
        return f"Pokémonunuzun ismi: {self.name}\nPokémonunuzun atağı: {self.attack}\nPokémonunuzun canı: {self.hp}\nPokémonunuzun boyu: {self.height}\n"  # Pokémon'un adını içeren dizeyi döndürür

    async def show_img(self):
        # PokeAPI aracılığıyla bir pokémon görüntüsünün URL'sini almak için eşzamansız bir yöntem
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API'si
        async with aiohttp.ClientSession() as session:  # Bir HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtının alınması ve kodunun çözülmesi
                    return data['sprites']['front_default']  # Bir Pokémon'un adını döndürme
                else:
                    return "Pikachu"  # İstek başarısız olursa varsayılan adı döndürür
    
    async def get_attack(self):
        # PokeAPI aracılığıyla bir pokémonun adını almak için eşzamansız bir yöntem
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API'si
        async with aiohttp.ClientSession() as session:  # Bir HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtının alınması ve kodunun çözülmesi
                    return data['stats'][1]['base_stat']  # Bir Pokémon'un adını döndürme
                else:
                    return 10  # İstek başarısız olursa varsayılan adı döndürür

    async def get_hp(self):
        # PokeAPI aracılığıyla bir pokémonun adını almak için eşzamansız bir yöntem
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API'si
        async with aiohttp.ClientSession() as session:  # Bir HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtının alınması ve kodunun çözülmesi
                    return data['stats'][0]['base_stat']*5  # Bir Pokémon'un adını döndürme
                else:
                    return 10  # İstek başarısız olursa varsayılan adı döndürür

    async def get_height(self):
        # PokeAPI aracılığıyla bir pokémonun adını almak için eşzamansız bir yöntem
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API'si
        async with aiohttp.ClientSession() as session:  # Bir HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtının alınması ve kodunun çözülmesi
                    return data['height']  # Bir Pokémon'un adını döndürme
                else:
                    return 10  # İstek başarısız olursa varsayılan adı döndürür
    
    async def saldırı(self,enemy):
        
        if isinstance(enemy, Wizard):
            x = random.randint(1,10)
            if x == 2:
                return f"{enemy.name} kalkan açtı ve hasar almadı"
        
        if self.attack >= enemy.hp:
            return f"{self.name}, {enemy.name}'ye saldırdı. Kullanılan Güç: {self.attack}"
        else:
            enemy.hp -= self.attack
            return f"{self.name}, {enemy.name}'ye saldırdı. {enemy.name}'nin {enemy.hp} canı kaldı."
        

class Fighter(Pokemon):
    async def saldırı(self,enemy):
        bonus = random.randint(1, 50)
        self.attack += bonus
        sonuç = await super().saldırı(enemy)
        self.attack -= bonus
        return f"{sonuç} Bonus attack: {bonus}"

class Wizard(Pokemon):
    pass

if __name__ == "__main__":
    async def deneme():
        ben = Fighter("derin")
        enemy = Wizard("abc")

        print(await ben.info())
        print(await enemy.info())
        print(await ben.saldırı(enemy))
        print(await enemy.saldırı(ben))
        

    asyncio.run(deneme())