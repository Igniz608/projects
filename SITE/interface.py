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
interface.geometry("600x450")
# interface.maxsize(600,450)
# interface.minsize(100,75)
interface.resizable(False,False)
interface.config(bg="#6959CD")

img=PhotoImage(file="imagennnn/logopython.png")
img2=PhotoImage(file="imagennnn/miles.png")

logo=Label(interface)
logo.pack(fill="x", expand=TRUE, anchor=N, ipady= 30)
fundo=Label(logo, image=img)

fundo.place(x=0, y=0)

foto=Label(interface, image=img2)
foto.place(x=-2, y=0)

retangulo=LabelFrame(interface, bg= "#290c3e")
retangulo.pack(fill="y", expand=TRUE, anchor=CENTER, ipadx= 100, ipady=100, pady=60)

tnome=Label(interface,text="USUÁRIO", bg="#290c3e", foreground='white')
tnome.place(relx=0.40, rely=0.38)
nome=Entry(interface)
nome.place(relx=0.40, rely=0.44)

email=Label(interface,text="E-MAIL", bg="#290c3e", foreground='white')
email.place(relx=0.40, rely=0.53)
temail=Entry(interface,relief= FLAT)
temail.place(relx=0.40, rely=0.58)

tsenha=Label(interface,text="SENHA", bg="#290c3e", foreground='white')
tsenha.place(relx=0.40, rely=0.68)
senha=Entry(interface,show="*")
senha.place(relx=0.40, rely=0.73)

botao=Button(interface,text="CADASTRAR",width=9, command= cadastrar, bg="#ff8c32")
botao.place(relx=0.38, rely=0.79)

btlogar=Button(interface,text="LOGAR",width=9, command= entrar, bg="#ff8c32")
btlogar.place(relx=0.51, rely=0.79)


psenha=Label(interface,bg="#6959CD",width=10)
psenha.place()

interface.mainloop()