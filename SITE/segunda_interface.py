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
                       url="C:\Users\joao.matos\Desktop\SITE\site.html"
                       webbrowser.open(url,new=new)
                       messagebox.showinfo(title="confirmado",message='logado')
                       interface.destroy()
                else:
                    texto["text"]=("senha incorreta")
                
            
        else:   
            texto["text"]=("usuario não encontrado")
    
    interface=Tk()
    interface.config(bg="#06113c")
    interface.geometry("600x450")
    # interface.maxsize(300,330)
    # interface.minsize(300,330)
    interface.resizable(False,False)
    interface.config(bg="#6959CD")

   
    # img3=PhotoImage(file="imagem2/miles2.png")

    

    # foto3=Label(interface, image=img3)
    # foto3.place(x=-2, y=0)

    # foto3.place(x=0, y=0)

    retangulo2=LabelFrame(interface, bg= "#290c3e")
    retangulo2.pack(fill="y", expand=TRUE, anchor=CENTER, ipadx= 100, ipady=100, pady=130)


    lusuario=Label(interface,text="USUÁRIO", bg="#290c3e", foreground='white')
    lusuario.place(relx=0.40, rely=0.36)
    usuario=Entry(interface)
    usuario.place(relx=0.40, rely=0.42)

    lsenha= Label(interface,text="SENHA", bg="#290c3e", foreground='white')
    lsenha.place(relx=0.40, rely=0.51)
    senha=Entry(interface,show="*")
    senha.place(relx=0.40, rely=0.56)

    botao4=Button(interface, text="CONCLUIR",command=logar,width=10,bg="#ff8c32")
    botao4.place(relx=0.44, rely=0.64)
    texto=Label(interface,text="",bg="#6959CD",fg="white")
    texto.place(rely=0.8,relx=0.5,y=28)

    interface.mainloop()