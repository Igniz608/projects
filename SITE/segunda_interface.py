import webbrowser
from cgitb import text
from tkinter import*
from tkinter import scrolledtext
from tkinter import messagebox
from turtle import left, position, width

from setuptools import Command
nomes = []
senhas = []
uemail = []

def entrar():

    def logar():
        u=usuario.get()
        s=senha.get()
        if u in nomes:
            for i in range(len(nomes)):
                if u==nomes[i]:
                    print(i)
                    if s==senhas[i]:
                       texto["text"]=("acesso permitido")
                       
                       new=2
                       url="file:///C:/Users/zollner/Desktop/SITE/SITE/site.html"
                       webbrowser.open(url,new=new)
                       messagebox.showinfo(title="confirmado",message='logado')
                       interface.destroy()
                else:
                    texto["text"]=("senha incorreta")
                
            
        else:   
            texto["text"]=("usuario não encontrado")
    interface=Tk()


    interface.config(bg="#06113c")
    interface.maxsize(300,330)
    interface.minsize(300,330)


    usuario=Entry(interface,width=46,)
    usuario.place(rely=0.5,height=50,y=-22,x=10)


    senha=Entry(interface,show="*",width=46)
    senha.place(rely=0.8,height=50,y=-33,x=10)

    botao4=Button(interface, text="CONCLUIR",command=logar,width=10,bg="#ff8c32")
    botao4.place(rely=0.9,x=12,y=-4,height=30)
    texto=Label(interface,text="",bg="#1c264e",fg="white")
    texto.place(rely=0.8,relx=0.5,y=30)

    interface.mainloop()