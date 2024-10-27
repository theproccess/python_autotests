import requests, pytest



URL = 'https://api.pokemonbattle.ru/v2'
Token = 'token you'
Header = {'Content-Type':'application/json','trainer_token':Token}
Tr_id = '6903'

def test_stcode():
    response=requests.get(url=f'{URL}/pokemons', params={'trainer_id':Tr_id})
    assert response.status_code == 200

def test_part_of_response():
    response_get=requests.get(url=f'{URL}/pokemons', params={'trainer_id':Tr_id})
    assert response_get.json()["data"][4]["name"]=='hippowdon'

@pytest.mark.parametrize('key,value',[('name','hippowdon'),('trainer_id',Tr_id),('id','116191')])

def test_parametrize(key,value):
    response_parametrize=requests.get(url=f'{URL}/pokemons', params={'trainer_id':Tr_id})
    assert response_parametrize.json()["data"][4][key] == value

def test_trname():
    response_trname=requests.get(url=f'{URL}/trainers', params={'trainer_id':Tr_id})
    assert response_trname.json()["data"][0]["trainer_name"]== 'Kafka'