from django.shortcuts import render
from django.http import HttpResponse
import requests
from googletrans import Translator



def personagens(request):

    pagina = request.GET.get('page', 1)
    quantidade_por_pagina = 10
    api_url = f'https://last-airbender-api.fly.dev/api/v1/characters?perPage={quantidade_por_pagina}&page={pagina}'

    response = requests.get(api_url)

    personagem = response.json()

    translator = Translator()

    for p in personagem:
        afiliacao = p.get("affiliation", "")
        p["affiliacao_traduzida"] = translator.translate(afiliacao, dest="pt").text
        nome = p.get("name", "")
        p["name_traduzido"] = translator.translate(nome, dest="pt").text
    
    context = {
         'personagem': personagem,
         'page': int(pagina)
    }


    return render(request, "index.html", context)


########################## Como Corrigir ID para dar Continuidade ##########################

# def personagens(request):
#     # 1. Obter os parâmetros da página
#     pagina = int(request.GET.get('page', 1)) # Garantir que seja um inteiro
#     quantidade_por_pagina = 10
    
#     # 2. Fazer a chamada à API
#     api_url = f'https://last-airbender-api.fly.dev/api/v1/characters?perPage={quantidade_por_pagina}&page={pagina}'
#     response = requests.get(api_url)
#     personagem = response.json()

#     # 3. Calcular o número inicial para a página atual
#     # Para a página 1, start_index = (1 - 1) * 10 = 0
#     # Para a página 2, start_index = (2 - 1) * 10 = 10
#     # Para a página 3, start_index = (3 - 1) * 10 = 20
#     # etc...
#     start_index = (pagina - 1) * quantidade_por_pagina

#     # 4. Traduzir e adicionar o ID contínuo
#     translator = Translator()
#     # Usamos enumerate para ter o índice do item na lista atual (0, 1, 2...)
#     for i, p in enumerate(personagem):
#         # Adiciona uma nova chave ao dicionário do personagem
#         p['id_continuo'] = start_index + i + 1  # +1 porque enumerate começa em 0

#         afiliacao = p.get("affiliation", "")
#         p["affiliacao_traduzida"] = translator.translate(afiliacao, dest="pt").text
#         nome = p.get("name", "")
#         p["name_traduzido"] = translator.translate(nome, dest="pt").text
    
#     # 5. Passar os dados para o contexto
#     context = {
#         'personagem': personagem,
#         'page': pagina
#     }

#     return render(request, "index.html", context)



# <tbody>
#     {% for p in personagem %}
#     <tr>
#         <td>{{ p.id_continuo }}</td>
        
#         <td><img src="{{ p.photoUrl }}" alt="{{ p.name }}"
#                 class="img-fluid rounded-circle" style="width: 50px; height: 50px;"></td>
#         <td>{{ p.name_traduzido }}</td>
#         <td>{{ p.affiliacao_traduzida }}</td>
#         <td>{{ p.allies|last }}</td>
#         <td>{{ p.enemies|last }}</td>
#     </tr>
#     {% endfor %}
# </tbody>

########################## metodo implementando com a tradução ##########################
# def personagens(request):
    
#     api_url = f"https://last-airbender-api.fly.dev/api/v1/characters"
#     response = requests.get(api_url)

#     personagem = response.json()

#     translator = Translator()

#     for p in personagem:
#         afiliacao = p.get("affiliation", "")
#         p["affiliacao_traduzida"] = translator.translate(afiliacao, dest="pt").text
#         nome = p.get("name", "")
#         p["name_traduzido"] = translator.translate(nome, dest="pt").text
    
#     context = {
#         'personagem': personagem
#     }

#     return render(request, "index.html", context)


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


