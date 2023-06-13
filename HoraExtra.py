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
import calendar
import csv
import pipes
from entity.Usuariopc import Usuario
import threading
import time
import pdfkit
import win32print
import win32com.client
import win32api
import tempfile
import requests
from UI import limpaWidget
import subprocess
import os
from  Leitura import Leitura
from PIL import Image, ImageTk
from tkinter.filedialog import asksaveasfile, asksaveasfilename,askopenfile,askopenfilename
import io
import locale
import pytesseract
import json
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
Datalabel = Label(DeptopFrame, text= "Data:" f"{datetime.now(): %d/%m/%Y}", bg="#ff7f27", fg="White")
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
horaExtraService = HoraExtraService()


def Entrar():
    senha = PassEntry.get()
    data_Entrada = datetime.today().date()
    hora_atual = datetime.now().time()
    loginService = LoginService()
    usuarioLogado = loginService.realizarLoginComSenha(senha)

    if usuarioLogado is None or not hasattr(usuarioLogado, 'getusuarioid'):
        messagebox.showerror('Erro', 'Credenciais de login e senha inválidas.')
        return

    horaExtraService.criartempodeTolerancia(usuarioLogado.getusuarioid(), usuarioLogado.getNome(), data_Entrada)    
    horaExtraService.obtervalordetempodetolerancia()
    autorizado = str(horaExtraService.obtervalordeautorizado())
    Hora1 = horaExtraService.obtervalorHora1()
    data1 = horaExtraService.obtervalordata()
    data_formatada = data1.strftime("%d/%m/%Y")
    autorizacao = horaExtraService.obtervalorautorizacao()
    Hora1 = horaExtraService.obtervalorHora1()      
    Hora2 = horaExtraService.obtervalorHora2()   
    Hora3 = horaExtraService.obtervalorHora3()

        # Verificar se o usuário está autorizado a registrar entrada ou saída
    if autorizado == autorizacao:
        entrada_ou_saida = horaExtraService.obtervalorentradaousaida321312(usuarioLogado.getusuarioid())

        if entrada_ou_saida == 'ENTRADA':
            if horaExtraService.existeRegistroDeEntrada(usuarioLogado.getusuarioid(), data_Entrada):
                messagebox.showerror('Erro', 'Já existe um registro de entrada para a data atual.')
                return
            else:
                idUsuario = usuarioLogado.getusuarioid()
                horaExtraService.InserirHoraExtra(hora_atual, data_Entrada, idUsuario, usuarioLogado.getNome())
                messagebox.showinfo('Entrada', f'{usuarioLogado.getNome()}, Registro efetuado com sucesso')
                horaExtraService.atualizardados()
                PassEntry.delete(0, 'end')

        elif entrada_ou_saida == 'SAIDA':
            if horaExtraService.existeRegistroDeSaida(usuarioLogado.getusuarioid(), data_Entrada):
                idUsuario = usuarioLogado.getusuarioid()
                horaExtraService.alterarHoraExtra(hora_atual, data_Entrada, idUsuario)
                messagebox.showinfo('Atualização de Saída', f'{usuarioLogado.getNome()}, Registro de saída atualizado com sucesso')
                horaExtraService.atualizardados()
                PassEntry.delete(0, 'end')

            elif horaExtraService.existeRegistroDeEntrada(usuarioLogado.getusuarioid(), data_Entrada):
                idUsuario = usuarioLogado.getusuarioid()
                horaExtraService.InserirSaida(hora_atual, data_Entrada, idUsuario, usuarioLogado.getNome())
                messagebox.showinfo('Saída', f'{usuarioLogado.getNome()}, Registro efetuado com sucesso')
                horaExtraService.atualizardados()
                PassEntry.delete(0, 'end')

            else:
                messagebox.showerror('Erro', 'Já existe um registro de saída para a data atual.')
                PassEntry.delete(0, 'end')
    else:
        mensagem2 = horaExtraService.Selecionarmensagem2(usuarioLogado.getNome())
        mensagem3 = horaExtraService.Selecionarmensagem3(usuarioLogado.getNome())

        if mensagem2 != autorizacao:
            messagebox.showinfo("NÃO AUTORIZADO", f"EXISTE SOLICITAÇÃO NÃO AUTORIZADA PARA ESTE USUÁRIO NESTA DATA: {data_formatada}", icon='error')
            PassEntry.delete(0, 'end')

        elif mensagem3:
            messagebox.showinfo("NÃO AUTORIZADO", f"EXISTE SOLICITAÇÃO AUTORIZADA PARA ÀS: {Hora1}, PODENDO ENTRAR ENTRE {Hora2} E {Hora3}", icon='error')
            PassEntry.delete(0, 'end')
            
        else:
            messagebox.showinfo("NÃO AUTORIZADO", 'NÃO EXISTE SOLICITAÇÃO PARA ESTE USUÁRIO NESTA DATA', icon='error')
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
       
       
