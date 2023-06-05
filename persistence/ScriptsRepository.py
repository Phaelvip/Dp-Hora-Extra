import mysql.connector
from mysql.connector import Error
from persistence.DbConnecion import DbConnection

class ScriptsRepository:



    def BuscaValordecusto(self, dtInicial, dtFinal, despesa, competencia):
      db = DbConnection()
      usuario = None
      try:
        con = db.getConn()
        cursor = con.cursor(dictionary = True)
        valores = (dtInicial, dtFinal, despesa, competencia)
        cursor.execute("create table   `"+db.getDbName()+"`.ccustos2 (valor varchar(10) , porcento varchar(10) , total varchar(10) );")
        cursor.execute("insert into   `"+db.getDbName()+"`.ccustos2 (valor, porcento) SELECT e.valor, p.porcento  FROM   `"+db.getDbName()+"`.saida AS e  INNER JOIN   `"+db.getDbName()+"`.saicusto AS p ON e.codigo = p.codigo  where e.data >= %s and  e.data <= %s and e.desp = %s and p.custo = %s; ", valores)
        cursor.execute("update   `"+db.getDbName()+"`.ccustos2 set total = (valor/100*porcento); ")
        cursor.execute("select round(sum(total),2) as  resultado from   `"+db.getDbName()+"`.ccustos2; ")
        
        ver = cursor.fetchone()
        print(ver)
        cursor.execute("drop table `"+db.getDbName()+"`.ccustos2;")
        db.closeConn(cursor)    
        return ver
      except Error as e :
        print(e)
        return usuario
      
        pass  
    
    def BuscarValorPorCustoCompete(self, periododeCompetenciaInicial ,periododeCompetenciafinal, competencia, custo):
      db = DbConnection()
      usuario = None
      try:
        con = db.getConn()
        cursor = con.cursor(dictionary = True)
        valores = (periododeCompetenciaInicial ,periododeCompetenciafinal,  competencia, custo)
        cursor.execute("create table  `"+db.getDbName()+"`.ccustos2 (valor varchar(10) , porcento varchar(10) , total varchar(10) );")
        cursor.execute(" insert into `"+db.getDbName()+"`.ccustos2 (valor, porcento) SELECT e.valor, p.porcento FROM `"+db.getDbName()+"`.saida AS e INNER JOIN `"+db.getDbName()+"`.saicusto AS p ON e.codigo = p.codigo where e.compete >= %s and e.compete <= %s  and e.desp = %s and p.custo = %s;", valores)
        cursor.execute("update  `"+db.getDbName()+"`.ccustos2 set total = (valor/100*porcento); ")
        cursor.execute("select round(sum(total),2) as resultado from  `"+db.getDbName()+"`.ccustos2; ")
        
        ver = cursor.fetchone()
        print(ver)
        cursor.execute("drop table `"+db.getDbName()+"`.ccustos2;")
        db.closeConn(cursor)    
        return ver
      except Error as e :
        print(e)
        return usuario
        
      
    def BuscarValorPorCustoCompeteSemCusto(self, periododeCompetenciaInicial ,periododeCompetenciafinal, custo):
      db = DbConnection()
      usuario = None
      try:
        con = db.getConn()
        cursor = con.cursor(dictionary = True)
        valores = (periododeCompetenciaInicial ,periododeCompetenciafinal,  custo)
        cursor.execute("create table  `"+db.getDbName()+"`.ccustos2 (valor varchar(10) , porcento varchar(10) , total varchar(10) );")
        cursor.execute(" insert into `"+db.getDbName()+"`.ccustos2 (valor, porcento) SELECT e.valor, p.porcento FROM `"+db.getDbName()+"`.saida AS e INNER JOIN `"+db.getDbName()+"`.saicusto AS p ON e.codigo = p.codigo where e.compete >= %s and e.compete <= %s  and p.custo = %s;", valores)
        cursor.execute("update   `"+db.getDbName()+"`.ccustos2 set total = (valor/100*porcento); ")
        cursor.execute("select round(sum(total),2) as resultado from  `"+db.getDbName()+"`.ccustos2; ")
        
        ver = cursor.fetchone()
        print(ver)
        cursor.execute("drop table `"+db.getDbName()+"`.ccustos2;")
        db.closeConn(cursor)    
        return ver
      except Error as e :
        print(e)
        return usuario
    
      
      
      
    def BuscarValorPorCustoData(self, dtInicial, dtFinal, custo):
      db = DbConnection()
      usuario = None
      try:
        con = db.getConn()
        cursor = con.cursor(dictionary = True)
        valores = (dtInicial, dtFinal, custo)
        cursor.execute("create table   `"+db.getDbName()+"`.ccustos2 (valor varchar(10) , porcento varchar(10) , total varchar(10) );")
        cursor.execute("insert into `"+db.getDbName()+"`.ccustos2 (valor, porcento) SELECT e.valor, p.porcento FROM `"+db.getDbName()+"`.saida AS e INNER JOIN `"+db.getDbName()+"`.saicusto AS p ON e.codigo = p.codigo where e.data >= %s and e.data <= %s and p.custo = %s;", valores)
        cursor.execute("update   `"+db.getDbName()+"`.ccustos2 set total = (valor/100*porcento); ")
        cursor.execute("select round(sum(total),2) as resultado from  `"+db.getDbName()+"`.ccustos2; ")
        
        ver = cursor.fetchone()
        print(ver)
        cursor.execute("drop table `"+db.getDbName()+"`.ccustos2;")
        db.closeConn(cursor)    
        return ver
      except Error as e :
        print(e)
        return usuario
        pass   
pass




        