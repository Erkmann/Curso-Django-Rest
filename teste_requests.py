import requests
from pprint import pprint

# GET Avaliacoes

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# print(avaliacoes.status_code)

# Acessando os dados da resposta

pprint(avaliacoes.json()['results'][-1]['nome'])
