from persistence.DbConnecion import DbConnection
from entity.Usuariopc import Usuario
from mysql.connector import Error
from entity.PermissaoDepartamentoPessoal import PermDeptPEssoal

class LoginRepository:
    #Construtor... Não esquece carai
    def __init__(self):
        pass
    
    def EntrarComLogin(self, nome, senha):
        #con = mysql.connector.connect(host='127.0.0.1', user='root', database='ezsys',password='q9w8e7#MTB')
        db = DbConnection()
        usuario = None
        try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (nome, senha)
            cursor.execute('SELECT usuario, senha, usuarioid FROM ezsys.usuarios WHERE usuario = %s AND senha = %s', valores)
            #cursor.execute('SELECT nome, senha FROM ez-sys.senha WHERE nome = %s AND senha = %s', valores)
            ver = cursor.fetchone()
            if(ver != None):
                usuario = Usuario(ver['usuarioid'],ver['usuario'], ver['senha'], None)
            db.closeConn(cursor)    
            return usuario
        except Error as e :
            print(e)
            return usuario
   
        

        
   
    def permDeptPessoal(self,usuarioid): 
       db = DbConnection()
        
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (usuarioid)
            usuario='select * from ezsys.perm_deptpessoal where fk_usuarioid = "{}"'.format(valores)
            cursor.execute(usuario)
            ver = cursor.fetchone()

            if(ver != None):
             permissao =  PermDeptPEssoal(ver["dept_id"], ver["perm_autorizarhoraextra"])
 
            db.closeConn(cursor)    
            return permissao
       except Error as e :
            print(e)
            return None
        
        
        
    def EntrarComSenha(self, senha):
        #con = mysql.connector.connect(host='127.0.0.1', user='root', database='ezsys',password='q9w8e7#MTB')
        db = DbConnection()
        usuario = None
        try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (senha,)
            cursor.execute('SELECT usuarioid, usuario, senha, nome FROM ezsys.usuarios WHERE senha = %s', valores)
            #cursor.execute('SELECT nome, senha FROM ez-sys.senha WHERE nome = %s AND senha = %s', valores)
            ver = cursor.fetchone()
            if(ver != None):
                usuario = Usuario(ver['usuarioid'], ver['senha'],ver['nome'],ver['usuario'], None)

            db.closeConn(cursor)    
            return usuario
        except Error as e :
            print(e)
            return usuario        
    pass