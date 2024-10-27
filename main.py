

import requests

URL = 'https://api.pokemonbattle.ru/v2'
Token = 'token you'
Header = {'Content-Type':'application/json','trainer_token':Token}
body_reg = {
    "trainer_token": Token
}
body_creat = {
    "name": "generate",
    "photo_id": -1
}



response_creat=requests.post(url=f'{URL}/pokemons',headers=Header, json=body_creat)
print(response_creat.status_code)
print(response_creat.text)
poke_id = response_creat.json()['id']
#print(poke_id)
print(response_creat.json()['message'])

body_name ={
    "pokemon_id": poke_id,
    "name": "Cherrt"
}

body_pokeb={
    "pokemon_id": poke_id
}

response_name=requests.patch(url=f'{URL}/pokemons',headers=Header, json=body_name)
print(response_name.text)
print(response_name.json()['message'])
response_pokeb=requests.post(url=f'{URL}/trainers/add_pokeball',headers=Header, json=body_pokeb)
print(response_pokeb.text)
print(response_pokeb.json()['message'])