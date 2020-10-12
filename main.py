import json, requests
from tkinter import *

window = Tk()
window.title('Buscar CEP')

def search_cep():
    uf = 'PB'
    cidade = 'Santa Luzia'
    bairro = 'Frei Damião'
    response = requests.get(f"https://viacep.com.br/ws/{uf}/{cidade}/{bairro}/json/")
    conteudo = json.loads(response.content)
    print(conteudo[0]['cep'])
search_cep()

window.maxsize(width = 500, height=500)
window.minsize(width = 500, height=500)
window.geometry('500x500')
window.mainloop()