import json, requests
from tkinter import *

cep = 58600000
response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
conteudo = json.loads(response.content)
print(conteudo)