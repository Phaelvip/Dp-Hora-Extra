from configparser import ConfigParser
from datetime import  datetime


class Leitura:

    def __init__(self):
        config = ConfigParser()
        config.read('Leitura.ini')

        self.title = config.get('DEFAULT', 'title')
        #print('title', type(title), title)

        self.username = config.get('DATABASE', 'user') #Como funciona, config.get([TITULO] , ATRIBUTO)
        self.password = config.get('DATABASE','pass')
        self.dbname = config.get('DATABASE', 'dbname')
        self.host = config.get('DATABASE', 'host')
        self.port = config.getint('DATABASE', 'port')
        #keep_alive = config.getboolean('DATABASE', 'keep_alive')
        self.timeout = config.getint('DATABASE', 'timeout', fallback=60)
        
        self.excel= config.get('URL', 'caminhoExcel') 
        self.excel2= config.get('URL','caminhoExcel2') 
        #print('user', type(username), username)
        #print('port', type(port), port)
        #print('keep_alive', type(keep_alive), keep_alive)

        #print('timeout', type(timeout), timeout) 
        self.PDF= config.get('URL', 'caminhoPDF') 
        self.PDF2= config.get('URL', 'caminhoPDF2') 
  
  

    
    def __excel__(self, excel):
        self.__excel= excel
        
    def getExcel(self):
       return self.__excel
    
    def setExcel(self, excel):
        self.__excel = excel


    pass
        
        


#from configparser import ConfigParser
#config = ConfigParser()
#config.read('config.ini')

#title = config.get('DEFAULT', 'title')
#print('title', type(title), title)

#username = config.get('database', 'user')
#port = config.getint('database', 'port')
#keep_alive = config.getboolean('database', 'keep-alive')
#timeout = config.getint('database', 'timeout', fallback=60)

#print('user', type(username), username)
#print('port', type(port), port)
#print('keep_alive', type(keep_alive), keep_alive)

#print('timeout', type(timeout), timeout) 