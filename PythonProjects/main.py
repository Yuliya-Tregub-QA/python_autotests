import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'ea27702853966db8c7df07294e42fbaa'
HEADER = {'Content-Type':'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "Крутяшка",
    "photo_id": 119
}

body_new_name = {
    "pokemon_id": "292800",
    "name": "SuperPuper",
    "photo_id": 120
}

body_add_pokeball = {
    "pokemon_id": "292803"
}



response_create = requests.post(url = f'{URL}/pokemons', headers=HEADER, json=body_create)
print(response_create.json())


response_new_name = requests.put(url = f'{URL}/pokemons', headers=HEADER, json=body_new_name)
print(response_new_name.json())


response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_add_pokeball)
print(response_add_pokeball.json())