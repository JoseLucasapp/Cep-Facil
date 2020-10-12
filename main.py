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
#-Label's-#
labelquestion1 = Label(window,text='Insira o cep aqui',font="Verdana 12 bold italic")
labelquestion1.place(x=190,y=5)
#-Entry's-#
cep = Entry(window,width=20, bg='gray',font="Verdana 12 bold italic", validate='key', validatecommand=(validate, '%P'))
cep.place(x=157,y=35)
#-Button-#
button = Button(window,text='Buscar CEP', font="Verdana 14 bold italic", bg='green', fg='white')
button.place(x=195,y=65)

window.maxsize(width = 500, height=500)
window.minsize(width = 500, height=500)
window.geometry('500x500')
window.mainloop()