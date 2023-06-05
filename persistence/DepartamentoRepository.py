import mysql.connector
from mysql.connector import Error
from persistence.DbConnecion import DbConnection
from  entity.Usuario import Usuario
import datetime



class DepartamentoRepository:
    
    def consultarFuncionarios(self):
     db = DbConnection()
     user = None
     try:
        con = db.getConn()     
        cursor= con.cursor()
        valores = ()
        cursor.execute("SELECT `id`, `nome`,`celular`,`email`,`ENDER_TIPOLOGR`,`endereco`,`ENDER_NUMERO`,`bairro`,`cidade`,`estado`,`cep`,`ramo`,`funcao`,`ramalinterno`,id FROM `ezsys`.dp_funcionarios ORDER BY `nome` ASC")      
        ver = cursor.fetchall() 
        db.closeConn(cursor)    
        return ver
     except Error as e :
            print(e)
            return user


    def selecionarUsuarioPorNome(self, nome):
      db = DbConnection()
      try:
          con = db.getConn()     
          cursor = con.cursor()
          query = "SELECT `id`, `nome`,`celular`,`email`,`ENDER_TIPOLOGR`,`endereco`,`ENDER_NUMERO`,`bairro`,`cidade`,`estado`,`cep`,`ramo`,`funcao`,`ramalinterno`,id FROM `ezsys`.dp_funcionarios WHERE LOWER(`nome`) LIKE LOWER(%s) ORDER BY `nome` ASC"
          cursor.execute(query, ('%'+nome+'%',))
          resultados = cursor.fetchall()
          return [list(r) for r in resultados]
      except Error as e:
        print(e)
        return None


    def selecionarNaTabelaFuncionarios(self,id):
     db = DbConnection()
     user = None
     try:
        con = db.getConn()     
        cursor= con.cursor(dictionary=True)
        valores = (id)
        # con = mysql.connector.connect(host='127.0.0.1', user='root', database='eztestes',password='q9w8e7#MTB')
        select="SELECT * FROM `ezsys`.dp_funcionarios WHERE `id` = {};".format(valores)
        #data,solicitacao_assunto,solicitacao_texto,solicitacao_status,solicitacao_incluido,solicitacao_editado   
        cursor.execute(select)
        ver = cursor.fetchone()                       
        db.closeConn(cursor)    
        return ver
     except Error as e :
            print(e)
            return user 
         
    def DeletarFuncionarios(self,usuario):   
     db = DbConnection()
     try:
        con = db.getConn()     
        cursor= con.cursor(dictionary = True)
        valores = (usuario)
        sql = "DELETE FROM `ezsys`.dp_funcionarios WHERE id = {};".format(valores)
        cursor.execute(sql)
        con.commit()
        db.closeConn(cursor)  
        print(cursor.rowcount, "registro excluído")  
        return True
     except Error as e :
          print(e)
          return False            

    def inserirFuncionarios(self,nome,codigo,nomecompleto,telefone2,celular,email,nacionalidade,nasc,ENDER_TIPOLOGR,endereco,ENDER_NUMERO,ENDER_COMPLEM,bairro,cidade,estado,cep,pais,cgccpf,insc,escolaridade,estcivil,ramo,funcao,codsetor,carttrab,certreserv,tipofuncio,titeleitor,nomepai,nomemae,ativo,numpis,obs1,obs2,ramalinterno,usuario_sistema):         
        db = DbConnection()
        
        
        try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (nome,codigo,nomecompleto,telefone2,celular,email,nacionalidade,nasc,ENDER_TIPOLOGR,endereco,ENDER_NUMERO,ENDER_COMPLEM,bairro,cidade,estado,cep,pais,cgccpf,insc,escolaridade,estcivil,ramo,funcao,codsetor,carttrab,certreserv,tipofuncio,titeleitor,nomepai,nomemae,ativo,numpis,obs1,obs2,ramalinterno,usuario_sistema)
            #cursor.execute('SELECT nome, senha FROM ` `ezsys``.senha WHERE nome = %s AND senha = %s', valores)
            #cursor.execute('truncate table `ezsys`.woodpaper')
            cursor.execute("INSERT INTO ezsys.dp_funcionarios (nome,codigo,nomecompleto,telefone2,celular,email,nacionalidade,nasc,ENDER_TIPOLOGR,endereco,ENDER_NUMERO,ENDER_COMPLEM,bairro,cidade,estado,cep,pais,cgccpf,insc,escolaridade,estcivil,ramo,funcao,codsetor,carttrab,certreserv,tipofuncio,ativo,titeleitor,nomepai,nomemae,numpis,obs1,obs2,ramalinterno,usuario_sistema) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",valores)
            print(valores)
            con.commit()
            db.closeConn(cursor)    
            return True #Meu LastID
        except Error as e :
            print(e)
            return False           
       
       
    def selecionarFuncionarioUsuario(self): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = ()
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT usuario FROM ezsys.usuarios;" )
            cursor.execute(select)  
            ver = cursor.fetchall()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario         
       
       
     

    def consultarFuncionariosEmSalarios(self,id):
     db = DbConnection()
     user = None
     try:
        con = db.getConn()     
        cursor= con.cursor()
        valores = (id)
        cursor.execute('SELECT `nome`  FROM ezsys.dp_funcionarios WHERE `id` = {};'.format(valores))      
        ver = cursor.fetchall() 
        db.closeConn(cursor)    
        return ver
     except Error as e :
            print(e)
            return user


    def EditarFuncionarios(self,  nome,codigo,nomecompleto,telefone2,celular,email,nacionalidade,tipo,endereço,numero,complemento,bairro,cidade,estado,cep,pais,cpf,identidade,escolaridade,estadocivil,cargo,funcao,setor,carteiradetrabalho,carteiradereservista,setoradio,titeleitor,nomepai,nomemae,statusradio,obs1,obs2,ramal,usuarioSistema,id):
        db = DbConnection()
        try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = ( nome,codigo,nomecompleto,telefone2,celular,email,nacionalidade,tipo,endereço,numero,complemento,bairro,cidade,estado,cep,pais,cpf,identidade,escolaridade,estadocivil,cargo,funcao,setor,carteiradetrabalho,carteiradereservista,setoradio,titeleitor,nomepai,nomemae,statusradio,obs1,obs2,ramal,usuarioSistema,id)
            #cursor.execute('SELECT nome, senha FROM ` `ezsys``.senha WHERE nome = %s AND senha = %s', valores)
            #cursor.execute('truncate table `ezsys`.woodpaper')
            updateString =cursor.execute("UPDATE `ezsys`.dp_funcionarios SET `nome`= %s,`codigo`= %s,`nomecompleto`= %s,`telefone2`= %s,`celular`= %s,`email`= %s,`nacionalidade`= %s,`ENDER_TIPOLOGR`= %s,`endereco`= %s,`ENDER_NUMERO`= %s,`ENDER_COMPLEM`= %s ,`bairro`= %s,`cidade`= %s,`estado`= %s,`cep`= %s,`pais`= %s,`cgccpf`= %s,`insc`= %s,`escolaridade`= %s,`estcivil`= %s,`ramo`= %s,`funcao`= %s,`codsetor`= %s,`carttrab`= %s,`certreserv`= %s,`tipofuncio`= %s,`titeleitor`= %s,`nomepai`= %s,`nomemae`= %s,`ativo`=%s, `obs1`= %s, `obs2`= %s, `ramalinterno`= %s,`usuario_sistema`=%s WHERE  `Id` = %s;", valores)
            cursor.execute(updateString)      
            con.commit()
            db.closeConn(cursor)    
            
        except Error as e :
               print(e)
               return      

    def selecionarFuncionarioNome(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `nome` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario  
        

    def selecionarFuncionarioCodigo(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `codigo` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario 

    def selecionarFuncionarioNomeCompleto(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `nomecompleto` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario 

    def selecionarFuncionarioTelefone(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `telefone2` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario 

    def selecionarFuncionarioCelular(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `celular` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario 

    def selecionarFuncionarioEmail(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `email` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario 

    def selecionarFuncionarioNacionalidade(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `nacionalidade` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario 

    def selecionarFuncionarioNascimento(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `nasc` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario 

    def selecionarFuncionarioLogradouro(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `ENDER_TIPOLOGR` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario 

    def selecionarFuncionarioEndereco(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `endereco` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario 

    def selecionarFuncionarioNumero(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `ENDER_NUMERO` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario 

    def selecionarFuncionarioComplemento(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `ENDER_COMPLEM` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario 

    def selecionarFuncionarioBairro(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `bairro` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario 

    def selecionarFuncionarioCidade(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `cidade` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario 
       
    def selecionarFuncionarioEstado(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `estado` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario 
       
    def selecionarFuncionarioCep(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `cep` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario        
       
    def selecionarFuncionarioPais(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `pais` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario              

    def selecionarFuncionarioCPF(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `cgccpf` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario    

    def selecionarFuncionarioIdentidade(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `insc` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario    

    def selecionarFuncionarioEscolaridade(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `escolaridade` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario    

    def selecionarFuncionarioEstadoCivil(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `estcivil` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario    

    def selecionarFuncionarioRamo(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `ramo` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario   

    def selecionarFuncionarioFuncao(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `funcao` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario   

    def selecionarFuncionariocodsetor(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `codsetor` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario   
       
    def selecionarFuncionarioCarteiraDeTrabalho(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `carttrab` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario          
       
    def selecionarFuncionarioCarteiraDeReservista(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `certreserv` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario           
       
    def selecionarFuncionarioTipoFuncionario(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `tipofuncio` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchall()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario            
       
    def selecionarFuncionarioStatus(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `ativo` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchall()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario          

    def selecionarFuncionarioTituloDeEleitor(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `titeleitor` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario       

    def selecionarFuncionarioNomeDoPai(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `nomepai` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario     

    def selecionarFuncionarioNomeDoMae(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `nomemae` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario  
       
    def selecionarFuncionarioPis(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `numpis` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario     
       
       
    def ConsultarFuncionarioPis(self,pis): 
      db = DbConnection()
      try:
          con = db.getConn()
          cursor = con.cursor(dictionary=True)
          valores = (pis,)
          select = "SELECT `numpis` FROM ezsys.dp_funcionarios WHERE `numpis` = %s"
          cursor.execute(select, valores)
          ver = cursor.fetchall()
          db.closeConn(cursor)
          return ver
      except Error as e:
          print(e)
          return None      
       
            

    def selecionarFuncionarioObservacao1(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `obs1` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario     

    def selecionarFuncionarioObservacao2(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `obs2` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario  

    def selecionarFuncionarioRamalInterno(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `ramalinterno` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario  

    def selecionarFuncionarioUsuarioporID(self, texto):
     db = DbConnection()
     try:
          con = db.getConn()
          cursor = con.cursor(dictionary=True)
          valores = (texto,)
          select = "SELECT `usuario_sistema` FROM ezsys.dp_funcionarios WHERE `id` = %s;"
          cursor.execute(select, valores)
          resultado = cursor.fetchone()
          if resultado is None:
               return None
          else:
               return resultado['usuario_sistema']
     except Error as e:
          print(e)
     finally:
          db.closeConn(cursor)





#____________________________________________________Registro de Salarios___________________________________________________________________________________________
    def selecionarFuncionarioSalarioBase(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `salbase` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario  
       
       
    def selecionarFuncionarioSalarioFuncao(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `salfuncao` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario  

    def selecionarFuncionarioSalarioLiquido(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `salliquido` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario  
       
    def selecionarSalarioDivideBH(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_dividebh` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchall()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario          

 
    def selecionarFuncionarioInss(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `percinss` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario   

    def selecionarFuncionarioDecTerceiro(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_12decterc` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario  
 

    def selecionarFuncionarioComissaoPremio(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_comiprem` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario   
    
   
    def selecionarFuncionarioRecebeComissao(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_recebeprem` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchall()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario 


    def selecionarFuncionarioFerias(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_12ferias` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario   


    def selecionarFuncionarioInsalubridade(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_insalubr` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario   

    def selecionarFuncionarioFgts(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `percfgts` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario 
       
    def selecionarFuncionarioValeTranspDiario(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `valetrp` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario        
       
    def selecionarFuncionarioMaxValeTransp(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `percmaxvaletrp` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario              
       
    def selecionarFuncionarioSalSeguro(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_seguro` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario       
       
    def selecionarFuncionarioSalCesta(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_cesta` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario                   
       
    def selecionarFuncionarioSalGremio(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_gremio` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario                   
              
    def selecionarFuncionarioPensaoAlimenticia(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_pensaoalim` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario      
       
    def selecionarFuncionarioValeAlimentacao(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_valealiment` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario             
       
    def selecionarFuncionarioAssMedica(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_assmedica` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario             
       
    def selecionarFuncionarioHora50porc(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_hrextra50` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario             
       
    def selecionarFuncionarioHora100porc(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_hrextra100` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario            
       
    def selecionarFuncionarioHora100porc(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_hrextra100` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario       
       
    def selecionarFuncionarioSalFamilia(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_familia` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario             
       
    def selecionarFuncionarioFGTSDecimoTerceiro(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_fgts12decterc` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario                           
   
    def selecionarFuncionarioFGTSFerias(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_fgts12ferias` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario       
       
    def selecionarFuncionarioCafe(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_cafe` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario                                    
       
    def selecionarFuncionarioUniforme(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_uniforme` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario                                 
            
    def selecionarFuncionarioRepouso(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_repsemremun` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario      
       
    def selecionarFuncionarioParticipacaoLucros(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_partlucr` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario         

    def selecionarFuncionarioHorarioEntradaDiasUteis(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `hrdiautil1` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario    

    def selecionarFuncionarioHorarioSaidaDiasUteis(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `hrdiautil2` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario    

    def selecionarFuncionarioIntervaloSaida(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `hrintervalo1` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario    
             
    def selecionarFuncionarioIntervaloEntrada(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `hrintervalo2` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario         

    def selecionarFuncionarioTotalSalario(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_totsal` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario    

    def selecionarFuncionarioTotalBeneficios(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_totbenef` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario  

    def selecionarFuncionarioTotalCustoMes(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_customes` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario  

    def selecionarFuncionarioTotalCustoDiario(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_custodia` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario  

    def selecionarFuncionarioTotalCustoHora(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_custohr` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario  
 
    def EditarSalarioFuncionarios(self,salarioBase,inssFuncionario,salFuncaoFuncionario,salLiquidoFuncionario,decTerceiroFuncionario,comissaoFuncionario,feriarFuncionario,premiacaoFUncionario,Salinsalubridade,fgtsFuncionario,valTranspFuncionario,maxValeTranspFuncionario,seguroFuncionario,cestaFuncionario
                                                                 ,gremioFuncionario,pensaoAlimFuncionario,partLucrosFuncionario,horasExt50Funcionario,horasExt100Funcionario,salFamilFuncionario,fgtsParcFuncionario,fgtsFeriasFUncionario,cafeFuncionario,uniformeFuncionario,repousoFuncionario,diasUteisEntrada,diasUteisSaida,
                                                                 intervaloEntrada,intervaloSaida,totSalario,totBeneficio,custMensal,custDiario,custHora,valeAlimentacao,assMedica,dividebh,id):
        db = DbConnection()
        try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (salarioBase,inssFuncionario,salFuncaoFuncionario,salLiquidoFuncionario,decTerceiroFuncionario,comissaoFuncionario,feriarFuncionario,premiacaoFUncionario,Salinsalubridade,fgtsFuncionario,valTranspFuncionario,maxValeTranspFuncionario,seguroFuncionario,cestaFuncionario
                                                                 ,gremioFuncionario,pensaoAlimFuncionario,partLucrosFuncionario,horasExt50Funcionario,horasExt100Funcionario,salFamilFuncionario,fgtsParcFuncionario,fgtsFeriasFUncionario,cafeFuncionario,uniformeFuncionario,repousoFuncionario,diasUteisEntrada,diasUteisSaida,
                                                                 intervaloEntrada,intervaloSaida,totSalario,totBeneficio,custMensal,custDiario,custHora,valeAlimentacao,assMedica,dividebh,id)
            updateString =cursor.execute("UPDATE `ezsys`.dp_funcionarios SET `salbase`= %s, `percinss`= %s, `salfuncao`= %s,`salliquido`= %s,`sal_12decterc`=%s,`sal_comiprem`=%s,`sal_12ferias`= %s,`sal_recebeprem`=%s,`sal_insalubr`=%s,`percfgts`=%s,`valetrp`=%s,`percmaxvaletrp`=%s,`sal_seguro`=%s,`sal_cesta`=%s,`sal_gremio`=%s,`sal_pensaoalim`=%s,`sal_partlucr`=%s,`sal_hrextra50`=%s,`sal_hrextra100`=%s,`sal_familia`=%s,`sal_fgts12decterc`=%s,`sal_fgts12ferias`=%s,`sal_cafe`=%s,`sal_uniforme`=%s,`sal_repsemremun`=%s,`hrdiautil1`=%s,`hrdiautil2`=%s,`hrintervalo1`=%s,`hrintervalo2`=%s,`sal_totsal`=%s,`sal_totbenef`=%s,`sal_customes`=%s,`sal_custodia`=%s,`sal_custohr`=%s, `sal_valealiment` =%s,`sal_assmedica` =%s, `sal_dividebh`=%s WHERE `id` = %s;", valores)
            cursor.execute(updateString)      
            con.commit()
            db.closeConn(cursor)    
            
        except Error as e :
               print(e)
               return   

    def inserirSalarioFuncionarios(self,salarioBase,inssFuncionario,salFuncaoFuncionario,salLiquidoFuncionario,decTerceiroFuncionario,comissaoFuncionario,feriarFuncionario,premiacaoFUncionario,Salinsalubridade,fgtsFuncionario,valTranspFuncionario,maxValeTranspFuncionario,seguroFuncionario,cestaFuncionario
                                                                 ,gremioFuncionario,pensaoAlimFuncionario,partLucrosFuncionario,horasExt50Funcionario,horasExt100Funcionario,salFamilFuncionario,fgtsParcFuncionario,fgtsFeriasFUncionario,cafeFuncionario,uniformeFuncionario,repousoFuncionario,diasUteisEntrada,diasUteisSaida,
                                                                 intervaloEntrada,intervaloSaida,totSalario,totBeneficio,custMensal,custDiario,custHora):
     db= DbConnection()
     try:
        con = db.getConn() 
        Cursor = con.cursor()
        queryString = """INSERT INTO ezsys.dp_funcionarios(`salbase`,`percinss`,`salfuncao`,`salliquido`,`sal_12decterc`,`sal_comiprem`,`sal_12ferias`,`sal_recebeprem`,`sal_insalubr`,`percfgts`,`valetrp`,`percmaxvaletrp`,`sal_seguro`,`sal_cesta`,`sal_gremio`,`sal_pensaoalim`,`sal_partlucr`,`sal_hrextra50`,`sal_hrextra100`,`sal_familia`,`sal_fgts12decterc`,`sal_fgts12ferias`,`sal_cafe`,`sal_uniforme`,`sal_repsemremun`,`hrdiautil1`,`hrdiautil2`,`hrintervalo1`,`hrintervalo2`,`sal_totsal`,`sal_totbenef`,`sal_customes`,`sal_custodia`,`sal_custohr`) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        values = (salarioBase,inssFuncionario,salFuncaoFuncionario,salLiquidoFuncionario,decTerceiroFuncionario,comissaoFuncionario,feriarFuncionario,premiacaoFUncionario,Salinsalubridade,fgtsFuncionario,valTranspFuncionario,maxValeTranspFuncionario,seguroFuncionario,cestaFuncionario
                                                                 ,gremioFuncionario,pensaoAlimFuncionario,partLucrosFuncionario,horasExt50Funcionario,horasExt100Funcionario,salFamilFuncionario,fgtsParcFuncionario,fgtsFeriasFUncionario,cafeFuncionario,uniformeFuncionario,repousoFuncionario,diasUteisEntrada,diasUteisSaida,
                                                                 intervaloEntrada,intervaloSaida,totSalario,totBeneficio,custMensal,custDiario,custHora)
        Cursor.execute(queryString, values)
        con.commit()
        print(Cursor.rowcount,'Registros inseridos na tabela',values)
        Cursor.close()
     except Error as erro:
      print('Falha ao inserir dados no Mysql: {}'.format(erro))
     finally:
        try:
            if(con.is_connected()):
             con.close()
            Cursor.close()
        except Error as erro:
         print(erro)
     
     
    def inserirSalarioFuncionarios(self, salario):
          db= DbConnection()
          try:
               con = db.getConn() 
               Cursor = con.cursor()
               queryString = """INSERT INTO ezsys.dp_funcionarios(`salbase`,`percinss`,`salfuncao`,`salliquido`,`sal_12decterc`,`sal_comiprem`,`sal_12ferias`,`sal_recebeprem`,`sal_insalubr`,`percfgts`,`valetrp`,`percmaxvaletrp`,`sal_seguro`,`sal_cesta`,`sal_gremio`,`sal_pensaoalim`,`sal_partlucr`,`sal_hrextra50`,`sal_hrextra100`,`sal_familia`,`sal_fgts12decterc`,`sal_fgts12ferias`,`sal_cafe`,`sal_uniforme`,`sal_repsemremun`,`hrdiautil1`,`hrdiautil2`,`hrintervalo1`,`hrintervalo2`,`sal_totsal`,`sal_totbenef`,`sal_customes`,`sal_custodia`,`sal_custohr`) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
               values = (salario.salario_base,
                         salario.inssFuncionario,
                         salario.salFuncaoFuncionario,
                         salario.salLiquidoFuncionario,
                         salario.decTerceiroFuncionario,
                         salario.comissaoFuncionario,
                         salario.feriarFuncionario,
                         salario.premiacaoFUncionario,
                         salario.Salinsalubridade,
                         salario.fgtsFuncionario,
                         salario.valTranspFuncionario,
                         salario.maxValeTranspFuncionario,
                         salario.seguroFuncionario,
                         salario.cestaFuncionario,
                         salario.gremioFuncionario,
                         salario.pensaoAlimFuncionario,
                         salario.partLucrosFuncionario,
                         salario.horasExt50Funcionario,
                         salario.horasExt100Funcionario,
                         salario.salFamilFuncionario,
                         salario.fgtsParcFuncionario,
                         salario.fgtsFeriasFUncionario,
                         salario.cafeFuncionario,
                         salario.uniformeFuncionario,
                         salario.repousoFuncionario,
                         salario.diasUteisEntrada,
                         salario.diasUteisSaida,
                         salario.intervaloEntrada,
                         salario.intervaloSaida,
                         salario.totSalario,
                         salario.totBeneficio,
                         salario.custMensal,
                         salario.custDiario,
                         salario.custHora)
               Cursor.execute(queryString, values)
               con.commit()
               print(Cursor.rowcount,'Registros inseridos na tabela',values)
               Cursor.close()
          except Error as erro:
               print('Falha ao inserir dados no Mysql: {}'.format(erro))
          finally:
               try:
                    if(con.is_connected()):
                         con.close()
                    Cursor.close()
               except Error as erro:
                    print(erro)  

#______________________________________________________COMISSIONAMENTO  FUNCIONARIOS_______________________________________________________________________________
    
    def selecionarComissaoInicial(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `comi` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario  
       
    def selecionarComissaoFinal(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `come` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario         
       
    def selecionarValordaCota(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `valor` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario   

    def selecionarComissaoAcimaTabela(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `comiacima` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario   

    def selecionarComissaoOverVenda(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `comiover` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario   

    def selecionarComissaoDiadePagamento1(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `pagadia` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario  

    def selecionarComissaoPeriododePagamentoInicial1(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `pgtocomiss1` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario   
       
    def selecionarComissaoPeriododePagamentoFinal1(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `pgtocomiss2` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario          

    def selecionarComissaoDiadePagamento2(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `pagadia2` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario 

    def selecionarComissaoPeriododePagamentoInicial2(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `pgtocomiss3` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario   

    def selecionarComissaoPeriododePagamentoFinal2(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `pgtocomiss4` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario 

    def selecionarComissaoaoFinalDaVenda(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `geractpgvd` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchall()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario   

    def selecionarComissaoDobradaDomingoseFeriados(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `comidobr` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchall()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario   
   
    def selecionarComissaoParticipacaoEmVendas(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `part` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario

    def selecionarComissaoTipodeParticipacaoEmVendas(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `tipopart` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchall()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario

    def selecionarComissaoPagamentoVenda(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `pagcomi1` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario

    def selecionarComissaoPagamentoCliente(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `pagcomi2` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario

    def selecionarComissaoGerarPrevisaoPagamento(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `geraprevpagcomi` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchall()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario

    def selecionarAbaterImpostosparaCalculoComissao(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `tpcomiimpost` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchall()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario    
    
    def selecionarComissaoPrimeiroRecebimentoVenda(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `geracomiprimreceb` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchall()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario

    def selecionarImpostodeRendaParaCalculoComissao(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `irsobrecom` FROM ezsys.dp_funcionarios WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario    

    def EditarComissaoFuncionarios(self,comissaoInicial,comissaoFinal,valorCota,comissaoAcima,comissaoOver,periodoComissao1,periodoComissao2,pagamentoDia1,periodoComissao3,periodoComissao4,pagamentodia2,gerarConta,comissaoDobrada,
                                   participacaoVenda,tipoparticipacao,pagamentoComissao,pagamentoRecebimento,gerarPrevisao,abaterImposto,impostoDeRenda,gerarComissao,id):
        db = DbConnection()
        try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (comissaoInicial,comissaoFinal,valorCota,comissaoAcima,comissaoOver,periodoComissao1,periodoComissao2,pagamentoDia1,periodoComissao3,periodoComissao4,pagamentodia2,gerarConta,comissaoDobrada,
                                   participacaoVenda,tipoparticipacao,pagamentoComissao,pagamentoRecebimento,gerarPrevisao,abaterImposto,impostoDeRenda,gerarComissao,id)
            updateString =cursor.execute("UPDATE ezsys.dp_funcionarios SET `comi`= %s, `come`= %s, `valor`= %s,`comiacima`= %s,`comiover`=%s,`pagadia`=%s,`pgtocomiss1`= %s,`pgtocomiss2`=%s,`pagadia2`=%s,`pgtocomiss3`=%s,`pgtocomiss4`=%s,`geractpgvd`=%s,`comidobr`=%s,`part`=%s,`tipopart`=%s,`pagcomi1`=%s,`pagcomi2`=%s,`geraprevpagcomi`=%s,`tpcomiimpost`=%s,`irsobrecom`=%s, `geracomiprimreceb`=%s WHERE `id` = %s;", valores)
            cursor.execute(updateString)      
            con.commit()
            db.closeConn(cursor)    
            
        except Error as e :
               print(e)
               return   

    def InserirComissaoFuncionarios(self,comissaoInicial,comissaoFinal,valorCota,comissaoAcima,comissaoOver,periodoComissao1,periodoComissao2,pagamentoDia1,periodoComissao3,periodoComissao4,pagamentodia2,gerarConta,comissaoDobrada,
                                   participacaoVenda,tipoparticipacao,pagamentoComissao,pagamentoRecebimento,gerarPrevisao,abaterImposto,impostoDeRenda,gerarComissao,id):
     db= DbConnection()
     try:
        con = db.getConn() 
        Cursor = con.cursor()
        queryString = """INSERT INTO ezsys.dp_funcionarios(`comi`, `come`, `valor`,`comiacima`,`comiover`,`pagadia`,`pgtocomiss1`,`pgtocomiss2`,`pagadia2`,`pgtocomiss3`,`pgtocomiss4`,`geractpgvd`,`comidobr`,`part`,`tipopart`,`pagcomi1`,`pagcomi2`,`geraprevpagcomi`,`tpcomiimpost`,`irsobrecom`, `geracomiprimreceb`,`id`) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        values = (comissaoInicial,comissaoFinal,valorCota,comissaoAcima,comissaoOver,periodoComissao1,periodoComissao2,pagamentoDia1,periodoComissao3,periodoComissao4,pagamentodia2,gerarConta,comissaoDobrada,
                                   participacaoVenda,tipoparticipacao,pagamentoComissao,pagamentoRecebimento,gerarPrevisao,abaterImposto,impostoDeRenda,gerarComissao,id)
        Cursor.execute(queryString, values)
        con.commit()
        print(Cursor.rowcount,'Registros inseridos na tabela',values)
        Cursor.close()
     except Error as erro:
      print('Falha ao inserir dados no Mysql: {}'.format(erro))
     finally:
        try:
            if(con.is_connected()):
             con.close()
            Cursor.close()
        except Error as erro:
         print(erro)  


#_____________________________________________________OCORRENCIAS DENTRO DE FUNCIONARIOS___________________________________________________________________________
   
   
    def SelecionarjanelaOcorrencias(self,usuarioid): 
       db = DbConnection()
        
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (usuarioid)
            usuario='select  * from ezsys.dp_ocorrencias where id = "{}"'.format(valores)
            cursor.execute(usuario)
            ver = cursor.fetchall()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario 

    def SelecionarOcorrencias(self,id): 
       db = DbConnection()
        
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (id)
            usuario = "SELECT `id`, `dataocorrencia`, `codocorr`, `descocorr`, `discrimina` FROM ezsys.dp_ocorrencias WHERE fk_dpocorencia='{}'".format(valores)

            cursor.execute(usuario)
            ver = cursor.fetchall()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario  
       
       
       
    def selecionarOcorrenciasPrincipais(self, id): 
     db = DbConnection()

     try:
          con = db.getConn()
          cursor = con.cursor(dictionary=True)
          valores=(id)
          usuario = "SELECT * FROM ezsys.dp_ocorrencias WHERE id='%s'",valores
          cursor.execute(usuario)
          ver = cursor.fetchall()
          print(ver) 
          db.closeConn(cursor)    
          return ver
     except Error as e:
          print(e)
          return None
       
   
    def inserirOcorrenciasFuncionarios(self, Data, Codigo, Descricao, Discriminacao,nome,ID):
     db= DbConnection()
     try:
        con = db.getConn() 
        Cursor = con.cursor()
        queryString = """INSERT INTO ezsys.dp_ocorrencias(`dataocorrencia`,`codocorr`,`descocorr`,`discrimina`,`funcionario`,fk_dpocorencia) values (%s,%s,%s,%s,%s,%s)"""
        values = (Data, Codigo, Descricao, Discriminacao,nome,ID)
        Cursor.execute(queryString, values)
        con.commit()
        print(Cursor.rowcount,'Registros inseridos na tabela',values)
        Cursor.close()
     except Error as erro:
      print('Falha ao inserir dados no Mysql: {}'.format(erro))
     finally:
        try:
            if(con.is_connected()):
             con.close()
            Cursor.close()
        except Error as erro:
         print(erro)              
         

    def DeletarOcorrenciasFuncionarios(self,usuario):   
     db = DbConnection()
     try:
        con = db.getConn()     
        cursor= con.cursor(dictionary = True)
        valores = (usuario)
        sql = "DELETE FROM `ezsys`.dp_ocorrencias WHERE id= {};".format(valores)
        cursor.execute(sql)
        con.commit()
        db.closeConn(cursor)  
        print(cursor.rowcount, "registro excluído")  
        return True
     except Error as e :
          print(e)

    def selecionarDataOcorrenciasFuncionarios(self, texto): 
     db = DbConnection()
     try:
          con = db.getConn()
          cursor = con.cursor(dictionary=True)
          valores = (texto,)
          select = "SELECT dataocorrencia FROM `ezsys`.dp_ocorrencias  WHERE id = %s;"
          cursor.execute(select, valores)
          ver = cursor.fetchone()
          db.closeConn(cursor)
          if ver is None:
               return {'dataocorrencia': None}
          return ver
     except Error as e:
          print(e)
          return {'dataocorrencia': None}

    def selecionarCodigodeOcorrenciasFuncionarios(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT codocorr FROM `ezsys`.dp_ocorrencias  WHERE id = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario   

    def selecionarDescricaoOcorrenciasFuncionarios(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT descocorr FROM `ezsys`.dp_ocorrencias  WHERE id = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario   

    def selecionarDiscrminacaoOcorrenciasFuncionarios(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `discrimina` FROM `ezsys`.dp_ocorrencias  WHERE id = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario  

    def EditarOcorrenciasFuncionarios(self, data,codigo,descricao,discriminacao,funcionario,codigo_funcionario, id):
        db = DbConnection()
        try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (data,codigo,descricao,discriminacao,funcionario,codigo_funcionario, id) 
            updateString = "UPDATE `ezsys`.dp_ocorrencias SET `dataocorrencia`= '{}', `codocorr`= '{}', `descocorr`= '{}', `discrimina`= '{}', `funcionario`= '{}', `fk_dpocorencia`= '{}' WHERE `id` = '{}'".format(*valores)
            cursor.execute(updateString)      
            con.commit()
            db.closeConn(cursor)    
            
        except Error as e :
               print(e)
               return   

#____________________________________________________Registro Férias Funcionários_______________________________________________
    def SelecionarjanelaFerias(self,usuarioid): 
       db = DbConnection()
        
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (usuarioid)
            usuario='select  * from ezsys.dp_funcionariosferias where fk_feriasid = "{}"'.format(valores)
            cursor.execute(usuario)
            ver = cursor.fetchall()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario 

    def SelecionarFerias(self,usuarioid): 
       db = DbConnection()
        
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (usuarioid)
            usuario='select `id`, `data1`,`data2` from ezsys.dp_funcionariosferias where fk_feriasid = "{}"'.format(valores)
            cursor.execute(usuario)
            ver = cursor.fetchall()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario  

    def inserirFeriasFuncionarios(self, Data1, Data2, nome,ID):
     db= DbConnection()
     try:
        con = db.getConn() 
        Cursor = con.cursor()
        queryString = """INSERT INTO ezsys.dp_funcionariosferias(`data1`,`data2`,funcionario, fk_feriasid) values (%s,%s,%s,%s)"""
        values = (Data1, Data2, nome,ID)
        Cursor.execute(queryString, values)
        con.commit()
        print(Cursor.rowcount,'Registros inseridos na tabela',values)
        Cursor.close()
     except Error as erro:
      print('Falha ao inserir dados no Mysql: {}'.format(erro))
     finally:
        try:
            if(con.is_connected()):
             con.close()
            Cursor.close()
        except Error as erro:
         print(erro)      

    def selecionarDataFeriasDeFuncionarios(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT data1 FROM `ezsys`.dp_funcionariosferias  WHERE id = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario    

    def selecionarDataFeriasAteFuncionarios(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT data2 FROM `ezsys`.dp_funcionariosferias  WHERE id = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario    

    def EditarFeriasAteFuncionario(self,Data1, Data2 ,ID):
        db = DbConnection()
        try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (Data1, Data2 ,ID)
            #cursor.execute('SELECT nome, senha FROM ` `ezsys``.senha WHERE nome = %s AND senha = %s', valores)
            #cursor.execute('truncate table `ezsys`.woodpaper')
            updateString =cursor.execute("UPDATE `ezsys`.dp_funcionariosferias SET `data1`= %s,`data2`= %s WHERE `id` = %s;", valores)
            cursor.execute(updateString)      
            con.commit()
            db.closeConn(cursor)    
            
        except Error as e :
               print(e)
               return    

    def DeletarFeriasFuncionarios(self,usuario):   
     db = DbConnection()
     try:
        con = db.getConn()     
        cursor= con.cursor(dictionary = True)
        valores = (usuario)
        sql = "DELETE FROM `ezsys`.dp_funcionariosferias WHERE id= {};".format(valores)
        cursor.execute(sql)
        con.commit()
        db.closeConn(cursor)  
        print(cursor.rowcount, "registro excluído")  
        return True
     except Error as e :
          print(e)
#_________________________________________________Registro Filhos Funcionários________________________________________________
    def SelecionarjanelaFilhos(self,usuarioid): 
       db = DbConnection()
        
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (usuarioid)
            usuario='select  * from ezsys.dp_funcionariosfilhos where fk_filhosid = "{}"'.format(valores)
            cursor.execute(usuario)
            ver = cursor.fetchall()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario 

    def SelecionarFilhos(self,usuarioid): 
       db = DbConnection()
        
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (usuarioid)
            usuario='select `id`, `nomefilh`,`idade`,`nascimento` from ezsys.dp_funcionariosfilhos where fk_filhosid = "{}"'.format(valores)
            cursor.execute(usuario)
            ver = cursor.fetchall()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario  

    def inserirFilhosFuncionarios(self, nome, idade, data,nomefunc,ID):
     db= DbConnection()
     try:
        con = db.getConn() 
        Cursor = con.cursor()
        queryString = """INSERT INTO ezsys.dp_funcionariosfilhos(`nomefilh`,`idade`,`nascimento`,`funcionario`,`fk_filhosid`) values (%s,%s,%s,%s,%s)"""
        values = (nome, idade, data,nomefunc,ID)
        Cursor.execute(queryString, values)
        con.commit()
        print(Cursor.rowcount,'Registros inseridos na tabela',values)
        Cursor.close()
     except Error as erro:
      print('Falha ao inserir dados no Mysql: {}'.format(erro))
     finally:
        try:
            if(con.is_connected()):
             con.close()
            Cursor.close()
        except Error as erro:
         print(erro)  

    def selecionarDataDeNascimentoFilho(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT nascimento FROM `ezsys`.dp_funcionariosfilhos  WHERE id = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario    

    def selecionarIDadeFilho(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `idade` FROM `ezsys`.dp_funcionariosfilhos  WHERE id = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario  

    def selecionarNomeFilho(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `nomefilh` FROM `ezsys`.dp_funcionariosfilhos  WHERE id = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario  

    def EditarFilhosFuncionario(self, nome, idade, data, ID):
        db = DbConnection()
        try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (nome, idade, data, ID)
            #cursor.execute('SELECT nome, senha FROM ` `ezsys``.senha WHERE nome = %s AND senha = %s', valores)
            #cursor.execute('truncate table `ezsys`.woodpaper')
            updateString =cursor.execute("UPDATE `ezsys`.dp_funcionariosfilhos SET `nomefilh`= %s,`idade`= %s, `nascimento` =%s WHERE `id` = %s;", valores)
            cursor.execute(updateString)      
            con.commit()
            db.closeConn(cursor)    
            
        except Error as e :
               print(e)
               return    

    def DeletarFilhosFuncionarios(self,usuario):   
     db = DbConnection()
     try:
        con = db.getConn()     
        cursor= con.cursor(dictionary = True)
        valores = (usuario)
        sql = "DELETE FROM `ezsys`.dp_funcionariosfilhos WHERE id= {};".format(valores)
        cursor.execute(sql)
        con.commit()
        db.closeConn(cursor)  
        print(cursor.rowcount, "registro excluído")  
        return True
     except Error as e :
          print(e)
# ____________________________________________________________CARGOS__________________________________________________________________________
    def consultarCargos(self):
     db = DbConnection()
     user = None
     try:
        con = db.getConn()     
        cursor= con.cursor()
        valores = ()
        # con = mysql.connector.connect(host='127.0.0.1', user='root', database='eztestes',password='q9w8e7#MTB')
        cursor.execute("SELECT `id`, `nome`,`sal_sindicato`,`valemaxmes`,`de1`,`ate1`,`percprem1`,`de2`,`ate2`,`percprem2`,`de3`,`ate3`,`percprem3`,`de4`,`ate4`,`percprem4` FROM ezsys.dp_cargos order by `nome` asc;")      
        ver = cursor.fetchall()
        print(ver)
            
            
        db.closeConn(cursor)    
        return ver
     except Error as e :
            print(e)
            return user     

    def inserirCargos(self, nome,salario,valAdiantado,valMax,horarioDe,horarioAte,comissoesPremio,comissaovalor,insalubridade,fgts,vale,maxVale,seguro,cBasica,inss,pdecimoterceiro,ferias,partlucros,horaextmetade,horaextinteira,salariofam,pfgts,pferias,cafe,uniforme,repouso,de1,ate1,porc1,premio1,de2,ate2,porc2,premio2,de3,ate3,porc3,premio3,de4,ate4,porc4,premio4):
     db= DbConnection()
     try:
        con = db.getConn() 
        Cursor = con.cursor()
        queryString = """INSERT INTO ezsys.dp_cargos(`nome`,`sal_sindicato`,`valadianta`,`valemaxmes`,`hortrab1`,`hortrab2`,`sal_comiprem`,`sal_recebeprem`,`sal_insalubr`,`percfgts`,`valetrp`,`percmaxvaletrp`,`sal_seguro`,`sal_cesta`,`percinss`,`sal_12decterc`,`sal_12ferias`,`sal_partlucr`,`sal_hrextra50`,`sal_hrextra100`,`sal_familia`,`sal_fgts12decterc`,`sal_fgts12ferias`,`sal_cafe`,`sal_uniforme`,`sal_repsemremun`,`de1`,`ate1`,`percprem1`,`tipprem1`,`de2`,`ate2`,`percprem2`,`tipprem2`,`de3`,`ate3`,`percprem3`,`tipprem3`,`de4`,`ate4`,`percprem4`,`tipprem4`) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        values = (nome,salario,valAdiantado,valMax,horarioDe,horarioAte,comissoesPremio,comissaovalor,insalubridade,fgts,vale,maxVale,seguro,cBasica,inss,pdecimoterceiro,ferias,partlucros,horaextmetade,horaextinteira,salariofam,pfgts,pferias,cafe,uniforme,repouso,de1,ate1,porc1,premio1,de2,ate2,porc2,premio2,de3,ate3,porc3,premio3,de4,ate4,porc4,premio4)
        Cursor.execute(queryString, values)
        con.commit()
        print(Cursor.rowcount,'Registros inseridos na tabela')
        Cursor.close()
     except Error as erro:
      print('Falha ao inserir dados no Mysql: {}'.format(erro))
     finally:
        try:
            if(con.is_connected()):
             con.close()
            Cursor.close()
        except Error as erro:
         print(erro)            
   
    def EditarCargos(self,nome,salario,valAdiantado,valMax,horarioDe,horarioAte,comissoesPremio,comissaovalor,insalubridade,fgts,vale,maxVale,seguro,cBasica,inss,pdecimoterceiro,ferias,partlucros,horaextmetade,horaextinteira,salariofam,pfgts,pferias,cafe,uniforme,repouso,de1,ate1,porc1,premio1,de2,ate2,porc2,premio2,de3,ate3,porc3,premio3,de4,ate4,porc4,premio4,id):
        db = DbConnection()
        try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (nome,salario,valAdiantado,valMax,horarioDe,horarioAte,comissoesPremio,comissaovalor,insalubridade,fgts,vale,maxVale,seguro,cBasica,inss,pdecimoterceiro,ferias,partlucros,horaextmetade,horaextinteira,salariofam,pfgts,pferias,cafe,uniforme,repouso,de1,ate1,porc1,premio1,de2,ate2,porc2,premio2,de3,ate3,porc3,premio3,de4,ate4,porc4,premio4,id)
            #cursor.execute('SELECT nome, senha FROM ` `ezsys``.senha WHERE nome = %s AND senha = %s', valores)
            #cursor.execute('truncate table `ezsys`.woodpaper')
            updateString =cursor.execute("UPDATE `ezsys`.dp_cargos SET `nome`= %s,`sal_sindicato`= %s,`valadianta`= %s,`valemaxmes`= %s,`hortrab1`= %s,`hortrab2`= %s,`sal_comiprem`= %s,`sal_recebeprem`= %s,`sal_insalubr`= %s,`percfgts`= %s,`valetrp`= %s,`percmaxvaletrp`= %s,`sal_seguro`= %s,`sal_cesta`= %s,`percinss`= %s,`sal_12decterc`= %s,`sal_12ferias`= %s,`sal_partlucr`= %s,`sal_hrextra50`= %s,`sal_hrextra100`= %s,`sal_familia`= %s,`sal_fgts12decterc`= %s,`sal_fgts12ferias`= %s,`sal_cafe`= %s,`sal_uniforme`= %s,`sal_repsemremun`= %s,`de1`= %s,`ate1`= %s,`percprem1`= %s,`tipprem1`= %s,`de2`= %s,`ate2`= %s,`percprem2`= %s,`tipprem2`= %s,`de3`= %s,`ate3`= %s,`percprem3`= %s,`tipprem3`= %s,`de4`= %s,`ate4`= %s,`percprem4`= %s,`tipprem4`= %s WHERE `id` = %s;", valores)
            cursor.execute(updateString)      
            con.commit()
            db.closeConn(cursor)    
            
        except Error as e :
               print(e)
               return       
    
    def selecionarNaTabelaCargos(self,id):
     db = DbConnection()
     user = None
     try:
        con = db.getConn()     
        cursor= con.cursor(dictionary=True)
        valores = (id)
        # con = mysql.connector.connect(host='127.0.0.1', user='root', database='eztestes',password='q9w8e7#MTB')
        select="SELECT * FROM `ezsys`.dp_cargos WHERE `id` = {};".format(valores)
        #data,solicitacao_assunto,solicitacao_texto,solicitacao_status,solicitacao_incluido,solicitacao_editado   
        cursor.execute(select)
        ver = cursor.fetchone()                       
        db.closeConn(cursor)    
        return ver
     except Error as e :
            print(e)
            return user 

    def DeletarCargos(self,usuario):   
     db = DbConnection()
     try:
        con = db.getConn()     
        cursor= con.cursor(dictionary = True)
        valores = (usuario)
        sql = "DELETE FROM `ezsys`.dp_cargos WHERE id= {};".format(valores)
        cursor.execute(sql)
        con.commit()
        db.closeConn(cursor)  
        print(cursor.rowcount, "registro excluído")  
        return True
     except Error as e :
          print(e)

    def selecionarCargoNome(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `nome` FROM ezsys.dp_cargos WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario  

    def selecionarCargoSalSindicato(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_sindicato` FROM ezsys.dp_cargos WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario  

    def selecionarCargoSalAdiantamento(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `valadianta` FROM ezsys.dp_cargos WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario  
         
    def selecionarCargoValeMax(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `valemaxmes` FROM ezsys.dp_cargos WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario  
         
    def selecionarCargoHoraTrab1(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `hortrab1` FROM ezsys.dp_cargos WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario  
         
    def selecionarCargoHoraTrab2(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `hortrab2` FROM ezsys.dp_cargos WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario  
         
    def selecionarCargoComPremios(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_comiprem` FROM ezsys.dp_cargos WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario                                      
                  
    def selecionarCargoRecebePremio(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_recebeprem` FROM ezsys.dp_cargos WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchall()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario                                      

    def selecionarCargoSalInsalubridade(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_insalubr` FROM ezsys.dp_cargos WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario                                      

    def selecionarCargoFGTS(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `percfgts` FROM ezsys.dp_cargos WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario                                      

    def selecionarCargoValeTransporte(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `valetrp` FROM ezsys.dp_cargos WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario           
         
    def selecionarCargoMaxValeTransp(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `percmaxvaletrp` FROM ezsys.dp_cargos WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario           
         
    def selecionarCargoSalSeguro(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_seguro` FROM ezsys.dp_cargos WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario                             
         
    def selecionarCargoSalCestaBasica(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_cesta` FROM ezsys.dp_cargos WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario  
         
    def selecionarCargoInss(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `percinss` FROM ezsys.dp_cargos WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario  
         
    def selecionarCargoSalPercDecimoTerceiro(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_12decterc` FROM ezsys.dp_cargos WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario      
         
    def selecionarCargoPercFerias(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_12ferias` FROM ezsys.dp_cargos WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario     
         
    def selecionarCargoSalPartLucros(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_partlucr` FROM ezsys.dp_cargos WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario     
         
    def selecionarCargoHoraExtraMet(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_hrextra50` FROM ezsys.dp_cargos WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario     
         
    def selecionarCargoHoraExtraInt(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_hrextra100` FROM ezsys.dp_cargos WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario      
             
    def selecionarCargoSalFamilia(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_familia` FROM ezsys.dp_cargos WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario     
         
    def selecionarCargoPercfgtsDecTerceiro(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_fgts12decterc` FROM ezsys.dp_cargos WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario     
         
    def selecionarCargoPercfgtsDecFerias(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_fgts12ferias` FROM ezsys.dp_cargos WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario     
         
    def selecionarCargoSalCafe(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_cafe` FROM ezsys.dp_cargos WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario                                                                                       

    def selecionarCargoSalUniforme(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_uniforme` FROM ezsys.dp_cargos WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario    
         
    def selecionarCargoSalRepouso(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `sal_repsemremun` FROM ezsys.dp_cargos WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario    
         
    def selecionarCargoPercPremiode1(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `de1` FROM ezsys.dp_cargos WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario    
         
    def selecionarCargoPercPremioate1(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `ate1` FROM ezsys.dp_cargos WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario    
         
    def selecionarCargoPercpremio1(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `percprem1` FROM ezsys.dp_cargos WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario       
         
    def selecionarCargoTipoPercPremio1(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `tipprem1` FROM ezsys.dp_cargos WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchall()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario                                              

    def selecionarCargoPercPremiode2(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `de2` FROM ezsys.dp_cargos WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario    
         
    def selecionarCargoPercPremioate2(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `ate2` FROM ezsys.dp_cargos WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario    
         
    def selecionarCargoPercpremio2(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `percprem2` FROM ezsys.dp_cargos WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario       
         
    def selecionarCargoTipoPercPremio2(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `tipprem2` FROM ezsys.dp_cargos WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchall()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario         

    def selecionarCargoPercPremiode3(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `de3` FROM ezsys.dp_cargos WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario    
         
    def selecionarCargoPercPremioate3(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `ate3` FROM ezsys.dp_cargos WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario    
         
    def selecionarCargoPercpremio3(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `percprem3` FROM ezsys.dp_cargos WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario       
         
    def selecionarCargoTipoPercPremio3(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `tipprem3` FROM ezsys.dp_cargos WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchall()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario         

    def selecionarCargoPercPremiode4(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `de4` FROM ezsys.dp_cargos WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario    
         
    def selecionarCargoPercPremioate4(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `ate4` FROM ezsys.dp_cargos WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario    
         
    def selecionarCargoPercpremio4(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `percprem4` FROM ezsys.dp_cargos WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario       
         
    def selecionarCargoTipoPercPremio4(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `tipprem4` FROM ezsys.dp_cargos WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchall()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario         
#_______________________________________________________________________Funções_________________________________________________________________________________________________________

    def consultarFuncoes(self):
     db = DbConnection()
     user = None
     try:
        con = db.getConn()     
        cursor= con.cursor()
        valores = ()
        # con = mysql.connector.connect(host='127.0.0.1', user='root', database='eztestes',password='q9w8e7#MTB')
        cursor.execute("SELECT `id`, `nome`,`desctarefa`,`desp`,`tipopagamento`,`valproddia`,`valprodhrnorm`,`valprodhrext`,`valprodhrdbr`,`valbonus`,`valbonusdia` FROM `ezsys`.dp_funcoes ORDER BY `nome` ASC;")      
        ver = cursor.fetchall()
        print(ver)
            
            
        db.closeConn(cursor)    
        return ver
     except Error as e :
            print(e)
            return user
    
    def selecionarnaTabelaFuncoes(self,id):
     db = DbConnection()
     user = None
     try:
        con = db.getConn()     
        cursor= con.cursor(dictionary=True)
        valores = (id)
        # con = mysql.connector.connect(host='127.0.0.1', user='root', database='eztestes',password='q9w8e7#MTB')
        select="SELECT * FROM `ezsys`.dp_feriados WHERE `id` = {};".format(valores)
        #data,solicitacao_assunto,solicitacao_texto,solicitacao_status,solicitacao_incluido,solicitacao_editado   
        cursor.execute(select)
        ver = cursor.fetchone()                       
        db.closeConn(cursor)    
        return ver
     except Error as e :
            print(e)
            return user       
         
    def selecionarFuncaoNome(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT nome FROM ezsys.dp_funcoes WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario            
         
    def selecionarFuncaoDescTarefa(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT desctarefa FROM ezsys.dp_funcoes WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario                  

    def selecionarFuncaoTipoPagamento(self, texto): 
        db = DbConnection()

        usuario = None
        try:
            con = db.getConn()
            cursor = con.cursor(dictionary=True)
            valores = (texto,)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select = "SELECT desp FROM ezsys.dp_funcoes WHERE `id` = %s;"
            cursor.execute(select, valores)
            resultado = cursor.fetchone()
            if resultado is None:
               return None
            else:
               return resultado['desp']
        except Error as e:
          print(e)
        finally:
          db.closeConn(cursor)

       
    def selecionarFuncaoTipoPagamentoDesp(self): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = ()
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select = ("SELECT nome FROM ezsys.class  order by nome ASC")
            cursor.execute(select)  
            ver = cursor.fetchall()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario                

    def selecionarFuncaoPagamento(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT tipopagamento FROM ezsys.dp_funcoes WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchall()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario   

    def selecionarFuncaoSalarioFuncionario(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT salfun FROM ezsys.dp_funcoes WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario   

    def selecionarFuncaoValorProducaoDia(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT valproddia FROM ezsys.dp_funcoes WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario   

    def selecionarFuncaoValorProducaoHoraNormal(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT valprodhrnorm FROM ezsys.dp_funcoes WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario  

    def selecionarFuncaoValorProducaoHoraExtra(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT valprodhrext FROM ezsys.dp_funcoes WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario  

    def selecionarFuncaoValorProducaoHoraDobrada(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT valprodhrdbr FROM ezsys.dp_funcoes WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario  

    def selecionarFuncaQuantidadeAdicional(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT valbonus FROM ezsys.dp_funcoes WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario  

    def selecionarFuncaValorBonusDiario(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT valbonusdia FROM ezsys.dp_funcoes WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario  

    def inserirFuncoes(self, Nome,  Descricao, desp, SalarioFuncionario, Pagamento,  ProducaoDia,ProducaoHoraNormal,ProducaoHoraExtra,ProducaoHoraDobrada,QuantidadeAdicional,BonusDiario):
     db= DbConnection()
     try:
        con = db.getConn() 
        Cursor = con.cursor()
        queryString = """INSERT INTO ezsys.dp_funcoes (`nome`,`desctarefa`,`desp`,`salfun`,`tipopagamento`,`valproddia`,`valprodhrnorm`,`valprodhrext`,`valprodhrdbr`,`valbonus`,`valbonusdia`) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        values = (Nome,  Descricao, desp,  SalarioFuncionario, Pagamento, ProducaoDia,ProducaoHoraNormal,ProducaoHoraExtra,ProducaoHoraDobrada,QuantidadeAdicional,BonusDiario)
        Cursor.execute(queryString, values)
        con.commit()
        print(Cursor.rowcount,'Registros inseridos na tabela')
        Cursor.close()
     except Error as erro:
      print('Falha ao inserir dados no Mysql: {}'.format(erro))
     finally:
        try:
            if(con.is_connected()):
             con.close()
            Cursor.close()
        except Error as erro:
         print(erro)                  
        
    def EditarFuncoes(self, Nome,  Descricao, TipoPagamento, Pagamento, SalarioFuncionario, ProducaoDia,ProducaoHoraNormal,ProducaoHoraExtra,ProducaoHoraDobrada,QuantidadeAdicional,BonusDiario, id):
        db = DbConnection()
        try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (Nome,  Descricao, TipoPagamento, Pagamento, SalarioFuncionario, ProducaoDia,ProducaoHoraNormal,ProducaoHoraExtra,ProducaoHoraDobrada,QuantidadeAdicional,BonusDiario, id)
            #cursor.execute('SELECT nome, senha FROM ` `ezsys``.senha WHERE nome = %s AND senha = %s', valores)
            #cursor.execute('truncate table `ezsys`.woodpaper')
            updateString ="UPDATE `ezsys`.`dp_funcoes` SET nome= '{}', desctarefa= '{}', desp= '{}', salfun= '{}', tipopagamento= '{}' , valproddia= '{}', valprodhrnorm= '{}',valprodhrext= '{}', valprodhrdbr= '{}', valbonus= '{}',  valbonusdia= '{}' WHERE `id` = {};".format(Nome,  Descricao, TipoPagamento, Pagamento, SalarioFuncionario, ProducaoDia,ProducaoHoraNormal,ProducaoHoraExtra,ProducaoHoraDobrada,QuantidadeAdicional,BonusDiario, id)
            cursor.execute(updateString)      
            con.commit()
            db.closeConn(cursor)    
            
        except Error as e :
               print(e)
               return           

    def DeletarFuncoes(self,usuario):   
     db = DbConnection()
     try:
        con = db.getConn()     
        cursor= con.cursor(dictionary = True)
        valores = (usuario)
        sql = "DELETE FROM `ezsys`.`dp_funcoes` WHERE id= {};".format(valores)
        cursor.execute(sql)
        con.commit()
        db.closeConn(cursor)  
        print(cursor.rowcount, "registro excluído")  
        return True
     except Error as e :
          print(e)



# ________________________________________________________________________________Feriados_____________________________________________________
  
    def ConsultarFeriados(self):
     db = DbConnection()
     user = None
     try:
        con = db.getConn()     
        cursor= con.cursor()
        valores = ()
        # con = mysql.connector.connect(host='127.0.0.1', user='root', database='eztestes',password='q9w8e7#MTB')
        cursor.execute("SELECT id, data, diasemana, descricao FROM `ezsys`.dp_feriados ORDER BY `data` ASC"),valores
        ver = cursor.fetchall()
        print(ver)
    
        db.closeConn(cursor)    
        return ver
     except Error as e :
            print(e)
            return user   


    def selecionarTabelaFeriados(self,id):
     db = DbConnection()
     user = None
     try:
        con = db.getConn()     
        cursor= con.cursor(dictionary=True)
        valores = (id)
        # con = mysql.connector.connect(host='127.0.0.1', user='root', database='eztestes',password='q9w8e7#MTB')
        select="SELECT * FROM `ezsys`.dp_feriados WHERE `id` = {};".format(valores)
        #data,solicitacao_assunto,solicitacao_texto,solicitacao_status,solicitacao_incluido,solicitacao_editado   
        cursor.execute(select)
        ver = cursor.fetchone()                       
        db.closeConn(cursor)    
        return ver
     except Error as e :
            print(e)
            return user 
                            
        
    def selecionarFeriadoDescricao(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT descricao FROM ezsys.dp_feriados WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario           
         
    def selecionarFeriadoData(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT data FROM ezsys.dp_feriados WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario             
        
    def consultarFilhos(self):
     db = DbConnection()
     user = None
     try:
        con = db.getConn()     
        cursor= con.cursor()
        valores = ()
        # con = mysql.connector.connect(host='127.0.0.1', user='root', database='eztestes',password='q9w8e7#MTB')
        cursor.execute("SELECT id, `idade`,`nascimento`,`nome`,`nomefilh` FROM `ezsys`.dp_funcionariosfilhos")      
        ver = cursor.fetchall()
        print(ver)
            
            
        db.closeConn(cursor)    
        return ver
     except Error as e :
            print(e)
            return user        
        
    def inserirFeriado(self, data,descricao):
     db= DbConnection()
     try:
        con = db.getConn() 
        Cursor = con.cursor()
        queryString = """INSERT INTO ezsys.dp_feriados (`data`,`descricao`) values (%s,%s)"""
        values = (data,descricao)
        Cursor.execute(queryString, values)
        con.commit()
        print(Cursor.rowcount,'Registros inseridos na tabela')
        Cursor.close()
     except Error as erro:
      print('Falha ao inserir dados no Mysql: {}'.format(erro))
     finally:
        try:
            if(con.is_connected()):
             con.close()
            Cursor.close()
        except Error as erro:
         print(erro)                  
        
    def EditarFeriados(self,data,desc,id):
        db = DbConnection()
        try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (data, desc,id)
            #cursor.execute('SELECT nome, senha FROM ` `ezsys``.senha WHERE nome = %s AND senha = %s', valores)
            #cursor.execute('truncate table `ezsys`.woodpaper')
            updateString ="UPDATE `ezsys`.`dp_feriados` SET data= '{}', descricao= '{}'  WHERE id = {};".format(data, desc,id)
            cursor.execute(updateString)      
            con.commit()
            db.closeConn(cursor)    
            
        except Error as e :
               print(e)
               return                      
   
    def DeletarFeriados(self,usuario):   
     db = DbConnection()
     try:
        con = db.getConn()     
        cursor= con.cursor(dictionary = True)
        valores = (usuario)
        sql = "DELETE FROM `ezsys`.`dp_feriados` WHERE id= {};".format(valores)
        cursor.execute(sql)
        con.commit()
        db.closeConn(cursor)  
        print(cursor.rowcount, "registro excluído")  
        return True
     except Error as e :
          print(e)
          return False                
#___________________________________________________Acidentes_________________________________________

    def ConsultarAcidentes(self):
     db = DbConnection()
     user = None
     try:
        con = db.getConn()     
        cursor= con.cursor()
        valores = ()
        # con = mysql.connector.connect(host='127.0.0.1', user='root', database='eztestes',password='q9w8e7#MTB')
        cursor.execute("SELECT id, data, descricao, qt_pessoasafastadas, qt_pessoasnaoafastadas FROM `ezsys`.dp_acidentes ORDER BY `data` ASC"),valores
        ver = cursor.fetchall()
        print(ver)
    
        db.closeConn(cursor)    
        return ver
     except Error as e :
            print(e)
            return user            


    def inserirAcidente(self, data, descricao, qt_pessoasafastadas, qt_pessoasnaoafastadas):
     db= DbConnection()
     try:
        con = db.getConn() 
        Cursor = con.cursor()
        queryString = """INSERT INTO ezsys.dp_acidentes (`data`, `descricao`, `qt_pessoasafastadas`, `qt_pessoasnaoafastadas`) values (%s,%s,%s,%s)"""
        values = (data,descricao,qt_pessoasafastadas,qt_pessoasnaoafastadas)
        Cursor.execute(queryString, values)
        con.commit()
        print(Cursor.rowcount,'Registros inseridos na tabela')
        Cursor.close()
     except Error as erro:
      print('Falha ao inserir dados no Mysql: {}'.format(erro))
     finally:
        try:
            if(con.is_connected()):
             con.close()
            Cursor.close()
        except Error as erro:
         print(erro)         


    def DeletarAcidente(self,usuario):   
     db = DbConnection()
     try:
        con = db.getConn()     
        cursor= con.cursor(dictionary = True)
        valores = (usuario)
        sql = "DELETE FROM `ezsys`.`dp_acidentes` WHERE id= {};".format(valores)
        cursor.execute(sql)
        con.commit()
        db.closeConn(cursor)  
        print(cursor.rowcount, "registro excluído")  
        return True
     except Error as e :
          print(e)
          return False     


    def EditarAcidente(self,data, descricao, qt_pessoasafastadas, qt_pessoasnaoafastadas, id):
        db = DbConnection()
        try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = ( descricao, qt_pessoasafastadas, qt_pessoasnaoafastadas, id)
            #cursor.execute('SELECT nome, senha FROM ` `ezsys``.senha WHERE nome = %s AND senha = %s', valores)
            #cursor.execute('truncate table `ezsys`.woodpaper'
            updateString = "UPDATE `ezsys`.`dp_acidentes` SET data= '{}',  descricao= '{}', qt_pessoasafastadas= {}, qt_pessoasnaoafastadas= {}  WHERE id = {};".format(data, descricao, qt_pessoasafastadas, qt_pessoasnaoafastadas, id)
            cursor.execute(updateString)      
            con.commit()
            db.closeConn(cursor)    
            
        except Error as e :
               print(e)
               return     


    def selecionarAcidenteData(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT data FROM ezsys.dp_acidentes WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario    


    def selecionarAcidenteDescricao(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT descricao FROM ezsys.dp_acidentes WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario  


    def selecionarAcidenteQuantidadepessoasafastadas(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT qt_pessoasafastadas FROM ezsys.dp_acidentes WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario 
         
    def selecionarAcidenteQuantidadepessoasNaoAfastadas(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT qt_pessoasnaoafastadas FROM ezsys.dp_acidentes WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario          


#_______________________________________________________________TRANSPORTES_________________________________________________________________________________

    def ConsultarTrasporte(self):
     db = DbConnection()
     user = None
     try:
        con = db.getConn()     
        cursor= con.cursor()
        valores = ()
        # con = mysql.connector.connect(host='127.0.0.1', user='root', database='eztestes',password='q9w8e7#MTB')
        cursor.execute("SELECT id, linha, fornecedor, itinerario, valor FROM `ezsys`.dp_transportes"),valores
        ver = cursor.fetchall()
        print(ver)
    
        db.closeConn(cursor)    
        return ver
     except Error as e :
            print(e)
            return user            


    def inserirTransporte(self, linha, fornecedor,itinerario , valor):
     db= DbConnection()
     try:
        con = db.getConn() 
        Cursor = con.cursor()
        queryString = """INSERT INTO ezsys.dp_transportes (`linha`, `fornecedor`, `itinerario`,`valor`) values (%s,%s,%s,%s)"""
        values = (linha, fornecedor,itinerario , valor)
        Cursor.execute(queryString, values)
        con.commit()
        print(Cursor.rowcount,'Registros inseridos na tabela')
        Cursor.close()
     except Error as erro:
      print('Falha ao inserir dados no Mysql: {}'.format(erro))
     finally:
        try:
            if(con.is_connected()):
             con.close()
            Cursor.close()
        except Error as erro:
         print(erro)         


    def DeletarTransporte(self,usuario):   
     db = DbConnection()
     try:
        con = db.getConn()     
        cursor= con.cursor(dictionary = True)
        valores = (usuario)
        sql = "DELETE FROM `ezsys`.`dp_transportes` WHERE id= {};".format(valores)
        cursor.execute(sql)
        con.commit()
        db.closeConn(cursor)  
        print(cursor.rowcount, "registro excluído")  
        return True
     except Error as e :
          print(e)
          return False     


    def EditarTransporte(self,linha, fornecedor,itinerario , valor, id):
        db = DbConnection()
        try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = ( linha, fornecedor, itinerario , valor, id)
            #cursor.execute('SELECT nome, senha FROM ` `ezsys``.senha WHERE nome = %s AND senha = %s', valores)
            #cursor.execute('truncate table `ezsys`.woodpaper'
            updateString = "UPDATE `ezsys`.`dp_transportes` SET linha= '{}',  fornecedor= '{}', itinerario= '{}', valor= '{}'  WHERE id = {};".format(linha, fornecedor,itinerario , valor, id)
            cursor.execute(updateString)      
            con.commit()
            db.closeConn(cursor)    
            
        except Error as e :
               print(e)
               return     


    def selecionarTransporteLinha(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT linha FROM ezsys.dp_transportes WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario    


    def selecionarTransporteFornecedor(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT fornecedor FROM ezsys.dp_transportes WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario  


    def selecionarTransporteItinerario(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT itinerario FROM ezsys.dp_transportes WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario 
         
    def selecionarTransporteValor(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT valor FROM ezsys.dp_transportes WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario          

    def selecionarTabelaTransporte(self,id):
     db = DbConnection()
     user = None
     try:
        con = db.getConn()     
        cursor= con.cursor(dictionary=True)
        valores = (id)
        # con = mysql.connector.connect(host='127.0.0.1', user='root', database='eztestes',password='q9w8e7#MTB')
        select="SELECT * FROM `ezsys`.dp_transportes WHERE `id` = {};".format(valores)
        #data,solicitacao_assunto,solicitacao_texto,solicitacao_status,solicitacao_incluido,solicitacao_editado   
        cursor.execute(select)
        ver = cursor.fetchone()                       
        db.closeConn(cursor)    
        return ver
     except Error as e :
            print(e)
            return user 




#______________________________________________________________OCORRENCIAS

    def ConsultarOcorrencia(self):
     db = DbConnection()
     try:
          con = db.getConn()     
          cursor = con.cursor()
          cursor.execute("SELECT id, funcionario , dataocorrencia, codocorr, descocorr, discrimina FROM `ezsys`.dp_ocorrencias")
          resultados = cursor.fetchall()
          db.closeConn(cursor)    
          return resultados
     except Exception as e:
          print(f"Erro ao consultar ocorrências: {str(e)}")
          raise e
         
         
    def selecionarTabelaOcorrencia(self,id):
     db = DbConnection()
     user = None
     try:
        con = db.getConn()     
        cursor= con.cursor(dictionary=True)
        valores = (id)
        # con = mysql.connector.connect(host='127.0.0.1', user='root', database='eztestes',password='q9w8e7#MTB')
        select="SELECT * FROM `ezsys`.dp_ocorrencias WHERE `id` = {};".format(valores)
        #data,solicitacao_assunto,solicitacao_texto,solicitacao_status,solicitacao_incluido,solicitacao_editado   
        cursor.execute(select)
        ver = cursor.fetchone()                       
        db.closeConn(cursor)    
        return ver
     except Error as e :
            print(e)
            return user          


    def ConsultarOcorrenciaTabelaFuncionario(self):
     db = DbConnection()
     user = None
     try:
        con = db.getConn()     
        cursor= con.cursor()
        valores = ()
        # con = mysql.connector.connect(host='127.0.0.1', user='root', database='eztestes',password='q9w8e7#MTB')
        cursor.execute("SELECT id, dataocorrencia, codocorr, descocorr, discrimina FROM `ezsys`.dp_ocorrencias"),valores
        ver = cursor.fetchall()
        print(ver)
    
        db.closeConn(cursor)    
        return ver
     except Error as e :
            print(e)
            return user  
#_____________________________________________________________________Imagem BD____________________________________________________________________________
    def selecionarimagem(self):
     db = DbConnection()
     user = None
     try:
        con = db.getConn()     
        cursor= con.cursor()
        valores = (id)
        # con = mysql.connector.connect(host='127.0.0.1', user='root', database='eztestes',password='q9w8e7#MTB')
        select="SELECT logomarca FROM ezsys.`cad_empresa` WHERE `id` = 1;".format(valores)
        #data,solicitacao_assunto,solicitacao_texto,solicitacao_status,solicitacao_incluido,solicitacao_editado   
        cursor.execute(select)
        ver = cursor.fetchone()                       
        db.closeConn(cursor)    
        return ver
     except Error as e :
            print(e)
            return user 
#__________________________________________________________Controle de Ponto_____________________________________________________________
    def ConsultarFolhadePonto(self):
     db = DbConnection()
     user = None
     try:
        con = db.getConn()     
        cursor= con.cursor()
        valores = ()
        # con = mysql.connector.connect(host='127.0.0.1', user='root', database='eztestes',password='q9w8e7#MTB')
        cursor.execute("SELECT id,`codigo`,`funcionario`, `data`, `hrentr`, `interv2entr`, `interv2said`,`hrsaid`,`interventr`,`intervsaid`,`tempo_intervalo`,`tothoras`,`justificativa`,`observacoes` FROM `ezsys`.dp_folhaponto ORDER BY `data` ASC"),valores
        ver = cursor.fetchall()
        db.closeConn(cursor)    
        return ver
     except Error as e :
            print(e)
            return user          
       
    def ConsultarFolhadePontoPorStatusOK(self):
     db = DbConnection()
     user = None
     try:
        con = db.getConn()     
        cursor= con.cursor()
        valores = ()
        # con = mysql.connector.connect(host='127.0.0.1', user='root', database='eztestes',password='q9w8e7#MTB')
        cursor.execute("SELECT id,`codigo`,`funcionario`, `data`, `hrentr`, `interv2entr`, `interv2said`,`hrsaid`,`interventr`,`intervsaid`,`tempo_intervalo`,`tothoras`,`justificativa`,`observacoes` FROM `ezsys`.dp_folhaponto WHERE justificativa = 'Ok'",valores)
        ver = cursor.fetchall()
        db.closeConn(cursor)    
        return ver
     except Error as e :
            print(e)
            return user       
   
    def ConsultarFolhadePontoPorStatusTratar(self):
     db = DbConnection()
     user = None
     try:
        con = db.getConn()     
        cursor= con.cursor()
        valores = ()
        # con = mysql.connector.connect(host='127.0.0.1', user='root', database='eztestes',password='q9w8e7#MTB')
        cursor.execute("SELECT id,`codigo`,`funcionario`, `data`, `hrentr`, `interv2entr`, `interv2said`,`hrsaid`,`interventr`,`intervsaid`,`tempo_intervalo`,`tothoras`,`justificativa`,`observacoes` FROM `ezsys`.dp_folhaponto WHERE justificativa = 'Tratar'",valores)
        ver = cursor.fetchall()
        db.closeConn(cursor)    
        return ver
     except Error as e :
            print(e)
            return user       
       
    def ConsultarFolhadePontoPorHoraextra(self):
     db = DbConnection()
     user = None
     try:
        con = db.getConn()     
        cursor= con.cursor()
        valores = ()
        # con = mysql.connector.connect(host='127.0.0.1', user='root', database='eztestes',password='q9w8e7#MTB')
        cursor.execute("SELECT id,`codigo`,`funcionario`, `data`, `hrentr`, `interv2entr`, `interv2said`,`hrsaid`,`interventr`,`intervsaid`,`tempo_intervalo`,`tothoras`,`justificativa`,`observacoes` FROM `ezsys`.dp_folhaponto WHERE `interventr` >= '00:01' AND `intervsaid` >= '00:01'", valores)
        ver = cursor.fetchall()
        print(ver)
    
        db.closeConn(cursor)    
        return ver
     except Error as e :
            print(e)
            return user           
       
    def ConsultarFolhadePontoSemHoraextra(self):
     db = DbConnection()
     user = None
     try:
        con = db.getConn()     
        cursor= con.cursor()
        valores = ()
        # con = mysql.connector.connect(host='127.0.0.1', user='root', database='eztestes',password='q9w8e7#MTB')
        cursor.execute("SELECT id,`codigo`,`funcionario`, `data`, `hrentr`, `interv2entr`, `interv2said`,`hrsaid`,`interventr`,`intervsaid`,`tempo_intervalo`,`tothoras`,`justificativa`,`observacoes` FROM `ezsys`.dp_folhaponto WHERE `interventr` <= '00:00' AND `intervsaid` <= '00:00'", valores)
        ver = cursor.fetchall()
        print(ver)
    
        db.closeConn(cursor)    
        return ver
     except Error as e :
            print(e)
            return user                    
             

    def ConsultarFolhadePontoPorFuncionario(self,Funcionario):
     db = DbConnection()
     user = None
     try:
        con = db.getConn()     
        cursor= con.cursor()
        valores = (Funcionario)
        # con = mysql.connector.connect(host='127.0.0.1', user='root', database='eztestes',password='q9w8e7#MTB')
        cursor.execute("SELECT id,`codigo`,`funcionario`, `data`, `hrentr`, `interv2entr`, `interv2said`,`hrsaid`,`interventr`,`intervsaid`,`tempo_intervalo`,`tothoras`,`justificativa`,`observacoes` FROM ezsys.dp_folhaponto WHERE funcionario = %s", (Funcionario,))
        ver = cursor.fetchall()
        db.closeConn(cursor)    
        return ver
     except Error as e :
            print(e)
            return user           
          
    def ConsultarFolhadePontoPorFuncionariEData(self, datainicial, datafinal, funcionario):
       db = DbConnection()
       try:
          con = db.getConn()     
          cursor= con.cursor()
          valores = (datainicial, datafinal, funcionario)
          cursor.execute("SELECT id,`codigo`,`funcionario`, `data`, `hrentr`, `interv2entr`, `interv2said`,`hrsaid`,`interventr`,`intervsaid`,`tempo_intervalo`,`tothoras`,`justificativa`,`observacoes` FROM ezsys.dp_folhaponto WHERE `data` BETWEEN %s AND %s AND funcionario = %s", valores)
          ver = cursor.fetchall()
          print(ver)
          db.closeConn(cursor)
          return ver
       except Error as e:
          print(e)
          return None         
     
    def ConsultarFolhadePontoPordataTratarNome(self,datainicial,datafinal,nome):
     db = DbConnection()
     user = None
     try:
        con = db.getConn()     
        cursor= con.cursor()
        valores = (datainicial,datafinal,nome)
        # con = mysql.connector.connect(host='127.0.0.1', user='root', database='eztestes',password='q9w8e7#MTB')
        cursor.execute("SELECT id,`codigo`,`funcionario`, `data`, `hrentr`, `interv2entr`, `interv2said`,`hrsaid`,`interventr`,`intervsaid`,`tempo_intervalo`,`tothoras`,`justificativa`,`observacoes`FROM `ezsys`.dp_folhaponto WHERE `data` BETWEEN %s AND %s AND funcionario = %s AND justificativa = 'Tratar'", valores)
        ver = cursor.fetchall()
        print(ver)
    
        db.closeConn(cursor)    
        return ver
     except Error as e :
            print(e)
            return user         
       
       
       
       
    def ConsultarFolhadePontoPordataOkNome(self,datainicial,datafinal,nome):
     db = DbConnection()
     user = None
     try:
        con = db.getConn()     
        cursor= con.cursor()
        valores = (datainicial,datafinal,nome)
        # con = mysql.connector.connect(host='127.0.0.1', user='root', database='eztestes',password='q9w8e7#MTB')
        cursor.execute("SELECT id,`codigo`,`funcionario`, `data`, `hrentr`, `interv2entr`, `interv2said`,`hrsaid`,`interventr`,`intervsaid`,`tempo_intervalo`,`tothoras`,`justificativa`,`observacoes` FROM `ezsys`.dp_folhaponto WHERE `data` BETWEEN %s AND %s AND funcionario = %s AND justificativa = 'Ok'", valores)
        ver = cursor.fetchall()
        print(ver)
    
        db.closeConn(cursor)    
        return ver
     except Error as e :
            print(e)
            return user      
       
    def ConsultarFolhadePontoPordataHoraextraNome(self,datainicial,datafinal,nome):
     db = DbConnection()
     user = None
     try:
        con = db.getConn()     
        cursor= con.cursor()
        valores = (datainicial,datafinal,nome)
        # con = mysql.connector.connect(host='127.0.0.1', user='root', database='eztestes',password='q9w8e7#MTB')
        cursor.execute("SELECT id, `codigo`, `funcionario`, `data`, `hrentr`, `hrsaid`, `interv2entr`, `interv2said`, `interventr`, `intervsaid`, `justificativa`, `observacoes` FROM `ezsys`.dp_folhaponto WHERE `data` BETWEEN %s AND %s AND funcionario = %s AND `interventr` != '' AND `intervsaid` != ''", valores)
        ver = cursor.fetchall()
        print(ver)
    
        db.closeConn(cursor)    
        return ver
     except Error as e :
            print(e)
            return user     
       
    def ConsultarFolhadePontoPordataSemHoraextraNome(self,datainicial,datafinal,nome):
     db = DbConnection()
     user = None
     try:
        con = db.getConn()     
        cursor= con.cursor()
        valores = (datainicial,datafinal,nome)
        # con = mysql.connector.connect(host='127.0.0.1', user='root', database='eztestes',password='q9w8e7#MTB')
        cursor.execute("SELECT id, `codigo`, `funcionario`, `data`, `hrentr`, `hrsaid`, `interv2entr`, `interv2said`, `interventr`, `intervsaid`, `justificativa`, `observacoes` FROM `ezsys`.dp_folhaponto WHERE `data` BETWEEN %s AND %s  AND funcionario = %s AND `interventr` = '' AND `intervsaid` = ''", valores)
        ver = cursor.fetchall()
        print(ver)
    
        db.closeConn(cursor)    
        return ver
     except Error as e :
            print(e)
            return user                    
       
    def selecionarPorFuncionario(self): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = ()
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT funcionario FROM ezsys.dp_folhaponto ORDER BY `funcionario` ASC")
            cursor.execute(select)  
            ver = cursor.fetchall()
            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario          
       
       
    def selecionarFuncionarioPorNome(self): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = ()
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT nome FROM ezsys.dp_funcionarios ORDER BY `nome` ASC")
            cursor.execute(select)  
            ver = cursor.fetchall()
            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario           
       
    def ConsultarFolhadePontoPordataTratar(self,datainicial,datafinal):
     db = DbConnection()
     user = None
     try:
        con = db.getConn()     
        cursor= con.cursor()
        valores = (datainicial,datafinal)
        # con = mysql.connector.connect(host='127.0.0.1', user='root', database='eztestes',password='q9w8e7#MTB')
        cursor.execute("SELECT id,`codigo`,`funcionario`, `data`, `hrentr`, `interv2entr`, `interv2said`,`hrsaid`,`interventr`,`intervsaid`,`tempo_intervalo`,`tothoras`,`justificativa`,`observacoes` FROM `ezsys`.dp_folhaponto WHERE `data` BETWEEN %s AND %s AND justificativa = 'Tratar'", valores)
        ver = cursor.fetchall()
        print(ver)
    
        db.closeConn(cursor)    
        return ver
     except Error as e :
            print(e)
            return user           
       
    def ConsultarFolhadePontoPordataOk(self,datainicial,datafinal):
     db = DbConnection()
     user = None
     try:
        con = db.getConn()     
        cursor= con.cursor()
        valores = (datainicial,datafinal)
        # con = mysql.connector.connect(host='127.0.0.1', user='root', database='eztestes',password='q9w8e7#MTB')
        cursor.execute("SELECT id,`codigo`,`funcionario`, `data`, `hrentr`, `interv2entr`, `interv2said`,`hrsaid`,`interventr`,`intervsaid`,`tempo_intervalo`,`tothoras`,`justificativa`,`observacoes` FROM `ezsys`.dp_folhaponto WHERE `data` BETWEEN %s AND %s AND justificativa = 'Ok'", valores)
        ver = cursor.fetchall()
        print(ver)
    
        db.closeConn(cursor)    
        return ver
     except Error as e :
            print(e)
            return user      
       
    def ConsultarFolhadePontoPordataHoraextra(self,datainicial,datafinal):
     db = DbConnection()
     user = None
     try:
        con = db.getConn()     
        cursor= con.cursor()
        valores = (datainicial,datafinal)
        # con = mysql.connector.connect(host='127.0.0.1', user='root', database='eztestes',password='q9w8e7#MTB')
        cursor.execute("SELECT id,`codigo`,`funcionario`, `data`, `hrentr`, `interv2entr`, `interv2said`,`hrsaid`,`interventr`,`intervsaid`,`tempo_intervalo`,`tothoras`,`justificativa`,`observacoes` FROM `ezsys`.dp_folhaponto WHERE `data` BETWEEN %s AND %s AND `interventr` != '' AND `intervsaid` != ''", valores)
        ver = cursor.fetchall()
        print(ver)
    
        db.closeConn(cursor)    
        return ver
     except Error as e :
            print(e)
            return user                      
  
    def ConsultarFolhadePontoPordataSemHoraextra(self, datainicial, datafinal):
     db = DbConnection()
     try:
          con = db.getConn()     
          cursor = con.cursor()
          valores = (datainicial, datafinal)
          cursor.execute("SELECT id, `codigo`, `funcionario`, `data`, `hrentr`, `interv2entr`, `interv2said`, `hrsaid`, `interventr`, `intervsaid`, `tempo_intervalo`, `tothoras`, `justificativa`, `observacoes` FROM `ezsys`.dp_folhaponto WHERE `data` BETWEEN %s AND %s AND `interventr` <= '00:00' AND `intervsaid` <= '00:00'", valores)
          ver = cursor.fetchall()
          print(ver)

          db.closeConn(cursor)
          return ver
     except Error as e:
          print(e)
          return None
  
  
    def ConsultarFolhadePontoPordata(self,datainicial,datafinal):
     db = DbConnection()
     user = None
     try:
        con = db.getConn()     
        cursor= con.cursor()
        valores = (datainicial,datafinal)
        # con = mysql.connector.connect(host='127.0.0.1', user='root', database='eztestes',password='q9w8e7#MTB')
        cursor.execute("SELECT id,`codigo`,`funcionario`, `data`, `hrentr`, `interv2entr`, `interv2said`,`hrsaid`,`interventr`,`intervsaid`,`tempo_intervalo`,`tothoras`,`justificativa`,`observacoes` FROM `ezsys`.dp_folhaponto WHERE `data` BETWEEN %s AND %s", valores)
        ver = cursor.fetchall()
        print(ver)
    
        db.closeConn(cursor)    
        return ver
     except Error as e :
            print(e)
            return user      
  
  
    def InserirControledeponto(self,data,codigo_funcionario, funcionario,horarioEntrada,horarioSaida,entradaAlmoco,saidaAlmoco,entradaIntervalo,saidaIntervalo,status,observacao,imagem):
      db= DbConnection()
      try:
        con = db.getConn() 
        Cursor = con.cursor()
        queryString = """INSERT INTO ezsys.dp_folhaponto (`data`,codigo,`funcionario`, `hrentr`, `hrsaid`, `interv2entr`, `interv2said`, `interventr`, `intervsaid`,`justificativa`,`observacoes`,`img_caminho`) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        values = (data,codigo_funcionario, funcionario,horarioEntrada,horarioSaida,entradaAlmoco,saidaAlmoco,entradaIntervalo,saidaIntervalo,status,observacao,imagem)
        Cursor.execute(queryString, values)
        con.commit()
        print(Cursor.rowcount,'Registros inseridos na tabela')
        Cursor.close()
      except Error as erro:
       print('Falha ao inserir dados no Mysql: {}'.format(erro))
      finally:
        try:
            if(con.is_connected()):
             con.close()
            Cursor.close()
        except Error as erro:
         print(erro) 


    def InserirControledepontoImportacao(self,codigo,funcionario,data,horarioEntrada,horarioSaida,entradaAlmoco,saidaAlmoco,entradaIntervalo,saidaIntervalo,status,observacao):
      db= DbConnection()
      try:
        con = db.getConn() 
        Cursor = con.cursor()
        queryString = """INSERT INTO ezsys.dp_folhaponto (`codigo`,`funcionario`,`data`, `hrentr`, `hrsaid`, `interv2entr`, `interv2said`, `interventr`, `intervsaid`,`justificativa`,`observacoes`) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        values = (codigo,funcionario,data,horarioEntrada,horarioSaida,entradaAlmoco,saidaAlmoco,entradaIntervalo,saidaIntervalo,status,observacao)
        Cursor.execute(queryString, values)
        con.commit()
        print(Cursor.rowcount,'Registros inseridos na tabela')
        Cursor.close()
      except Error as erro:
       print('Falha ao inserir dados no Mysql: {}'.format(erro))
      finally:
        try:
            if(con.is_connected()):
             con.close()
            Cursor.close()
        except Error as erro:
         print(erro) 

    def SelecionarIdFolhadePonto(self,id):
     db = DbConnection()
     user = None
     try:
        con = db.getConn()     
        cursor= con.cursor(dictionary=True)
        valores = (id)
        # con = mysql.connector.connect(host='127.0.0.1', user='root', database='eztestes',password='q9w8e7#MTB')
        select="SELECT * FROM `ezsys`.dp_folhaponto WHERE `id` = {};".format(valores)
        #data,solicitacao_assunto,solicitacao_texto,solicitacao_status,solicitacao_incluido,solicitacao_editado   
        cursor.execute(select)
        ver = cursor.fetchone()                       
        db.closeConn(cursor)    
        return ver
     except Error as e :
            print(e)
            return user 

    def EditarFolhadePonto(self, data,codigo, funcionario, horarioEntrada, horarioSaida, entradaAlmoco, saidaAlmoco, entradaIntervalo, saidaIntervalo, status, observacao, imagem, id):
     db = DbConnection()
     try:
          con = db.getConn()
          cursor = con.cursor(dictionary=True)
          updateString = "UPDATE `ezsys`.`dp_folhaponto` SET data=%s, codigo=%s, funcionario=%s, hrentr=%s, hrsaid=%s, interv2entr=%s, interv2said=%s, interventr=%s, intervsaid=%s, justificativa=%s, observacoes=%s, img_caminho=%s WHERE id=%s"
          values = (data,codigo, funcionario, horarioEntrada, horarioSaida, entradaAlmoco, saidaAlmoco, entradaIntervalo, saidaIntervalo, status, observacao, imagem, id)
          cursor.execute(updateString, values)
          print(values)
          con.commit()
          db.closeConn(cursor)
     except Error as e:
          print(e)
          return

    def SelecionarFolhadePontoData(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = '{}' AND senha = %s', valores)
            select=("SELECT data FROM ezsys.dp_folhaponto WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario  
       
    def SelecionarFolhadePontoFuncionario(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT funcionario FROM ezsys.dp_folhaponto WHERE `id` = {} order by nome asc;".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario        

    def SelecionarFolhadePontoHorEntrada(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT hrentr FROM ezsys.dp_folhaponto WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario 
       
    def SelecionarFolhadePontoHorSaida(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT hrsaid FROM ezsys.dp_folhaponto WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario      
       
    def SelecionarFolhadePontoInterHorEntrada(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT interv2entr FROM ezsys.dp_folhaponto WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario           
          
    def SelecionarFolhadePontoInterHorSaida(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT interv2said FROM ezsys.dp_folhaponto WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario           

    def SelecionarFolhadePontoHorEntradaEx(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT interventr FROM ezsys.dp_folhaponto WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario 
       
    def SelecionarFolhadePontoHorSaidaExt(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT intervsaid FROM ezsys.dp_folhaponto WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario  
       
    def SelecionarFolhadePontoTotHoras(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT tothoras FROM ezsys.dp_folhaponto WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario     
       
    def selecionarFuncionarioJustificativa(self, texto): 
     db = DbConnection()
               
     try:
          con = db.getConn()
          cursor = con.cursor()
          select = "SELECT justificativa FROM ezsys.dp_folhaponto WHERE id = {}".format(texto)
          cursor.execute(select)  
          justificativa = cursor.fetchone()[0]
          db.closeConn(cursor)    
          return justificativa
     except Error as e:
          print(e)
          return None
       
    def SelecionarFolhadePontoObservacao(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT observacoes FROM ezsys.dp_folhaponto WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario           
       
    def SelecionarFolhadePontoImagem(self, id): 
     db = DbConnection()
          
     try:
          con = db.getConn()
          cursor = con.cursor()
          select = "SELECT img_caminho FROM ezsys.dp_folhaponto WHERE id = %s"
          cursor.execute(select, (id,))
          resultado = cursor.fetchone()
          db.closeConn(cursor)
          if resultado is not None:
               return resultado[0]
          else:
               return None
     except Error as e:
          print(e)
          return None   
       
    def DeletarFolhaDePonto(self,usuario):   
     db = DbConnection()
     try:
        con = db.getConn()     
        cursor= con.cursor(dictionary = True)
        valores = (usuario)
        sql = "DELETE FROM `ezsys`.`dp_folhaponto` WHERE id= {};".format(valores)
        cursor.execute(sql)
        con.commit()
        db.closeConn(cursor)  
        print(cursor.rowcount, "registro excluído")  
        return True
     except Error as e :
          print(e)
          return False             
#____________________________________________________________Folha de pagamento_________________________________________________________________________
    def ConsultarFolhadePAgamento(self):
     db = DbConnection()
     user = None
     try:
        con = db.getConn()     
        cursor= con.cursor()
        valores = ()
        # con = mysql.connector.connect(host='127.0.0.1', user='root', database='eztestes',password='q9w8e7#MTB')
        cursor.execute("SELECT id, `bonus`,`codigo`,`credito`,`datafin`,`dataini`,`desconto`,`formapgt`,`funcionario`,`insalubr`,`liquido`,`percpremio`,`premio`,`repousorem`,`saidacodigo`,`salbase`,`salfam`,`statpremio`,`totextra`,`totinss` FROM `ezsys`.folhapagto"),valores
        ver = cursor.fetchall()
        print(ver)
    
        db.closeConn(cursor)    
        return ver
     except Error as e :
            print(e)
            return user   
       
    def selecionarFuncionario(self): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = ()
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT codigo, nome FROM ezsys.dp_funcionarios where ativo = '1' ORDER BY `nome` ASC")
            cursor.execute(select)  
            ver = cursor.fetchall()
            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario      
       
    def selecionarFuncionarioNomes(self): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = ()
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `id`,`codigo`, `nome` FROM `ezsys`.dp_funcionarios  ORDER BY `nome` ASC")
            cursor.execute(select)  
            ver = cursor.fetchall()
            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario         
       
    def selecionarFuncionarioNomesAtivo(self): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = ()
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `id`,`codigo`, `nome` FROM `ezsys`.dp_funcionarios where ativo = '1' ORDER BY `nome` ASC")
            cursor.execute(select)  
            ver = cursor.fetchall()
            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario        
       
    def selecionarFuncionarioNomesInativo(self): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = ()
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT `id`,`codigo`, `nome` FROM `ezsys`.dp_funcionarios where ativo = '2' ORDER BY `nome` ASC")
            cursor.execute(select)  
            ver = cursor.fetchall()
            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario          
       
    def selecionarUsuarioPorNomeeid(self, nome):
     db = DbConnection()
     try:
          con = db.getConn()     
          cursor = con.cursor()
          query = 'SELECT `id`,`codigo`, `nome` FROM `ezsys`.dp_funcionarios  WHERE LOWER(`nome`)  LIKE LOWER(%s) ORDER BY `nome` ASC'
          cursor.execute(query, ('%'+nome+'%',))
          resultados = cursor.fetchall()
          print(resultados)
          return [dict(zip(['id','codigo', 'nome'], r)) for r in resultados]
     except Error as e:
          print(e)
          return None         
       
    def selecionarFuncionarioporID(self, texto):
     db = DbConnection()
     try:
          con = db.getConn()
          cursor = con.cursor(dictionary=True)
          valores = (texto,)
          select = "SELECT `funcionario` FROM ezsys.dp_folhaponto WHERE `id` = %s;"
          cursor.execute(select, valores)
          resultado = cursor.fetchone()
          if resultado is None:
               return None
          else:
               return resultado['funcionario']
     except Error as e:
          print(e)
     finally:
          db.closeConn(cursor)    
          
          
    def selecionarFuncionarioporIDOcorrencia(self, texto):
     db = DbConnection()
     try:
          con = db.getConn()
          cursor = con.cursor(dictionary=True)
          valores = (texto,)
          select = "SELECT `funcionario` FROM ezsys.dp_ocorrencias WHERE `id` = %s;"
          cursor.execute(select, valores)
          resultado = cursor.fetchone()
          if resultado is None:
               return None
          else:
               return resultado['funcionario']
     except Error as e:
          print(e)
     finally:
          db.closeConn(cursor)            
          
#______________________________________________________________________________HORA EXTRA______________________________________________________________________________________________
    def ConsultarHoraExtra(self):
     db = DbConnection()
     user = None
     try:
        con = db.getConn()     
        cursor= con.cursor()
        valores = ()
        # con = mysql.connector.connect(host='127.0.0.1', user='root', database='eztestes',password='q9w8e7#MTB')
        cursor.execute("SELECT id, `data`,codigo,`funcionario`,`he_entrada`, `he_saida`, `intervalo`,`justificativa`,`observacoes`  FROM `ezsys`.dp_horaextra ORDER BY `data` ASC"),valores
        ver = cursor.fetchall()
        db.closeConn(cursor)    
        return ver
     except Error as e :
            print(e)   
            
    def ConsultarHoraExtrasOK(self):
     db = DbConnection()
     user = None
     try:
        con = db.getConn()     
        cursor= con.cursor()
        valores = ()
        # con = mysql.connector.connect(host='127.0.0.1', user='root', database='eztestes',password='q9w8e7#MTB')
        cursor.execute("SELECT id, `data`,codigo,`funcionario`,`he_entrada`, `he_saida`, `intervalo`,`justificativa`,`observacoes`  FROM `ezsys`.dp_horaextra WHERE justificativa = 'Ok'",valores)
        ver = cursor.fetchall()
        db.closeConn(cursor)    
        return ver
     except Error as e :
            print(e)
            return user       
   
    def ConsultarHoraExtraStatusTratar(self):
     db = DbConnection()
     user = None
     try:
        con = db.getConn()     
        cursor= con.cursor()
        valores = ()
        # con = mysql.connector.connect(host='127.0.0.1', user='root', database='eztestes',password='q9w8e7#MTB')
        cursor.execute("SELECT id, `data`,codigo,`funcionario`,`he_entrada`, `he_saida`, `intervalo`,`justificativa`,`observacoes`  FROM `ezsys`.dp_horaextra WHERE justificativa = 'Tratar'",valores)
        ver = cursor.fetchall()
        db.closeConn(cursor)    
        return ver
     except Error as e :
            print(e)
            return user  
       
    def ConsultarHoraExtraPordata(self,datainicial,datafinal):
     db = DbConnection()
     user = None
     try:
        con = db.getConn()     
        cursor= con.cursor()
        valores = (datainicial,datafinal)
        # con = mysql.connector.connect(host='127.0.0.1', user='root', database='eztestes',password='q9w8e7#MTB')
        cursor.execute("SELECT id, `data`,codigo,`funcionario`,`he_entrada`, `he_saida`, `intervalo`,`justificativa`,`observacoes`  FROM `ezsys`.dp_horaextra WHERE `data` BETWEEN %s AND %s", valores)
        ver = cursor.fetchall()
        print(ver)
    
        db.closeConn(cursor)    
        return ver
     except Error as e :
            print(e)
            return user      
                      
    def ConsultarHoraExtraPordataTratar(self,datainicial,datafinal):
     db = DbConnection()
     user = None
     try:
        con = db.getConn()     
        cursor= con.cursor()
        valores = (datainicial,datafinal)
        # con = mysql.connector.connect(host='127.0.0.1', user='root', database='eztestes',password='q9w8e7#MTB')
        cursor.execute("SELECT id, `data`,codigo,`funcionario`,`he_entrada`, `he_saida`, `intervalo`,`justificativa`,`observacoes`  FROM `ezsys`.dp_horaextra WHERE `data` BETWEEN %s AND %s AND justificativa = 'Tratar'", valores)
        ver = cursor.fetchall()
        print(ver)
    
        db.closeConn(cursor)    
        return ver
     except Error as e :
            print(e)
            return user           
       
    def ConsultarHoraExtraPordataOk(self,datainicial,datafinal):
     db = DbConnection()
     user = None
     try:
        con = db.getConn()     
        cursor= con.cursor()
        valores = (datainicial,datafinal)
        # con = mysql.connector.connect(host='127.0.0.1', user='root', database='eztestes',password='q9w8e7#MTB')
        cursor.execute("SELECT id, `data`,codigo,`funcionario`,`he_entrada`, `he_saida`, `intervalo`,`justificativa`,`observacoes`  FROM `ezsys`.dp_horaextra WHERE `data` BETWEEN %s AND %s AND justificativa = 'Ok'", valores)
        ver = cursor.fetchall()
        print(ver)
    
        db.closeConn(cursor)    
        return ver
     except Error as e :
            print(e)
            return user      

    def SelecionarIdHoraExtra(self,id):
     db = DbConnection()
     user = None
     try:
        con = db.getConn()     
        cursor= con.cursor(dictionary=True)
        valores = (id)
        # con = mysql.connector.connect(host='127.0.0.1', user='root', database='eztestes',password='q9w8e7#MTB')
        select="SELECT * FROM `ezsys`.dp_horaextra WHERE `id` = {};".format(valores)
        #data,solicitacao_assunto,solicitacao_texto,solicitacao_status,solicitacao_incluido,solicitacao_editado   
        cursor.execute(select)
        ver = cursor.fetchone()                       
        db.closeConn(cursor)    
        return ver
     except Error as e :
            print(e)
            return user 

    def SelecionarHoraExtraData(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = '{}' AND senha = %s', valores)
            select=("SELECT data FROM ezsys.dp_horaextra WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario         
       
    def SelecionarHoraExtraEntrada(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT he_entrada FROM ezsys.dp_horaextra WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario 
       
    def SelecionarHoraExtraSaida(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT he_saida FROM ezsys.dp_horaextra WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario            
       
    def SelecionarTempoIntervalo(self, texto): 
       db = DbConnection()
        
       usuario = None
       try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (texto)
            #cursor.execute('SELECT nome, senha FROM ``ez-sys``.senha WHERE nome = %s AND senha = %s', valores)
            select=("SELECT intervalo FROM ezsys.dp_horaextra WHERE `id` = {};".format(valores))
            cursor.execute(select)  
            ver = cursor.fetchone()

            db.closeConn(cursor)    
            return ver
       except Error as e :
            print(e)
            return usuario                   
   
    def selecionarFuncionarioporIDHoraExtra(self, texto):
     db = DbConnection()
     try:
          con = db.getConn()
          cursor = con.cursor(dictionary=True)
          valores = (texto,)
          select = "SELECT `funcionario` FROM ezsys.dp_horaextra WHERE `id` = %s;"
          cursor.execute(select, valores)
          resultado = cursor.fetchone()
          if resultado is None:
               return None
          else:
               return resultado['funcionario']
     except Error as e:
          print(e)
     finally:
          db.closeConn(cursor)     
   
    def InserirHoraExtra(self,data,codigo_funcionario, funcionario,entradaIntervalo,saidaIntervalo,intervalo,status,observacao,imagem):
      db= DbConnection()
      try:
        con = db.getConn() 
        Cursor = con.cursor()
        queryString = """INSERT INTO ezsys.dp_horaextra (`data`,`codigo`,`funcionario`, `he_entrada`, `he_saida`, `intervalo`,`justificativa`,`observacoes`,`img_caminho`) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        values = (data,codigo_funcionario, funcionario,entradaIntervalo,saidaIntervalo,intervalo,status,observacao,imagem)
        Cursor.execute(queryString, values)
        con.commit()
        print(Cursor.rowcount,'Registros inseridos na tabela')
        Cursor.close()
      except Error as erro:
       print('Falha ao inserir dados no Mysql: {}'.format(erro))
      finally:
        try:
            if(con.is_connected()):
             con.close()
            Cursor.close()
        except Error as erro:
         print(erro) 
           
    def EditarHoraExtra(self, data,codigo_funcionario, funcionario,entradaIntervalo,saidaIntervalo,intervalo,status,observacao,imagem, id):
     db = DbConnection()
     try:
          con = db.getConn()
          cursor = con.cursor(dictionary=True)
          updateString = "UPDATE `ezsys`.`dp_horaextra` SET data=%s, codigo=%s, funcionario=%s, he_entrada=%s, he_saida=%s, intervalo=%s, justificativa=%s, observacoes=%s, img_caminho=%s WHERE id=%s"
          values = (data,codigo_funcionario, funcionario,entradaIntervalo,saidaIntervalo,intervalo,status,observacao,imagem, id)
          cursor.execute(updateString, values)
          print(values)
          con.commit()
          db.closeConn(cursor)
     except Error as e:
          print(e)
          return          
     
     
    def selecionarHoraExtraJustificativa(self, texto): 
     db = DbConnection()
               
     try:
          con = db.getConn()
          cursor = con.cursor()
          select = "SELECT justificativa FROM ezsys.`dp_horaextra` WHERE id = {}".format(texto)
          cursor.execute(select)  
          justificativa = cursor.fetchone()[0]
          db.closeConn(cursor)    
          return justificativa
     except Error as e:
          print(e)
          return None
       
    def SelecionarHoraExtraObservacao(self, textoLabel): 
      db = DbConnection()
      try:
        con = db.getConn()
        cursor = con.cursor(dictionary=True)
        valores = (textoLabel)
        select=("SELECT observacoes FROM `ezsys`.dp_horaextra WHERE id = {};".format(valores))
        cursor.execute(select)  
        ver = cursor.fetchone()
        db.closeConn(cursor)    
        return ver
      except Error as e:
        print(e)
        return None         
       
    def SelecionarHoraExtraImagem(self, id): 
     db = DbConnection()
          
     try:
          con = db.getConn()
          cursor = con.cursor()
          select = "SELECT img_caminho FROM ezsys.`dp_horaextra` WHERE id = %s"
          cursor.execute(select, (id,))
          resultado = cursor.fetchone()
          db.closeConn(cursor)
          if resultado is not None:
               return resultado[0]
          else:
               return None
     except Error as e:
          print(e)
          return None   
       
    def DeletarHoraExtra(self,usuario):   
     db = DbConnection()
     try:
        con = db.getConn()     
        cursor= con.cursor(dictionary = True)
        valores = (usuario)
        sql = "DELETE FROM `ezsys`.`dp_horaextra` WHERE id= {};".format(valores)
        cursor.execute(sql)
        con.commit()
        db.closeConn(cursor)  
        print(cursor.rowcount, "registro excluído")  
        return True
     except Error as e :
          print(e)
          return False                  

    def InserirHoraExtraPorSenha(self,data, funcionario,entradaIntervalo,saidaIntervalo):
      db= DbConnection()
      try:
        con = db.getConn() 
        Cursor = con.cursor()
        queryString = """INSERT INTO ezsys.dp_horaextra (`data`,`codigo`,`funcionario`, `he_entrada`, `he_saida`, `intervalo`,`justificativa`,`observacoes`,`img_caminho`) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        values = (data, funcionario,entradaIntervalo,saidaIntervalo)
        Cursor.execute(queryString, values)
        con.commit()
        print(Cursor.rowcount,'Registros inseridos na tabela')
        Cursor.close()
      except Error as erro:
       print('Falha ao inserir dados no Mysql: {}'.format(erro))
      finally:
        try:
            if(con.is_connected()):
             con.close()
            Cursor.close()
        except Error as erro:
         print(erro) 

#___________________________________________________________________________Relogio de ponto___________________________________________________________________________________________
   
   
    def ConsultarRelogiodePonto(self):
     db = DbConnection()
     user = None
     try:
        con = db.getConn()     
        cursor= con.cursor()
        valores = ()
        # con = mysql.connector.connect(host='127.0.0.1', user='root', database='eztestes',password='q9w8e7#MTB')
        cursor.execute("SELECT `id`,`codigo`,`tipo`, `data`, `hora`, `pis` FROM `ezsys`.dp_relogioponto ORDER BY `data` ASC"),valores
        ver = cursor.fetchall()
        db.closeConn(cursor)    
        return ver
     except Error as e :
            print(e)     
            
            
    def ConsultarRelogiodePontoordata(self,datainicial,datafinal):
     db = DbConnection()
     user = None
     try:
        con = db.getConn()     
        cursor= con.cursor()
        valores = (datainicial,datafinal)
        # con = mysql.connector.connect(host='127.0.0.1', user='root', database='eztestes',password='q9w8e7#MTB')
        cursor.execute("SELECT `id`, `codigo`,`tipo`, `data`, `hora`, `pis` FROM `ezsys`.dp_relogioponto WHERE `data` BETWEEN %s AND %s", valores)
        ver = cursor.fetchall()
        print(ver)
    
        db.closeConn(cursor)    
        return ver
     except Error as e :
            print(e)                 
                    
                    
    def InserirRelogiodePontoImportacao(self, cod, tipo, data, hora, pis):
          db = DbConnection()
          try:
               con = db.getConn()
               cursor = con.cursor()
               queryString = """INSERT INTO ezsys.dp_relogioponto (`codigo`, `tipo`, `data`, `hora`, `pis`) VALUES (%s, %s, %s, %s, %s)"""
               values = (cod, tipo, data, hora, pis)
               cursor.execute(queryString, values)
               con.commit()
               print(cursor.rowcount, 'Registros inseridos na tabela')
               cursor.close()
          except Error as erro:
               print('Falha ao inserir dados no MySQL: {}'.format(erro))
          finally:
               try:
                    if con.is_connected():
                         con.close()
                    cursor.close()
               except Error as erro:              
                print(erro)       
pass    