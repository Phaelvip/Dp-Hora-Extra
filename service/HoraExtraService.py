from persistence.HoraExtraRepository import HoraExtraRepository
from datetime import *
from  datetime import datetime
from mysql.connector import Error
import  locale   
  
class HoraExtraService:
    def __init__(self):
        self.__HoraExtraDao = HoraExtraRepository()    
        locale.setlocale(locale.LC_ALL,'pt_BR')
        locale.setlocale(locale.LC_MONETARY,'pt_BR.UTF-8')  
    
    def InserirHoraExtra(self, hora_atual, data_Entrada, idUsuario, usuarioLogado):
        self.__HoraExtraDao.inserirEntrada(hora_atual, data_Entrada, idUsuario, usuarioLogado)
   
    def alterarHoraExtra(self, hora_atual,data,  idUsuario ):
         self.__HoraExtraDao.atualizarSaida(hora_atual, data,  idUsuario)

    

        
    def isEntradaOuSaida(self, senha):
        #Ele vai me retornar uma informação ou um objeto inteiro
        retorno = self.__HoraExtraDao.obterValorEntrada(senha)
        if retorno ==None:
            return "ENTRADA"
        else:
            return "SAIDA"
        
        
    def isSaida(self, idUsuario):
        retorno = self.__HoraExtraDao.obterValorSaida(idUsuario)
        return retorno
    
    def obtervalordehoradetrabalho(self, idUsuario):
        retorno = self.__HoraExtraDao.obtervalordehoradetrabalho(idUsuario)
        return retorno
    
    def obtervalordetempodetolerancia(self):
        retorno = self.__HoraExtraDao.obtervalordetempodetolerancia()
        return retorno
    
    def obtervalordeautorizado(self, nome,data):
        retorno = self.__HoraExtraDao.obtervalordeautorizado(nome,data)
        return retorno       
    
    def criartempodeTolerancia(self,nome,senha,data):
        retorno = self.__HoraExtraDao.criartempodeTolerancia(nome,senha,data)
        return retorno            
    
    def atualizardados(self):
        retorno = self.__HoraExtraDao.atualizardados()
        return retorno    
    def SelecionartempodeTolerancia(self):
        retorno = self.__HoraExtraDao.SelecionartempodeTolerancia()
        return retorno        
        