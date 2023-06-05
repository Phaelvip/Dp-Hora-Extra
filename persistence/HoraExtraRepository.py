import mysql.connector
from mysql.connector import Error
from persistence.DbConnecion import DbConnection
from  tkinter import  messagebox
from  entity.Usuario import Usuario

from datetime import date, datetime
   
   
class HoraExtraRepository:   
    
    #ENUM
    ENTRADA = "ENTRADA"
    SAIDA = "SAIDA"
         
    def inserirEntrada(self, hora_atual, data_Entrada, idUsuario, usuarioLogado):
        db = DbConnection()
        try:
            con = db.getConn()
            cursor = con.cursor()
            cursor.execute("SELECT * FROM ezsys.dp_horaextra WHERE data=%s AND funcionario_id=%s", (data_Entrada, idUsuario))
            registro = cursor.fetchone()
            if registro:
                messagebox.showerror('Erro', 'Já existe um registro de hora extra para este dia.')
            else:
                query = "INSERT INTO ezsys.dp_horaextra (`he_entrada`,`data`, `funcionario_id`,`funcionario`) VALUES (%s, %s, %s, %s);"
                values = ( hora_atual, data_Entrada, idUsuario, usuarioLogado)
                cursor.execute(query, values)
                con.commit()
                print(cursor.rowcount, "registro(s) inserido(s)")
        except mysql.connector.Error as error:
            print("Falha ao inserir registro de hora extra na tabela dp_horaextra: {}".format(error))
        finally:
            if (con.is_connected()):
                cursor.close()
                con.close()
                print("Conexão ao MySQL foi encerrada")

    def atualizarSaida(self,  hora_atual,data,  idUsuario):
        db = DbConnection()
        try:
            con = db.getConn()
            cursor = con.cursor()
            query = "UPDATE ezsys.dp_horaextra SET `he_saida` = %s WHERE `data`=%s AND `funcionario_id` = %s"
            values = ( hora_atual,data,  idUsuario)
            cursor.execute(query, values)
            con.commit()
            print(cursor.rowcount, "registro(s) atualizado(s)")
        except mysql.connector.Error as error:
            print("Falha ao atualizar saída na tabela dp_horaextra: {}".format(error))
        finally:
            if (con.is_connected()):
                cursor.close()
                con.close()
                print("Conexão ao MySQL foi encerrada")
    def obterValorEntrada(self, senha):
        # PEGAR APENAS O VALOR DA ENTRADA PELO LOGIN
        db = DbConnection()
        try:
            con = db.getConn()
            cursor = con.cursor()
            data_atual = datetime.today().strftime('%Y-%m-%d')
            cursor.execute('SELECT he_entrada FROM ezsys.dp_horaextra WHERE funcionario_id = %s AND data = %s', (senha, data_atual))
            valor_entrada = cursor.fetchone()
            db.closeConn(cursor)
            if valor_entrada:
                return valor_entrada[0]
            else:
                return None
        except Error as e:
            print(e)
            return None
        
    def obterValorSaida(self, senha):
        # PEGAR APENAS O VALOR DA ENTRADA PELO LOGIN
        db = DbConnection()
        try:
            con = db.getConn()
            cursor = con.cursor()
            data_atual = datetime.today().strftime('%Y-%m-%d')
            cursor.execute('SELECT he_saida FROM ezsys.dp_horaextra WHERE funcionario_id = %s AND data = %s', (senha, data_atual))
            registro = cursor.fetchone()
            db.closeConn(cursor)
            if registro == None:
                return None
            else:
                return registro[0]

        except Error as e:
            print(e)
            return None 
        
        
        
    def obterValor(self, data_Entrada, usuarioLogado):
        #PEGAR APENAS O VALOR DA ENTRADA PELO LOGIN
        #con = mysql.connector.connect(host='127.0.0.1', user='root', database='ezsys',password='q9w8e7#MTB')
        db = DbConnection()
        usuario = None
        try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (data_Entrada, usuarioLogado)
            cursor.execute('SELECT `data`, `funcionario`, he_entrada, he_saida FROM  ezsys.dp_horaextra  WHERE funcionario_id = %s', valores)
            ver = cursor.fetchone()
            db.closeConn(cursor)    
            return ver
        except Error as e :
            print(e)
            return usuario          
        
    def obtervalordehoradetrabalho(self, senha):
        # PEGAR APENAS O VALOR DA ENTRADA PELO LOGIN
        db = DbConnection()
        try:
            con = db.getConn()
            cursor = con.cursor()
            data_atual = datetime.today().strftime('%Y-%m-%d')
            cursor.execute('SELECT hrdiautil1, hrdiautil2 FROM ezsys.dp_horaextra WHERE id = %s AND data = %s', (senha, data_atual))
            registro = cursor.fetchone()
            db.closeConn(cursor)
            if registro == None:
                return None
            else:
                return registro[0]

        except Error as e:
            print(e)
            return None 
   
    def criartempodeTolerancia(self,id,nome,data):
        db = DbConnection()
        try:
            values = (id,nome,data)
            con = db.getConn()
            cursor = con.cursor()
            #cursor.execute("UPDATE ezsys.dp_horaextra_autoriza t INNER JOIN ezsys.dp_funcionarios f ON t.funcionario = f.usuario_sistema SET t.codigo = f.codigo;")        
            cursor.execute("drop table if exists ezsys.dp_horaextra_tolera;")
            cursor.execute("create table ezsys.dp_horaextra_tolera (id int primary key not null, nome varchar (100),codigo int, data date ,aut varchar(1), hr_atual time, hr_solicit time, tolera time, tolera_inicio time as (timediff(hr_solicit,tolera)), tolera_fim time as (SEC_TO_TIME(TIME_TO_SEC(hr_solicit) + TIME_TO_SEC(tolera))));")      
            insert=cursor.execute("insert into ezsys.dp_horaextra_tolera (id, nome, data) values (%s, %s, %s);", values)                 
            con.commit()
            print(cursor.rowcount, "registro(s) atualizado(s)")
        except mysql.connector.Error as error:
            print("Falha ao atualizar saída na tabela dp_horaextra: {}".format(error))
        finally:
            if (con.is_connected()):
                cursor.close()
                con.close()
                print("Conexão ao MySQL foi encerrada")            
        
        
 
    def obtervalordetempodetolerancia(self):
        db = DbConnection()
        try:

            con = db.getConn()
            cursor = con.cursor()
            #cursor.execute("UPDATE ezsys.dp_horaextra_autoriza t INNER JOIN ezsys.dp_funcionarios f ON t.funcionario = f.usuario_sistema SET t.codigo = f.codigo;")         
            cursor.execute("UPDATE dp_horaextra_tolera t INNER JOIN ezsys.dp_funcionarios f ON t.nome = f.usuario_sistema SET t.codigo = f.codigo;")  
            cursor.execute("UPDATE dp_horaextra_tolera t INNER JOIN ezsys.dp_funcionarios f ON t.nome = f.usuario_sistema SET t.nome = f.nome ;")                     
            cursor.execute("UPDATE dp_horaextra_tolera AS tb1 INNER JOIN dp_horaextra_autoriza AS tb2 ON tb1.nome = tb2.funcionario and tb1.data = tb2.data_he SET tb1.hr_solicit = tb2.hora where tb2.entrasai='E';") 
            ver=cursor.execute("UPDATE dp_horaextra_tolera AS tb1 INNER JOIN dp_horaextra_autoriza AS tb2 set tb1.aut = tb2.aut; ;")               
            cursor.execute("UPDATE dp_horaextra_tolera AS tb1 INNER JOIN config_dept AS tb2 SET tb1.tolera = tb2.tempo_tolerancia ;")      
            con.commit()
            print(cursor.rowcount, "registro(s) atualizado(s)",ver)
        except mysql.connector.Error as error:
            print("Falha ao atualizar saída na tabela dp_horaextra: {}".format(error))
        finally:
            if (con.is_connected()):
                cursor.close()
                con.close()
                print("Conexão ao MySQL foi encerrada")            

    def obtervalordeautorizado(self, nome,data):
        db = DbConnection()
        try:
            con = db.getConn()
            cursor = con.cursor()
            cursor.execute("UPDATE dp_horaextra_tolera t INNER JOIN ezsys.dp_funcionarios f ON t.nome = f.usuario_sistema SET t.nome = f.nome ;")   
            cursor.execute('SELECT aut FROM ezsys.dp_horaextra_tolera WHERE nome = %s AND data = %s',(nome,data))
            ver = cursor.fetchone()
            print(ver)
            db.closeConn(cursor)    
            return ver
        except Error as e :
            print(e)
            return              
   
    def SelecionartempodeTolerancia(self):
        db = DbConnection()
        try:
            con = db.getConn()
            cursor = con.cursor()
            cursor.execute('SELECT hr_atual FROM ezsys.configdept WHERE nome = "1"')
            ver = cursor.fetchone()
            print(ver)
            db.closeConn(cursor)    
            return ver
        except Error as e :
            print(e)
            return               
         
        
    def atualizardados(self):
        db = DbConnection()
        try:
            con = db.getConn()
            cursor = con.cursor()
            cursor.execute("UPDATE ezsys.dp_horaextra t INNER JOIN ezsys.dp_funcionarios f ON t.funcionario = f.usuario_sistema SET t.codigo = f.codigo;")        
            cursor.execute("UPDATE ezsys.dp_horaextra t INNER JOIN ezsys.dp_funcionarios f ON t.funcionario = f.usuario_sistema SET t.funcionario = f.nome ;")      
            values = ()
            con.commit()
            print(cursor.rowcount, "registro(s) atualizado(s)")
        except mysql.connector.Error as error:
            print("Falha ao atualizar saída na tabela dp_horaextra: {}".format(error))
        finally:
            if (con.is_connected()):
                cursor.close()
                con.close()
                print("Conexão ao MySQL foi encerrada")        
                                 
pass