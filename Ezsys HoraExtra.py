from tkinter.ttk import *
from  tkinter  import *
from pandas import *
from tkcalendar import*
from tkinter import filedialog
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from tkinter import messagebox
from tkinter import ttk
from tkinter import Entry
import tkinter  as tk
from tkcalendar import DateEntry
from mysql.connector import Error
from persistence.DbConnecion import DbConnection
from service.LoginService import LoginService
from service.VendaService import VendaService
from service.HoraExtraService import HoraExtraService
from datetime import date, datetime
from workalendar.america import Brazil
from entity.Usuariopc import Usuario
from UI import limpaWidget
from  Leitura import Leitura
from PIL import Image, ImageTk
from tkinter.filedialog import asksaveasfile, asksaveasfilename,askopenfile,askopenfilename
from decimal import Decimal
import numpy as np

janDep = Tk()
janDep.title("Ez Dept. Pessoal (Cadastro de Horas Extras)")
janDep.geometry("1360x760+0+0")
janDep.configure(background="White")
janDep.resizable(width=True, height=True)
janDep.attributes("-fullscreen", 1.1)


logo = PhotoImage(file='Resource\logo\Ezipa.gif')

logo2 = PhotoImage(file='Resource\logo\Ezipanovo.gif')

logo3 = PhotoImage(file='Resource\logo\Logo teste2.png')

img=PhotoImage(file='Resource\logo\EzipaBG.gif')
img=img.subsample(1,0)

janDep.iconbitmap('Resource\Financeiro\Icone.bmp')


DeptopFrame = Frame(janDep, width=9999, height=135, bg="#ff7f27", relief="raise")
DeptopFrame.pack(side=TOP,fill = 'both', expand = True)
DepbottomFrame = Frame(janDep, width=9999, height=665,bg="white", relief="raise")
DepbottomFrame.pack(side=BOTTOM,fill = 'both', expand = True)
LogoLabel = Label(DeptopFrame, image=logo, bg="#ff7f27")
LogoLabel.place(x=1205, y=0)
LogoLabel = Label(DeptopFrame, image=logo3, bg="#ff7f27")
LogoLabel.place(x=0, y=0)
EmpresaLabel = Label(DeptopFrame, text="Empresa: Ezipa", font=("Calibri",8), bg="#ff7f27", fg="White")
EmpresaLabel.place(x= 630 ,y=35)   
Datalabel = Label(DeptopFrame, text= "Data:" f"{datetime.now(): %d/%m/%y}", bg="#ff7f27", fg="White")
Datalabel.place(x= 630 ,y=60)  
PassLabel = Label(DepbottomFrame, text="Senha:", font=("Calibri",25), bg="white", fg="black")
PassLabel.place(x= 465,y=250)
PassEntry = ttk.Entry(DepbottomFrame, width=25, show="*")
PassEntry.bind("<KeyPress>", lambda e: Entrar() if e.char == '\r' else None)
PassEntry.configure(font=('Arial', 16))
PassEntry.place(x=565, y=255)
#ModuloLabel = Label(DeptopFrame, text="Módulo: Departamento Pessoal", font=("Calibri",8), bg="#ff7f27", fg="White")
#ModuloLabel.place(x= 595 ,y=10)    
#MenuLabel = Label(DeptopFrame, text="Cadastro de horas Extras", font=("Calibri",10), bg="#ff7f27", fg="White")
#MenuLabel.place(x= 600 ,y=90)    



def Entrar():
    senha = PassEntry.get()
    data_Entrada = datetime.today().date()
    hora_atual = datetime.now().time()
    loginService = LoginService()
    usuarioLogado = loginService.realizarLoginComSenha(senha)
    horaExtraService = HoraExtraService()

    if usuarioLogado is None:
        messagebox.showerror('Erro', 'Credenciais de login e senha inválidas.')
        return
    if not hasattr(usuarioLogado, 'getusuarioid'):
        messagebox.showerror('Erro', 'Credenciais de login e senha inválidas.')
        return
    horaExtraService.criartempodeTolerancia()
    isEntradaOuSaida = horaExtraService.isEntradaOuSaida(usuarioLogado.getusuarioid())

    atualizarfuncionario = horaExtraService.obtervalordetempodetolerancia(usuarioLogado.getusuarioid(), usuarioLogado.getNome(), data_Entrada)
    autorizado = horaExtraService.obtervalordeautorizado(usuarioLogado.getNome(), data_Entrada)

    if autorizado != 'S':
        messagebox.showerror('Erro', 'Login não autorizado, favor procurar o responsável')
        print(autorizado)
        return


    if isEntradaOuSaida == "ENTRADA":
        idUsuario = usuarioLogado.getusuarioid()
        horaExtraService.InserirHoraExtra(hora_atual, data_Entrada, idUsuario, usuarioLogado.getNome())
        messagebox.showinfo('Entrada', f'{usuarioLogado.getNome()}, Registro 1 efetuado com sucesso') #Entrada hora extra às {datetime.now():%d/%m/%y %H:%M}')
        horaExtraService.atualizardados()        
    elif isEntradaOuSaida == "SAIDA":
        horaextra= horaExtraService.isSaida(usuarioLogado.getusuarioid())
        idUsuario = usuarioLogado.getusuarioid()
        if horaextra == None:
            horaExtraService.alterarHoraExtra(hora_atual, data_Entrada, idUsuario)
            messagebox.showinfo('Saida', f'{usuarioLogado.getNome()}, Registro 2 efetuado com sucesso')# Saida hora extra às {datetime.now():%d/%m/%y %H:%M}')
            horaExtraService.atualizardados()
        else:
            messagebox.showerror("Erro", "Esse registro já existe, favor procurar o R.H",icon="error") 
                
    else:
        messagebox.showerror('Erro', 'Não foi possível determinar se é hora de entrada ou saída.')
    PassEntry.delete(0, 'end')     
            
LoginButton = ttk.Button(DepbottomFrame, text="Entrar", width=18, command=Entrar)
LoginButton.bind("<KeyPress>", lambda e: Entrar() if e.char == '\r' else None) 
LoginButton.place(x=580,y=320)   

def Sair():
    janDep.destroy()
    return
    
ExitButton = ttk.Button(DepbottomFrame, text="Sair", width=18, command=Sair)
ExitButton.place(x=710,y=320)

janDep.mainloop()      