import requests

URL = 'https://api.pokemonbattle.ru'
TOKEN = 'USER_TOKEN'
HEADER = {
    'Content-Type': 'application/json',
    'trainer_token': TOKEN
}

# Создание покемона
body_create_pokemon = {
    'name': 'generate',
    'photo_id': -1
}
response = requests.post(url = f'{URL}/v2/pokemons', headers = HEADER, json = body_create_pokemon)
print(response.status_code, response.text)
pokemon_id = response.json()['id']

# Смена имени покемона
body_change_name_pokemon = {
    'pokemon_id': pokemon_id,
    'name': 'bobr'
}
response = requests.patch(url = f'{URL}/v2/pokemons', headers = HEADER, json = body_change_name_pokemon)
print(response.status_code, response.text)

# Поймать покемона в покебол
body_catch_at_pokeball = {
    'pokemon_id': pokemon_id
}
response = requests.post(url = f'{URL}/v2/trainers/add_pokeball', headers = HEADER, json = body_catch_at_pokeball)
print(response.status_code, response.text)



