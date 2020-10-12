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
lbl1 = Label(cep, text='cep')
lbl1.grid(column = 0, row=0)
lbl2 = Label(endereco, text='endereco')
lbl2.grid(column = 0, row=0)
tab_control.pack(expand = 1, fill='both')

def search_cep():
    uf = 'PB'
    cidade = 'Santa Luzia'
    bairro = 'Frei Damião'
    response = requests.get(f"https://viacep.com.br/ws/{uf}/{cidade}/{bairro}/json/")
    conteudo = json.loads(response.content)
    cep = conteudo[0]['cep']
    messagebox.showinfo('CEP',cep)
def search_endereco():
    cep = '58600000'
    response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    conteudo = json.loads(response.content)
    if conteudo['bairro']:
        endereco = conteudo['bairro'] +' / ' + conteudo['localidade']+' / ' + conteudo['uf']
    else:
        endereco = conteudo['localidade'] +' / ' + conteudo['uf']
    messagebox.showinfo('Endereço', endereco)
#----- Pagina 1 -----#
btn1 = Button(cep,text='Buscar CEP',command=search_cep)
btn1.grid(column = 2, row=1)

#----- Pagina 2 -----#
btn2 = Button(endereco, text='Buscar Endereço',command=search_endereco)
btn2.grid(column = 2, row = 1)

window.maxsize(width = 500, height=500)
window.minsize(width = 500, height=500)
window.geometry('500x500')
window.mainloop()