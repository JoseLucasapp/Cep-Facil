import json, requests
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

window = Tk()
window.title('Buscar CEP')

tab_control = ttk.Notebook(window)
cep = ttk.Frame(tab_control)
endereco = ttk.Frame(tab_control)
tab_control.add(cep,text = 'Buscar CEP')
tab_control.add(endereco,text = 'Buscar Endereço')
tab_control.pack(expand = 1, fill='both')

def search_cep():
    uf = 'PB'
    cidade = 'Santa Luzia'
    bairro = 'Frei Damião'
    response = requests.get(f"https://viacep.com.br/ws/{uf}/{cidade}/{bairro}/json/")
    conteudo = json.loads(response.content)
    cep = 'Cep: ' + conteudo[0]['cep']
    messagebox.showinfo('CEP',cep)
def search_endereco():
    cep = campo_cep.get()
    response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    conteudo = json.loads(response.content)
    if conteudo['bairro']:
        endereco = conteudo['bairro'] +' / ' + conteudo['localidade']+' / ' + conteudo['uf']
    else:
        endereco = conteudo['localidade'] +' / ' + conteudo['uf']
    messagebox.showinfo('Endereço', endereco)
#----- Pagina 1 -----#

btn1 = Button(cep,text='Buscar CEP',command=search_cep)
btn1.place(x=0,y=0)

#----- Pagina 2 -----#
campo_cep = Entry(endereco)
campo_cep.place(x=200,y=10)
btn2 = Button(endereco, text='Buscar Endereço',command=search_endereco)
btn2.place(x=200,y=100)

window.maxsize(width = 500, height=500)
window.minsize(width = 500, height=500)
window.geometry('500x500')
window.mainloop()