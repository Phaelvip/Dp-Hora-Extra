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
             permissao =  PermDeptPEssoal(ver["dept_id"], ver["perm_caddept"], ver["perm_caddept_funcionarios"], ver["perm_caddept_cargos"],
                                        ver["perm_caddept_funcoes"], ver["perm_caddept_transportes"], ver["perm_caddept_acidentes"], ver["perm_caddept_ocorrencias"],
                                        ver["perm_caddept_feriados"], ver["perm_funcionarios_incluir"], ver["perm_funcionarios_editar"],
                                        ver["perm_funcionarios_excluir"], ver["perm_cargps_incluir"], ver["perm_cargps_editar"],
                                        ver["perm_cargos_excluir"], ver["perm_funcoes_incluir"], ver["perm_funcoes_editar"], ver["perm_funcoes_excluir"], 
                                        ver["perm_transportes_incluir"], ver["perm_transportes_editar"], ver["perm_transportes_excluir"], ver["perm_acidentes_incluir"],
                                        ver["perm_acidentes_editar"], ver["perm_acidentes_excluir"], ver["perm_ocorrencias_incluir"],
                                        ver["perm_ocorrencias_editar"], ver["perm_ocorrencias_excluir"], ver["perm_feriados_incluir"], ver["perm_feriados_editar"], ver["perm_feriados_excluir"],
                                        ver["perm_folhadeponto"], ver["perm_hr_extra"], ver["perm_relatorios"],
                                        ver["perm_rel_cons_hextra"], ver["perm_rel_bhora"],
                                        ver["perm_rel_cfrequencia"], ver["perm_rel_fpagamento"],ver["perm_relogio_ponto"])
 
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
            cursor.execute('SELECT usuarioid, usuario, senha FROM ezsys.usuarios WHERE senha = %s', valores)
            #cursor.execute('SELECT nome, senha FROM ez-sys.senha WHERE nome = %s AND senha = %s', valores)
            ver = cursor.fetchone()
            if(ver != None):
                usuario = Usuario(ver['usuarioid'],ver['usuario'], ver['senha'], None)

            db.closeConn(cursor)    
            return usuario
        except Error as e :
            print(e)
            return usuario        
    pass