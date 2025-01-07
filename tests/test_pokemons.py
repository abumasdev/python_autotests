import requests
import pytest

URL = 'https://api.pokemonbattle.ru'
TOKEN = 'USER_TOKEN'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '13187'

def test_status_code():
    response = requests.get(url = f'{URL}/v2/trainers', params = {'trainer_id': TRAINER_ID} )
    assert response.status_code == 200

def test_trainer_name():
    response = requests.get(url = f'{URL}/v2/trainers', params = {'trainer_id': TRAINER_ID} )
    assert response.json()['data'][0]['trainer_name'] == 'Мастер Абу'

# def test_status():
#     response = requests.get(url = f'{URL}/v2/pokemons', params = {'trainer_id': TRAINER_ID} )
#     assert response.status_code == 200

# def test_pokemon_name():
#     response = requests.get(url = f'{URL}/v2/pokemons', params = {'trainer_id': TRAINER_ID} )
#     assert response.json()['data'][0]['name'] == 'bobr'

# @pytest.mark.parametrize('key, value', [('name', 'bobr'), ('trainer_id', TRAINER_ID), ('id', '179330')])
# def test_patametrize(key, value):
#     response = requests.get(url = f'{URL}/v2/pokemons', params = {'trainer_id': TRAINER_ID} )
#     assert response.json()['data'][0][key] == value