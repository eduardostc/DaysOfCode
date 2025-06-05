import json
import requests
from googletrans import Translator

########################## metodo implementando com a tradução ##########################
# def personagens():

#     api_url = f'https://last-airbender-api.fly.dev/api/v1/characters'

#     personagem = (requests.get(api_url)).json()
#     print(type(personagem))
    
#     translator = Translator()

#     for p in personagem:
#         afiliacao = p.get('affiliation', '')
#         p['affiliacao_traduzida'] = translator.translate(afiliacao, dest='pt').text
#         nome = p.get('name', '')
#         p['name_traduzido'] = translator.translate(nome, dest='pt').text

#     print(personagem)

# personagens()


########################## metodo implementando sem a tradução ##########################
import json
import requests

def personagens():

    api_url = f'https://last-airbender-api.fly.dev/api/v1/characters'

    response = requests.get(api_url)

    print(json.dumps(response.json(), indent=4))

personagens()


