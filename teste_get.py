import requests
import jsonpath

from pprint import pprint

headers = {
    'Authorization': 'Token bf654bd324541d783c7c4a78cf97174e47ef64d1'
}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_base_cursos, headers=headers)
pprint(resultado.json())
