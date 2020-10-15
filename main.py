import json, requests
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import webbrowser

#-------------------------------------#

window = Tk()
window.title('Buscar CEP')

tab_control = ttk.Notebook(window)
cep = ttk.Frame(tab_control)
endereco = ttk.Frame(tab_control)
tab_control.add(cep,text = 'Buscar CEP')
tab_control.add(endereco,text = 'Buscar Endereço')
tab_control.pack(expand = 1, fill='both')

#-------------------------------------#

def search_cep():
    uf = campo_uf.get()
    cidade = campo_cidade.get()
    bairro = campo_bairro.get()
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
def limitarSigla(uf):
    if len(uf)> 2:
        return False
    else:
        return True
def limitarCEP(cep):
    if len(cep) > 8:
        return False
    else:
        return True
def acessarSites(site):
    webbrowser.open_new(site)

#-------------------------------------#
validaruf = window.register(func=limitarSigla)
validarcep = window.register(func=limitarCEP)

#----- Pagina 1 -----#
label_uf = Label(cep,text='Informe o Estado')
campo_uf = Entry(cep, validate='key', validatecommand=(validaruf,'%P'))
label_cidade = Label(cep, text='Informe a Cidade')
campo_cidade = Entry(cep)
label_bairro = Label(cep,text='Informe o Bairro')
campo_bairro = Entry(cep)
btn_cep = Button(cep,text='Buscar CEP', command = search_cep)

#-----Posicionando------#
label_uf.place(x=215,y=10)
label_cidade.place(x=215,y=70)
label_bairro.place(x=215,y=130)

campo_uf.place(x=200,y=30)
campo_cidade.place(x=200,y=90)
campo_bairro.place(x=200,y=150)

btn_cep.place(x=225,y=200)

#----- Pagina 2 -----#
label_cep = Label(endereco,text='Informe o CEP')
campo_cep = Entry(endereco, validate='key', validatecommand=(validarcep,'%P'))

btn_endereco = Button(endereco, text='Buscar Endereço',command=search_endereco)

#-----Posicionando------#
label_cep.place(x=220,y=10)

campo_cep.place(x=200,y=40)

btn_endereco.place(x=210,y=80)
#-------------------------------------#
versao = Label(window, text='V 1.0')
versao.place(x=190,y=420)
link = Label(window, text="Acesse no Github", cursor="hand2", fg="blue")
link.place(x=240,y=420)
link.bind("<Button>",lambda e: acessarSites('https://github.com/JoseLucasapp/Busca-por-cep'))

window.maxsize(width = 500, height=500)
window.minsize(width = 500, height=500)
window.geometry('500x500')
window.mainloop()