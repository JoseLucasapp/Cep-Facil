import json, requests
from tkinter import *

#cep logradouro complemento bairro localidade uf ddd

window = Tk()
window.title('Buscar CEP')

def search_cep():
    cep = 58600000
    response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    conteudo = json.loads(response.content)
def onlyInt(value):
    if value.isdigit():
        return True
    else:
        return False
validate = window.register(func=onlyInt)

labelquestion1 = Label(window,text='Insira o cep aqui')
labelquestion1.place(x=200,y=5)
cep = Entry(window,width=20, bg='gray', validate='key', validatecommand=(validate, '%P'))
cep.place(x=190,y=35)

window.maxsize(width = 500, height=500)
window.minsize(width = 500, height=500)
window.geometry('500x500')
window.mainloop()