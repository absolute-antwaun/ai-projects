import os
import requests

SPRITE_DIR = "assets/sprites"
POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon/"

os.makedirs(SPRITE_DIR, exist_ok=True)

def download_sprite(pokemon_id):
    url = f"{POKEAPI_URL}{pokemon_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        sprite_url = data['sprites']['front_default']
        if sprite_url:
            img_data = requests.get(sprite_url).content
            file_path = os.path.join(SPRITE_DIR, f"{pokemon_id}.png")
            with open(file_path, "wb") as f:
                f.write(img_data)
            print(f"✅ Downloaded Pokémon #{pokemon_id}")
        else:
            print(f"⚠️ No sprite for Pokémon #{pokemon_id}")
    else:
        print(f"❌ Failed to fetch Pokémon #{pokemon_id}")

if __name__ == "__main__":
    for i in range(1, 152):
        download_sprite(i)