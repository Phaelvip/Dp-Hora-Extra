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
horaExtraService = HoraExtraService()
def verificar_autorizacao():
    autorizado = False  # Supondo que não esteja autorizado
    if autorizado:
        return True
    else:
        messagebox.showerror('Erro', 'Login não autorizado, favor procurar o responsável')
        return False

def verificar_tolerancia():
    # Verificar a tolerância de tempo
    hora_atual = datetime.now().time()
    tolerancia = horaExtraService.SelecionartempodeTolerancia()
    horario_atualizado = datetime.now() + tolerancia

    # Comparar com a hora atual do Windows
    if hora_atual < horario_atualizado.time():
        messagebox.showinfo('Aviso', 'Aguarde a liberação para entrar.')
        return False
    else:
        return True

def verificar_horario_trabalho():
    # Verificar se é horário de trabalho
    hora_atual = datetime.now().time()
    horario_entrada = datetime.strptime('08:00', '%H:%M').time()
    horario_saida = datetime.strptime('17:00', '%H:%M').time()

    if hora_atual < horario_entrada:
        messagebox.showinfo('Entrada', 'Registro de entrada efetuado com sucesso.')
    elif hora_atual > horario_saida:
        messagebox.showinfo('Saída', 'Registro de saída efetuado com sucesso.')
    else:
        messagebox.showinfo('Aviso', 'Fora do horário de trabalho.')

def Entrar():
    senha = PassEntry.get()
    data_Entrada = datetime.today().date()
    hora_atual = datetime.now().time()
    loginService = LoginService()
    usuarioLogado = loginService.realizarLoginComSenha(senha)


    if usuarioLogado is None or not hasattr(usuarioLogado, 'getusuarioid'):
        messagebox.showerror('Erro', 'Credenciais de login e senha inválidas.')
        return
    criartabela=horaExtraService.criartempodeTolerancia(usuarioLogado.getusuarioid(), usuarioLogado.getNome(), data_Entrada)    
    atualizarfuncionario = horaExtraService.obtervalordetempodetolerancia()
    autorizado = horaExtraService.obtervalordeautorizado(usuarioLogado.getNome(), data_Entrada)
    
    if not verificar_autorizacao():
        return

    if not verificar_tolerancia():
        return

    isEntradaOuSaida = horaExtraService.isEntradaOuSaida(usuarioLogado.getusuarioid())

    if isEntradaOuSaida == "ENTRADA":
        idUsuario = usuarioLogado.getusuarioid()
        horaExtraService.InserirHoraExtra(hora_atual, data_Entrada, idUsuario, usuarioLogado.getNome())
        verificar_horario_trabalho()
        horaExtraService.atualizardados()
    elif isEntradaOuSaida == "SAIDA":
        horaextra = horaExtraService.isSaida(usuarioLogado.getusuarioid())
        idUsuario = usuarioLogado.getusuarioid()
        if horaextra is None:
            horaExtraService.alterarHoraExtra(hora_atual, data_Entrada, idUsuario)
            verificar_horario_trabalho()
            horaExtraService.atualizardados()
        else:
            messagebox.showerror("Erro", "Esse registro já existe, favor procurar o R.H", icon="error") 


LoginButton = ttk.Button(DepbottomFrame, text="Entrar", width=18, command=Entrar)
LoginButton.bind("<KeyPress>", lambda e: Entrar() if e.char == '\r' else None) 
LoginButton.place(x=580,y=320)   

def Sair():
    janDep.destroy()
    return
    
ExitButton = ttk.Button(DepbottomFrame, text="Sair", width=18, command=Sair)
ExitButton.place(x=710,y=320)

janDep.mainloop()      