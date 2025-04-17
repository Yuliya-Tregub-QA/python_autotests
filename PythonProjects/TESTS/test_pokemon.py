import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'ea27702853966db8c7df07294e42fbaa'
HEADER = {'Content-Type':'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '29255'



def test_status_code():
    responce = requests.get(url = f'{URL}/trainers')
    assert responce.status_code == 200


def test_trainer_name():
    responce_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert responce_get.json()["data"][0]["trainer_name"] == 'SunRise19'


