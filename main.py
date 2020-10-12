import json, requests
from tkinter import *

window = Tk()
window.title('Buscar CEP')
#cep logradouro complemento bairro localidade uf ddd
cep = 58600000
response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
conteudo = json.loads(response.content)

window.maxsize('500x500')
window.minsize('500x500')
window.geometry('500x500')
window.mainloop()