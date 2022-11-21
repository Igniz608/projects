from segunda_interface import*
from distutils.cmd import Command
from tkinter import*
from tkinter.ttk import LabeledScale
from xmlrpc.client import DateTime

"""
def msenha():
 senha["show"]=""

def dsenha():
     senha["show"]="*"

"""

def cadastrar():
     mail = temail.get()
     usuario = nome.get()
     senhausuario = senha.get()
     nomes.append(usuario)
     senhas.append(senhausuario)
     uemail.append(mail)
     print(nomes, senhas, uemail)


interface=Tk()
interface.title("cadastro")
interface.maxsize(600,450)
interface.minsize(100,75)
interface.config(bg="#6959CD")




tnome=Label(interface,bg="#6959CD",text="USUÁRIO")
tnome.grid(row=1,column=1)
nome=Entry(interface)
nome.grid(row=1,column=2)

email=Label(interface,bg="#6959CD",text="E-MAIL")
email.grid(row=3,column=1)
temail=Entry(interface,)
temail.grid(row=3,column=2)

tsenha=Label(interface,bg="#6959CD",text="SENHA")
tsenha.grid(row=4,column=1)
senha=Entry(interface,show="*")
senha.grid(row=4,column=2)

btlogar=Button(interface,text="LOGAR",width=9, command= entrar)
btlogar.grid(row=6,column=2)

botao=Button(interface,text="CADASTRAR",width=9, command= cadastrar)
botao.grid(row=5,column=2)

psenha=Label(interface,bg="#6959CD",width=10)
psenha.grid(row=6,column=1)

interface.mainloop()