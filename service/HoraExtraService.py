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
         
    def InserirSaida(self, hora_atual, data_Saida, idUsuario, usuarioLogado ):
         self.__HoraExtraDao.inserirSaida(hora_atual, data_Saida, idUsuario, usuarioLogado)         

    

        
    def isEntradaOuSaida(self, senha):
        #Ele vai me retornar uma informação ou um objeto inteiro
        retorno = self.__HoraExtraDao.obterValorEntrada(senha)
        if retorno ==None:
            return "ENTRADA"
        else:
            return "SAIDA"
    
    def obtervalorentradaousaida(self, idUsuario):
        valor_entrada = self.__HoraExtraDao.obtervalorentradaousaida(idUsuario)
        
        if valor_entrada == 'E':
            if valor_entrada == 'S':
                return 'SAIDA'
            else:
                return 'ENTRADA'
        elif valor_entrada == 'S':
            return 'SAIDA'
        else:
            return None     
        
    def obtervalorentradaousaida321312(self, usuario_id, data):
        valor_entrada = self.__HoraExtraDao.existeRegistroDeEntrada(usuario_id, data)
        valor_saida = self.__HoraExtraDao.existeRegistroDeSaida(usuario_id, data)
        
        if valor_entrada == 'E':
            if valor_saida == 'S':
                return 'SAIDA'
            else:
                return 'ENTRADA'
        elif valor_entrada == 'S':
            return 'SAIDA'
        else:
            return None                
        
    def isSaida(self, idUsuario):
        retorno = self.__HoraExtraDao.obterValorSaida(idUsuario)
        return retorno
    
    def existeRegistroDeEntrada(self, usuario_id, data):
        retorno = self.__HoraExtraDao.existeRegistroDeEntrada(usuario_id, data)
        return retorno
    
    
    def existeRegistroDeSaida(self, usuario_id, data):
        retorno = self.__HoraExtraDao.existeRegistroDeSaida(usuario_id, data)
        return retorno        
    
    
    def obtervalordehoradetrabalho(self, idUsuario):
        retorno = self.__HoraExtraDao.obtervalordehoradetrabalho(idUsuario)
        return retorno
    
    def obtervalordetempodetolerancia(self):
        retorno = self.__HoraExtraDao.obtervalordetempodetolerancia()
        return retorno
    

    
    def obtervalordeautorizado(self):
        retorno = self.__HoraExtraDao.obtervalordeautorizado()
        return retorno    
    
    def Selecionarmensagem3(self,nome):
        retorno = self.__HoraExtraDao.Selecionarmensagem3(nome)
        return retorno           
    
    def Selecionarmensagem2(self,nome):
        retorno = self.__HoraExtraDao.Selecionarmensagem2(nome)
        return retorno        
    
    def Selecionarmensagem1(self,nome):
        retorno = self.__HoraExtraDao.Selecionarmensagem1(nome)
        return retorno     
    
    def obtervalordata(self):
        retorno = self.__HoraExtraDao.obtervalordata()
        return retorno         
    
    def obtervalorautorizacao(self):
        retorno = self.__HoraExtraDao.obtervalorautorizacao()
        return retorno          
      
    def obtervalorHora1(self):
        retorno = self.__HoraExtraDao.obtervalorHora1()
        return retorno    
    
    def obtervalorHora2(self):
        retorno = self.__HoraExtraDao.obtervalorHora2()
        return retorno        
    
    def obtervalorHora3(self):
        retorno = self.__HoraExtraDao.obtervalorHora3()
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
        