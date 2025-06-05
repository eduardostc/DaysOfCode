from django.shortcuts import render
from django.http import HttpResponse
import requests
from googletrans import Translator


########################## metodo implementando com a tradução ##########################
def personagens(request):

    api_url = f"https://last-airbender-api.fly.dev/api/v1/characters"
    response = requests.get(api_url)

    personagem = response.json()

    translator = Translator()

    for p in personagem:
        afiliacao = p.get("affiliation", "")
        p["affiliacao_traduzida"] = translator.translate(afiliacao, dest="pt").text
        nome = p.get("name", "")
        p["name_traduzido"] = translator.translate(nome, dest="pt").text
    
    context = {
        'personagem': personagem
    }

    return render(request, "index.html", context)


########################## metodo implementando com a tradução ##########################

import json

def personagens_sem_traducao(request):

    api_url = f'https://last-airbender-api.fly.dev/api/v1/characters'
    response = requests.get(api_url)

    # 2. Obter os dados como uma lista de dicionários Python
    lista_de_personagens = response.json()
       
    # 3.Preparar o contexto para o template
    context = {
        'personagens': lista_de_personagens # Passar a lista de dicionários diretamente
    }

    return render(request, "personagens_originais.html", context)


