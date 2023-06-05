from persistence.DepartamentoRepository import DepartamentoRepository
from datetime import *
from  datetime import datetime
from mysql.connector import Error
import  locale  


class DepartamentoService:
    def __init__(self):
        self.__DepartamentoDao = DepartamentoRepository()    
        locale.setlocale(locale.LC_ALL,'pt_BR')
        locale.setlocale(locale.LC_MONETARY,'pt_BR.UTF-8')



#____________________________________________________FUNCIONARIOS__________________________________________________________________________

    def ConsultarFuncionarios(self):#,usuario,senha,email,nome):  #def configPastaPadrao(self, idQueEuPassaria):
      resultados=self.__DepartamentoDao.consultarFuncionarios()
      return  resultados    
    
    
    def selecionarUsuarioPorNome(self,nome):
      if nome == "":
          return self.__DepartamentoDao.consultarFuncionarios()
      else:
          return self.__DepartamentoDao.selecionarUsuarioPorNome(nome)      
   
    
    def selecionarNaTabelaFuncionarios(self,id): 
       selecionar= self.__DepartamentoDao.selecionarNaTabelaFuncionarios(id)
       return selecionar      
  
    def DeletarFuncionarios(self,usuario): 
          usuarios=self.__DepartamentoDao.DeletarFuncionarios(usuario)            
          return usuarios  
                
    def selecionarFuncionariosNome(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioNome(textoLabel)
      if(resultado['nome'] == None):
            return ""    
    
      return resultado             
               
    def selecionarFuncionariosCodigo(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioCodigo(textoLabel)
      if(resultado['codigo'] == None):
            return ""    
    
      return resultado                     
        
    def selecionarFuncionarioNomeCompleto(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioNomeCompleto(textoLabel)
      if(resultado['nomecompleto'] == None):
            return ""    
    
      return resultado              
        
    def selecionarFuncionarioTelefone(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioTelefone(textoLabel)
      if(resultado['telefone2'] == None):
        return ""    
    
      return resultado                      
        
    def selecionarFuncionarioCelular(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioCelular(textoLabel)
      if(resultado['celular'] == None):
            return ""    
    
      return resultado      
    
    def selecionarFuncionarioEmail(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioEmail(textoLabel)
      if(resultado['email'] == None):
            return ""    
    
      return resultado                 
        
    def selecionarFuncionarioNacionalidade(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioNacionalidade(textoLabel)
      if(resultado['nacionalidade'] == None):
            return ""    
    
      return resultado              
  
  
  
    def selecionarFuncionarioNascimento(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioNascimento(textoLabel)
      if(resultado['nasc'] == None):
            return ""    
      return datetime.strftime(resultado['nasc'],'%d/%m/%Y')   
    
    def selecionarFuncionarioLogradouro(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioLogradouro(textoLabel)
      if(resultado['ENDER_TIPOLOGR'] == None):
            return ""    
    
      return resultado['ENDER_TIPOLOGR']             

    def selecionarFuncionarioEndereco(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioEndereco(textoLabel)
      if(resultado['endereco'] == None):
            return ""    
    
      return resultado             
                
    def selecionarFuncionarioNumero(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioNumero(textoLabel)
      if(resultado['ENDER_NUMERO'] == None):
            return ""    
    
      return resultado           
        
    def selecionarFuncionarioComplemento(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioComplemento(textoLabel)
      if(resultado['ENDER_COMPLEM'] == None):
            return ""    
    
      return resultado                 

    def selecionarFuncionarioBairro(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioBairro(textoLabel)
      if(resultado['bairro'] == None):
            return ""    
    
      return resultado    

    def selecionarFuncionarioCidade(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioCidade(textoLabel)
      if(resultado['cidade'] == None):
            return ""    
    
      return resultado             


    def selecionarFuncionarioEstado(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioEstado(textoLabel)
      if(resultado['estado'] == None):
            return ""    
    
      return resultado             

    def selecionarFuncionarioCep(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioCep(textoLabel)
      if(resultado['cep'] == None):
            return ""    
    
      return resultado    
    
    
    def selecionarFuncionarioPais(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioPais(textoLabel)
      if(resultado['pais'] == None):
            return ""    
    
      return resultado        


    def selecionarFuncionarioCPF(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioCPF(textoLabel)
      if(resultado['cgccpf'] == None):
            return ""    
    
      return resultado      
    
    
    def selecionarFuncionarioIdentidade(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioIdentidade(textoLabel)
      if(resultado['insc'] == None):
            return ""    
    
      return resultado          


    def selecionarFuncionarioEscolaridade(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioEscolaridade(textoLabel)
      if(resultado['escolaridade'] == None):
            return ""    
    
      return resultado    


    def selecionarFuncionarioEstadoCivil(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioEstadoCivil(textoLabel)
      if(resultado['estcivil'] == None):
            return ""    
    
      return resultado    


    def selecionarFuncionarioRamo(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioRamo(textoLabel)
      if(resultado['ramo'] == None):
            return ""    
    
      return resultado          
    
    
    def selecionarFuncionarioFuncao(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioFuncao(textoLabel)
      if(resultado['funcao'] == None):
            return ""    
    
      return resultado          
    
    def selecionarFuncionariocodsetor(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionariocodsetor(textoLabel)
      if(resultado['codsetor'] == None):
            return ""    
    
      return resultado           
    
    def selecionarFuncionarioCarteiraDeTrabalho(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioCarteiraDeTrabalho(textoLabel)
      if(resultado['carttrab'] == None):
            return ""    
    
      return resultado        
    
    
    def selecionarFuncionarioCarteiraDeReservista(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioCarteiraDeReservista(textoLabel)
      if(resultado['certreserv'] == None):
            return ""    
    
      return resultado    
    
    
    def selecionarFuncionarioTipoFuncionario(self,textoLabel):
      resultados= self.__DepartamentoDao.selecionarFuncionarioTipoFuncionario(textoLabel)
      retorno = []
      for resultado in resultados:
             retorno.append(resultado['tipofuncio'])
    
            
      return retorno[0]
    
    def selecionarFuncionarioStatus(self,textoLabel):
      resultados= self.__DepartamentoDao.selecionarFuncionarioStatus(textoLabel)
      retorno = []
      for resultado in resultados:
             retorno.append(resultado['ativo'])
    
            
      return retorno[0]    

    
    def selecionarFuncionarioTituloDeEleitor(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioTituloDeEleitor(textoLabel)
      if(resultado['titeleitor'] == None):
            return ""    
    
      return resultado              


    def selecionarFuncionarioNomeDoPai(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioNomeDoPai(textoLabel)
      if(resultado['nomepai'] == None):
            return ""    
    
      return resultado 

    def selecionarFuncionarioNomeDoMae(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioNomeDoMae(textoLabel)
      if(resultado['nomemae'] == None):
            return ""    
    
      return resultado 

    def selecionarFuncionarioPis(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioPis(textoLabel)
      if(resultado['numpis'] == None):
            return ""    
    
      return resultado 
    
    
    def ConsultaFuncionarioPis(self, pis):
      resultado = self.__DepartamentoDao.ConsultarFuncionarioPis(pis)
      if resultado is None:
          return False
      for item in resultado:
          if item['numpis'] == pis:
              return True
      return False

    def selecionarFuncionarioObservacao1(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioObservacao1(textoLabel)
      if(resultado['obs1'] == None):
            return ""    
    
      return resultado 

    def selecionarFuncionarioObservacao2(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioObservacao2(textoLabel)
      if(resultado['obs2'] == None):
            return ""    
    
      return resultado 
    
    def selecionarFuncionarioRamalInterno(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioRamalInterno(textoLabel)
      if(resultado['ramalinterno'] == None):
            return ""    
    
      return resultado 
    
    def selecionarFuncionarioUsuario(self):
      resultado= self.__DepartamentoDao.selecionarFuncionarioUsuario()
      return resultado     
 
    def selecionarFuncionarioUsuarioporID(self, texto):
      resultado = self.__DepartamentoDao.selecionarFuncionarioUsuarioporID(texto)
      if resultado is not None:
          return resultado
      else:
          return "Usuário não encontrado"
 
 
  #Fazer com Sobrecarga
 
    def inserirFuncionarios(self, nome, codigo, nomecompleto, telefone2, celular, email, nacionalidade, nascimento, tipo, endereco, numero, complemento, bairro, cidade, estado, cep, pais, cpf, identidade, escolaridade, estadocivil, cargo, funcao, setor, carteiradetrabalho, carteiradereservista, statusradio, setoradio, titeleitor, nomepai, nomemae, pis, obs1, obs2, ramal, usuarioSistema):
      self.__DepartamentoDao.inserirFuncionarios(nome, codigo, nomecompleto, telefone2, celular, email, nacionalidade, datetime.strptime(nascimento, '%d/%m/%Y').strftime('%Y-%m-%d'), tipo, endereco, numero, complemento, bairro, cidade, estado, cep, pais, cpf, identidade, escolaridade, estadocivil, cargo, funcao, setor, carteiradetrabalho, carteiradereservista, statusradio, setoradio, titeleitor, nomepai, nomemae, pis, obs1, obs2, ramal, usuarioSistema)

            
    def EditarFuncionarios(self, nome,codigo,nomecompleto,telefone2,celular,email,nacionalidade,tipo,endereço,numero,complemento,bairro,cidade,estado,cep,pais,cpf,identidade,escolaridade,estadocivil,cargo,funcao,setor,carteiradetrabalho,carteiradereservista,setoradio,titeleitor,nomepai,nomemae,statusradio,obs1,obs2,ramal,usuarioSistema,id):
            self.__DepartamentoDao.EditarFuncionarios( nome,codigo,nomecompleto,telefone2,celular,email,nacionalidade,tipo,endereço,numero,complemento,bairro,cidade,estado,cep,pais,cpf,identidade,escolaridade,estadocivil,cargo,funcao,setor,carteiradetrabalho,carteiradereservista,setoradio,titeleitor,nomepai,nomemae,statusradio,obs1,obs2,ramal,usuarioSistema,id)  
    

            

#__________________________________________________________Salario Funcionário_____________________________________________________________________________________________
    def selecionarFuncionarioSalarioBase(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioSalarioBase(textoLabel)
      if(resultado['salbase'] == None):
            return  ""       
    
      return resultado 
    
    def selecionarFuncionarioInss(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioInss(textoLabel)
      if(resultado['percinss'] == None):
            return  ""     
    
      return resultado  
     
    def selecionarFuncionarioSalarioFuncao(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioSalarioFuncao(textoLabel)
      if(resultado['salfuncao'] == None):
            return  ""        
      
      return resultado        

    def selecionarFuncionarioSalarioLiquido(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioSalarioLiquido(textoLabel)
      if(resultado['salliquido'] == None):
            return  ""       
      
      return resultado    
    
    def selecionarSalarioDivideBH(self,textoLabel):
      resultados= self.__DepartamentoDao.selecionarSalarioDivideBH(textoLabel)
      retorno = []
      for resultado in resultados:
             retorno.append(resultado['sal_dividebh'])
      
      return retorno[0]     
    
    def selecionarFuncionarioDecTerceiro(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioDecTerceiro(textoLabel)
      if(resultado['sal_12decterc'] == None):
            return  ""       
      
      return resultado          
    
    def selecionarFuncionarioComissaoPremio(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioComissaoPremio(textoLabel)
      if(resultado['sal_comiprem'] == None):
            return  ""       
      
      return resultado    
    
    def selecionarFuncionarioRecebeComissao(self,textoLabel):
      resultados= self.__DepartamentoDao.selecionarFuncionarioRecebeComissao(textoLabel)
      retorno = []
      for resultado in resultados:
             retorno.append(resultado['sal_recebeprem'])
      
      return retorno[0] 
                
    def selecionarFuncionarioFerias(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioFerias(textoLabel)
      if(resultado['sal_12ferias'] == None):
            return  ""       
      
      return resultado          
    
    def selecionarFuncionarioInsalubridade(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioInsalubridade(textoLabel)
      if(resultado['sal_insalubr'] == None):
            return  ""       
      
      return resultado     
    
    def selecionarFuncionarioFgts(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioFgts(textoLabel)
      if(resultado['percfgts'] == None):
            return ""      
    
      return resultado       
    
    def selecionarFuncionarioValeTranspDiario(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioValeTranspDiario(textoLabel)
      if(resultado['valetrp'] == None):
            return  ""       
    
      return resultado             
    
    def selecionarFuncionarioMaxValeTransp(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioMaxValeTransp(textoLabel)
      if(resultado['percmaxvaletrp'] == None):
            return  ""  
      
      return resultado                
          
    def selecionarFuncionarioSalSeguro(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioSalSeguro(textoLabel)
      if(resultado['sal_seguro'] == None):
            return  ""                 
    
      return resultado   
    
    def selecionarFuncionarioSalCesta(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioSalCesta(textoLabel)
      if(resultado['sal_cesta'] == None):
            return  ""                 
    
      return resultado           
    
    def selecionarFuncionarioSalGremio(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioSalGremio(textoLabel)
      if(resultado['sal_gremio'] == None):
            return  ""                 
    
      return resultado          

    def selecionarFuncionarioParticipacaoLucros(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioParticipacaoLucros(textoLabel)
      if(resultado['sal_partlucr'] == None):
            return  ""       
    
      return resultado     
    
    def selecionarFuncionarioPensaoAlimenticia(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioPensaoAlimenticia(textoLabel)
      if(resultado['sal_pensaoalim'] == None):
            return  ""                 
    
      return resultado        
    
    def selecionarFuncionarioValeAlimentacao(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioValeAlimentacao(textoLabel)
      if(resultado['sal_valealiment'] == None):
            return  ""                 
    
      return resultado     
    
    def selecionarFuncionarioAssMedica(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioAssMedica(textoLabel)
      if(resultado['sal_assmedica'] == None):
            return  ""                 
    
      return resultado             
    
    def selecionarFuncionarioHora50porc(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioHora50porc(textoLabel)
      if(resultado['sal_hrextra50'] == None):
            return  ""                 
    
      return resultado           
        
    def selecionarFuncionarioHora100porc(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioHora100porc(textoLabel)
      if(resultado['sal_hrextra100'] == None):
            return  ""                 
    
      return resultado                 
    
    def selecionarFuncionarioHora100porc(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioHora100porc(textoLabel)
      if(resultado['sal_hrextra100'] == None):
            return  ""                 
    
      return resultado         
    
    def selecionarFuncionarioSalFamilia(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioSalFamilia(textoLabel)
      if(resultado['sal_familia'] == None):
            return  ""                 
    
      return resultado       
    
    def selecionarFuncionarioFGTSDecimoTerceiro(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioFGTSDecimoTerceiro(textoLabel)
      if(resultado['sal_fgts12decterc'] == None):
            return  ""                 
    
      return resultado         
    
    def selecionarFuncionarioFGTSFerias(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioFGTSFerias(textoLabel)
      if(resultado['sal_fgts12ferias'] == None):
            return  ""                 
    
      return resultado            
     
    def selecionarFuncionarioCafe(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioCafe(textoLabel)
      if(resultado['sal_cafe'] == None):
            return  ""                 
    
      return resultado     
    
    def selecionarFuncionarioUniforme(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioUniforme(textoLabel)
      if(resultado['sal_uniforme'] == None):
            return  ""                 
    
      return resultado      
    
    def selecionarFuncionarioRepouso(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioRepouso(textoLabel)
      if(resultado['sal_repsemremun'] == None):
            return  ""                 
    
      return resultado              
       
    def selecionarFuncionarioHorarioEntradaDiasUteis(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioHorarioEntradaDiasUteis(textoLabel)
      if(resultado['hrdiautil1'] == None):
            return  ""                 
    
      return resultado  
    
    def selecionarFuncionarioHorarioSaidaDiasUteis(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioHorarioSaidaDiasUteis(textoLabel)
      if(resultado['hrdiautil2'] == None):
            return  ""                 
    
      return resultado      
              
    def selecionarFuncionarioIntervaloSaida(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioIntervaloSaida(textoLabel)
      if(resultado['hrintervalo1'] == None):
            return  ""                 
    
      return resultado   
    
    def selecionarFuncionarioIntervaloEntrada(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioIntervaloEntrada(textoLabel)
      if(resultado['hrintervalo2'] == None):
            return  ""                 
    
      return resultado      
    
    def selecionarFuncionarioTotalSalario(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioTotalSalario(textoLabel)
      if(resultado['sal_totsal'] == None):
            return float(0.00)                  
    
      return resultado 
    
    def selecionarFuncionarioTotalBeneficios(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioTotalBeneficios(textoLabel)
      if(resultado['sal_totbenef'] == None):
            return float(0.00)               
    
      return resultado 
    
    def selecionarFuncionarioTotalCustoMes(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioTotalCustoMes(textoLabel)
      if(resultado['sal_customes'] == None):
            return  float(0.00)                
    
      return resultado 
    
    def selecionarFuncionarioTotalCustoDiario(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioTotalCustoDiario(textoLabel)
      if(resultado['sal_custodia'] == None):
            return float(0.00)              
    
      return resultado 
    
    def selecionarFuncionarioTotalCustoHora(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncionarioTotalCustoHora(textoLabel)
      if(resultado['sal_custohr'] == None):
            return  float(0.00)           
    
      return resultado                                    
  
    def EditarSalarioFuncionarios(self,salarioBase,inssFuncionario,salFuncaoFuncionario,salLiquidoFuncionario,decTerceiroFuncionario,comissaoFuncionario,feriarFuncionario,premiacaoFUncionario,Salinsalubridade,fgtsFuncionario,valTranspFuncionario,maxValeTranspFuncionario,seguroFuncionario,cestaFuncionario
                                                                 ,gremioFuncionario,pensaoAlimFuncionario,partLucrosFuncionario,horasExt50Funcionario,horasExt100Funcionario,salFamilFuncionario,fgtsParcFuncionario,fgtsFeriasFUncionario,cafeFuncionario,uniformeFuncionario,repousoFuncionario,diasUteisEntrada,diasUteisSaida,
                                                                 intervaloEntrada,intervaloSaida,totSalario,totBeneficio,custMensal,custDiario,custHora,valeAlimentacao,assMedica,dividebh,id):
       self.__DepartamentoDao.EditarSalarioFuncionarios(salarioBase,inssFuncionario,salFuncaoFuncionario,salLiquidoFuncionario,decTerceiroFuncionario,comissaoFuncionario,feriarFuncionario,premiacaoFUncionario,Salinsalubridade,fgtsFuncionario,valTranspFuncionario,maxValeTranspFuncionario,seguroFuncionario,cestaFuncionario
                                                                 ,gremioFuncionario,pensaoAlimFuncionario,partLucrosFuncionario,horasExt50Funcionario,horasExt100Funcionario,salFamilFuncionario,fgtsParcFuncionario,fgtsFeriasFUncionario,cafeFuncionario,uniformeFuncionario,repousoFuncionario,diasUteisEntrada,diasUteisSaida,
                                                                 intervaloEntrada,intervaloSaida,totSalario,totBeneficio,custMensal,custDiario,custHora,valeAlimentacao,assMedica,dividebh,id)
   
   
    def InserirSalarioFuncionarios(self,salarioBase,inssFuncionario,salFuncaoFuncionario,salLiquidoFuncionario,decTerceiroFuncionario,comissaoFuncionario,feriarFuncionario,premiacaoFUncionario,Salinsalubridade,fgtsFuncionario,valTranspFuncionario,maxValeTranspFuncionario,seguroFuncionario,cestaFuncionario
                                                                 ,gremioFuncionario,pensaoAlimFuncionario,partLucrosFuncionario,horasExt50Funcionario,horasExt100Funcionario,salFamilFuncionario,fgtsParcFuncionario,fgtsFeriasFUncionario,cafeFuncionario,uniformeFuncionario,repousoFuncionario,diasUteisEntrada,diasUteisSaida,
                                                                 intervaloEntrada,intervaloSaida,totSalario,totBeneficio,custMensal,custDiario,custHora):
       self.__DepartamentoDao.inserirSalarioFuncionarios(salarioBase,inssFuncionario,salFuncaoFuncionario,salLiquidoFuncionario,decTerceiroFuncionario,comissaoFuncionario,feriarFuncionario,premiacaoFUncionario,Salinsalubridade,fgtsFuncionario,valTranspFuncionario,maxValeTranspFuncionario,seguroFuncionario,cestaFuncionario
                                                                 ,gremioFuncionario,pensaoAlimFuncionario,partLucrosFuncionario,horasExt50Funcionario,horasExt100Funcionario,salFamilFuncionario,fgtsParcFuncionario,fgtsFeriasFUncionario,cafeFuncionario,uniformeFuncionario,repousoFuncionario,diasUteisEntrada,diasUteisSaida,
                                                                 intervaloEntrada,intervaloSaida,totSalario,totBeneficio,custMensal,custDiario,custHora)
       
       
  
    def InserirSalarioFuncionarios(self, salario): #passa o ID do funcionário Também
       self.__DepartamentoDao.inserirSalarioFuncionarios(salario)

    def consultarFuncionariosEmSalarios(self,id):#,usuario,senha,email,nome):  #def configPastaPadrao(self, idQueEuPassaria):
      resultados=self.__DepartamentoDao.consultarFuncionariosEmSalarios(id)
      return  resultados           

    def inserirFuncionariosEmsalario(self,nome,codigo,nomecompleto):
          
            self.__DepartamentoDao.inserirFuncionariosEmsalario(nome,codigo,nomecompleto) 
#_________________________________________________Comissionamento Funcionario__________________________________________________________________________________________________
    def selecionarComissaoInicial(self,id):
      resultado= self.__DepartamentoDao.selecionarComissaoInicial(id)   
      if(resultado['comi'] == None):
            return  ""       
    
      return resultado 
    
    def selecionarComissaoFinal(self,id):
      resultado= self.__DepartamentoDao.selecionarComissaoFinal(id)        
      if(resultado['come'] == None):
            return  ""       
    
      return resultado 
    
    def selecionarValordaCota(self,id):
      resultado= self.__DepartamentoDao.selecionarValordaCota(id)        
      if(resultado['valor'] == None):
            return  ""       
    
      return resultado 
    
    def selecionarComissaoAcimaTabela(self,id):
      resultado= self.__DepartamentoDao.selecionarComissaoAcimaTabela(id)        
      if(resultado['comiacima'] == None):
            return  ""       
    
      return resultado   
    
    def selecionarComissaoOverVenda(self,id):
      resultado= self.__DepartamentoDao.selecionarComissaoOverVenda(id)        
      if(resultado['comiover'] == None):
         return  ""       
    
      return resultado    
    
    def selecionarComissaoDiadePagamento1(self,id):
      resultado= self.__DepartamentoDao.selecionarComissaoDiadePagamento1(id)        
      if(resultado['pagadia'] == None):
            return  ""       
    
      return resultado 
    
    def selecionarComissaoPeriododePagamentoInicial1(self,id):
      resultado= self.__DepartamentoDao.selecionarComissaoPeriododePagamentoInicial1(id)        
      if(resultado['pgtocomiss1'] == None):
            return  ""       
      return resultado  
    
    def selecionarComissaoPeriododePagamentoFinal1(self,id):
      resultado= self.__DepartamentoDao.selecionarComissaoPeriododePagamentoFinal1(id)        
      if(resultado['pgtocomiss2'] == None):
            return  ""       
      return resultado  

    def selecionarComissaoDiadePagamento2(self,id):
      resultado= self.__DepartamentoDao.selecionarComissaoDiadePagamento2(id)        
      if(resultado['pagadia2'] == None):
            return  ""       
    
      return resultado 
    
    def selecionarComissaoPeriododePagamentoInicial2(self,id):
      resultado= self.__DepartamentoDao.selecionarComissaoPeriododePagamentoInicial2(id)        
      if(resultado['pgtocomiss3'] == None):
            return  ""       
    
      return resultado         
    
    def selecionarComissaoPeriododePagamentoFinal2(self,id):
      resultado= self.__DepartamentoDao.selecionarComissaoPeriododePagamentoFinal2(id)        
      if(resultado['pgtocomiss4'] == None):
            return  ""       
    
      return resultado   

    def selecionarComissaoaoFinalDaVenda(self,textoLabel):
      resultados= self.__DepartamentoDao.selecionarComissaoaoFinalDaVenda(textoLabel)
      retorno = []
      for resultado in resultados:
             retorno.append(resultado['geractpgvd'])
      
      return retorno[0] 
    
    def selecionarComissaoDobradaDomingoseFeriados(self,textoLabel):
      resultados= self.__DepartamentoDao.selecionarComissaoDobradaDomingoseFeriados(textoLabel)
      retorno = []
      for resultado in resultados:
             retorno.append(resultado['comidobr'])
      
      return retorno[0]     


    def selecionarComissaoParticipacaoEmVendas(self,id):
      resultado= self.__DepartamentoDao.selecionarComissaoParticipacaoEmVendas(id)        
      if(resultado['part'] == None):
            return  ""       
      return resultado 
    
    def selecionarComissaoTipodeParticipacaoEmVendas(self,textoLabel):
      resultados= self.__DepartamentoDao.selecionarComissaoTipodeParticipacaoEmVendas(textoLabel)
      retorno = []
      for resultado in resultados:
             retorno.append(resultado['tipopart'])
      
      return retorno[0]     
    
    def selecionarComissaoPagamentoVenda(self,id):
      resultado= self.__DepartamentoDao.selecionarComissaoPagamentoVenda(id)        
      if(resultado['pagcomi1'] == None):
            return  ""       
    
      return resultado     
    
    def selecionarComissaoPagamentoCliente(self,id):
      resultado= self.__DepartamentoDao.selecionarComissaoPagamentoCliente(id)        
      if(resultado['pagcomi2'] == None):
            return  ""       
    
      return resultado  
    
    def selecionarComissaoGerarPrevisaoPagamento(self,textoLabel):
      resultados= self.__DepartamentoDao.selecionarComissaoGerarPrevisaoPagamento(textoLabel)
      retorno = []
      for resultado in resultados:
             retorno.append(resultado['geraprevpagcomi'])
      
      return retorno[0]        

    def selecionarComissaoPrimeiroRecebimentoVenda(self,textoLabel):
      resultados= self.__DepartamentoDao.selecionarComissaoPrimeiroRecebimentoVenda(textoLabel)
      retorno = []
      for resultado in resultados:
             retorno.append(resultado['geracomiprimreceb'])
      
      return retorno[0]    

    def selecionarAbaterImpostosparaCalculoComissao(self,textoLabel):
      resultados= self.__DepartamentoDao.selecionarAbaterImpostosparaCalculoComissao(textoLabel)
      retorno = []
      for resultado in resultados:
             retorno.append(resultado['tpcomiimpost'])
      
      return retorno[0]    

    def selecionarImpostodeRendaParaCalculoComissao(self,id):
          
      resultado= self.__DepartamentoDao.selecionarImpostodeRendaParaCalculoComissao(id)        
      if(resultado['irsobrecom'] == None):
            return  ""       
    
      return resultado  
    
    def EditarComissaoFuncionarios(self,comissaoInicial,comissaoFinal,valorCota,comissaoAcima,comissaoOver,periodoComissao1,periodoComissao2,pagamentoDia1,periodoComissao3,periodoComissao4,pagamentodia2,gerarConta,comissaoDobrada,
                                   participacaoVenda,tipoparticipacao,pagamentoComissao,pagamentoRecebimento,gerarPrevisao,abaterImposto,impostoDeRenda,gerarComissao,id):
       self.__DepartamentoDao.EditarComissaoFuncionarios(comissaoInicial,comissaoFinal,valorCota,comissaoAcima,comissaoOver,periodoComissao1,periodoComissao2,pagamentoDia1,periodoComissao3,periodoComissao4,pagamentodia2,gerarConta,comissaoDobrada,
                                   participacaoVenda,tipoparticipacao,pagamentoComissao,pagamentoRecebimento,gerarPrevisao,abaterImposto,impostoDeRenda,gerarComissao,id)
   


#_____________________________________________________Ocorrencia Funcionario_________________________________________________________________________________________________ 
    
    def selecionarjanelaOcorrenciaFuncionario(self,id):
      resultado= self.__DepartamentoDao.SelecionarjanelaOcorrencias(id)        
      return resultado        
     
    def selecionarOcorrenciaFuncionario(self,id):
      resultado= self.__DepartamentoDao.SelecionarOcorrencias(id)        
      return resultado            
    
    def selecionarOcorrenciasPrincipais(self,id):
      resultado= self.__DepartamentoDao.selecionarOcorrenciasPrincipais(id)        
      return resultado     
    
     
    def inserirOcorrenciaFuncionario(self, Data, Codigo, Descricao, Discriminacao,nome,ID):
            self.__DepartamentoDao.inserirOcorrenciasFuncionarios(Data, Codigo, Descricao, Discriminacao,nome,ID)      
                     
      
    def DeletarOcorrenciaFuncionario(self,usuario): 
          usuarios=self.__DepartamentoDao.DeletarOcorrenciasFuncionarios(usuario)            
          return usuarios            

    def selecionarDataOcorrenciasFuncionarios(self, textoLabel):
      resultado = self.__DepartamentoDao.selecionarDataOcorrenciasFuncionarios(textoLabel)
      if resultado is None or 'dataocorrencia' not in resultado or resultado['dataocorrencia'] is None:
          return ""
      return datetime.strftime(resultado['dataocorrencia'], '%d/%m/%Y')

    def selecionarCodigodeOcorrenciasFuncionarios(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarCodigodeOcorrenciasFuncionarios(textoLabel)
      if resultado is None or 'codocorr' not in resultado or resultado['codocorr'] is None:
            return ""    
    
      return resultado 
    
    def selecionarDescricaoOcorrenciasFuncionarios(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarDescricaoOcorrenciasFuncionarios(textoLabel)
      if resultado is None or 'descocorr' not in resultado or resultado['descocorr'] is None:
            return ""    
    
      return resultado     
    
    def selecionarDiscrminacaoOcorrenciasFuncionarios(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarDiscrminacaoOcorrenciasFuncionarios(textoLabel)
      if resultado is None or 'discrimina' not in resultado or resultado['discrimina'] is None:
            return ""    
      return resultado     
    
    def EditarOcorrenciasFuncionarios(self, data,codigo,descricao,discriminacao,funcionario,codigo_funcionario,id): 
           self.__DepartamentoDao.EditarOcorrenciasFuncionarios(data,codigo,descricao,discriminacao,funcionario,codigo_funcionario, id)        

#_______________________________________________________Registro Ferias____________________________________________________
    def SelecionarjanelaFerias(self,id):
      resultado= self.__DepartamentoDao.SelecionarjanelaFerias(id)        
      return resultado        
    
    def SelecionarFerias(self,id):
      resultado= self.__DepartamentoDao.SelecionarFerias(id)        
      return resultado    

    def inserirFeriasFuncionarios(self, Data1, Data2, nome,ID):
          self.__DepartamentoDao.inserirFeriasFuncionarios(Data1, Data2, nome ,ID)      

    def selecionarDataFeriasDeFuncionarios(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarDataFeriasDeFuncionarios(textoLabel)  
      return datetime.strftime(resultado['data1'],'%d/%m/%Y')
        
    def selecionarDataFeriasAteFuncionarios(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarDataFeriasAteFuncionarios(textoLabel)
      return datetime.strftime(resultado['data2'],'%d/%m/%Y')    
    
    def DeletarFeriasFuncionarios(self,usuario): 
          usuarios=self.__DepartamentoDao.DeletarFeriasFuncionarios(usuario)            
          return usuarios          

    def EditarFeriasFuncionarios(self,Data1, Data2 ,ID): 
           self.__DepartamentoDao.EditarFeriasAteFuncionario(Data1, Data2 ,ID)   

    
          
              
#_________________________________________________________Registro FIlhos________________________________________________
    def SelecionarjanelaFilhos(self,id):
      resultado= self.__DepartamentoDao.SelecionarjanelaFilhos(id)        
      return resultado        

    def SelecionarFilhos(self,id):
      resultado= self.__DepartamentoDao.SelecionarFilhos(id)        
      return resultado    

    def inserirFilhosFuncionarios(self,  nome, idade, data,nomefunc, ID):
          self.__DepartamentoDao.inserirFilhosFuncionarios(nome, idade, data,nomefunc,ID)      

    def selecionarDataDeNascimentoFilho(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarDataDeNascimentoFilho(textoLabel)  
      return datetime.strftime(resultado['nascimento'],'%d/%m/%Y')     

    def selecionarIdadeFilho(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarIDadeFilho(textoLabel)
      return resultado['idade']     
    
    def selecionarNomeFilho(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarNomeFilho(textoLabel)
      return resultado['nomefilh']      

    def EditarFilhosFuncionario(self, nome, idade, data, ID): 
           self.__DepartamentoDao.EditarFilhosFuncionario( nome, idade, data, ID)   

    def DeletarFilhosFuncionarios(self,usuario): 
          usuarios=self.__DepartamentoDao.DeletarFilhosFuncionarios(usuario)            
          return usuarios  
# ____________________________________________________________Cargos___________________________________________________
    def ConsultarCargos(self):#,usuario,senha,email,nome):  #def configPastaPadrao(self, idQueEuPassaria):
      resultados=self.__DepartamentoDao.consultarCargos()
      return  resultados       

    def inserirCargos(self,nome,salario,valAdiantado,valMax,horarioDe,horarioAte,comissoesPremio,comissaovalor,insalubridade,fgts,vale,maxVale,seguro,cBasica,inss,pdecimoterceiro,
                  ferias,partlucros,horaextmetade,horaextinteira,salariofam,pfgts,pferias,cafe,uniforme,repouso,de1,ate1,porc1,premio1,de2,ate2,porc2,premio2,de3,ate3,porc3,premio3,de4,ate4,porc4,premio4):
      
            self.__DepartamentoDao.inserirCargos(nome,salario,valAdiantado,valMax,horarioDe,horarioAte,comissoesPremio,comissaovalor,insalubridade,fgts,vale,maxVale,seguro,cBasica,inss,pdecimoterceiro,
                  ferias,partlucros,horaextmetade,horaextinteira,salariofam,pfgts,pferias,cafe,uniforme,repouso,de1,ate1,porc1,premio1,de2,ate2,porc2,premio2,de3,ate3,porc3,premio3,de4,ate4,porc4,premio4)   

    def EditarCargos(self, nome,salario,valAdiantado,valMax,horarioDe,horarioAte,comissoesPremio,comissaovalor,insalubridade,fgts,vale,maxVale,seguro,cBasica,inss,pdecimoterceiro,ferias,partlucros,horaextmetade,horaextinteira,salariofam,pfgts,pferias,cafe,uniforme,repouso,de1,ate1,porc1,premio1,de2,ate2,porc2,premio2,de3,ate3,porc3,premio3,de4,ate4,porc4,premio4,id): 
           self.__DepartamentoDao.EditarCargos(nome,salario,valAdiantado,valMax,horarioDe,horarioAte,comissoesPremio,comissaovalor,insalubridade,fgts,vale,maxVale,seguro,cBasica,inss,pdecimoterceiro,ferias,partlucros,horaextmetade,horaextinteira,salariofam,pfgts,pferias,cafe,uniforme,repouso,de1,ate1,porc1,premio1,de2,ate2,porc2,premio2,de3,ate3,porc3,premio3,de4,ate4,porc4,premio4,id)       

    def selecionarNaTabelaCargos(self,id): 
       selecionar= self.__DepartamentoDao.selecionarNaTabelaCargos(id)
       return selecionar      

    def DeletarCargos(self,usuario): 
          usuarios=self.__DepartamentoDao.DeletarCargos(usuario)            
          return usuarios

    def selecionarCargoNome(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarCargoNome(textoLabel)
      if(resultado['nome'] == None):
            return ""    
    
      return resultado 
    
    def selecionarCargoSalSindicato(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarCargoSalSindicato(textoLabel)
      if(resultado['sal_sindicato'] == None):
            return ""    
    
      return resultado 
    
    def selecionarCargoSalAdiantamento(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarCargoSalAdiantamento(textoLabel)
      if(resultado['valadianta'] == None):
            return ""    
    
      return resultado 

    def selecionarCargoValeMax(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarCargoValeMax(textoLabel)
      if(resultado['valemaxmes'] == None):
            return ""    
    
      return resultado 
    
    def selecionarCargoHoraTrab1(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarCargoHoraTrab1(textoLabel)
      if(resultado['hortrab1'] == None):
            return ""    
    
      return resultado 
    
    def selecionarCargoHoraTrab2(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarCargoHoraTrab2(textoLabel)
      if(resultado['hortrab2'] == None):
            return ""    
    
      return resultado 
    
    def selecionarCargoComPremios(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarCargoComPremios(textoLabel)
      if(resultado['sal_comiprem'] == None):
            return ""    
    
      return resultado      

    def selecionarCargoRecebePremio(self,textoLabel):
      resultados= self.__DepartamentoDao.selecionarCargoRecebePremio(textoLabel)
      retorno = []
      for resultado in resultados:
            retorno.append(resultado['sal_recebeprem'])
      
      return retorno[0]                   
                 
    
    def selecionarCargoSalInsalubridade(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarCargoSalInsalubridade(textoLabel)
      if(resultado['sal_insalubr'] == None):
            return ""    
    
      return resultado    
    
    def selecionarCargoFGTS(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarCargoFGTS(textoLabel)
      if(resultado['percfgts'] == None):
            return ""    
    
      return resultado    
    
    def selecionarCargoValeTransporte(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarCargoValeTransporte(textoLabel)
      if(resultado['valetrp'] == None):
            return ""    
    
      return resultado                        
     
    def selecionarCargoMaxValeTransp(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarCargoMaxValeTransp(textoLabel)
      if(resultado['percmaxvaletrp'] == None):
            return ""    
    
      return resultado    
    
    def selecionarCargoSalSeguro(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarCargoSalSeguro(textoLabel)
      if(resultado['sal_seguro'] == None):
            return ""    
    
      return resultado    
    
    def selecionarCargoSalCestaBasica(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarCargoSalCestaBasica(textoLabel)
      if(resultado['sal_cesta'] == None):
            return ""    
    
      return resultado                

    def selecionarCargoInss(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarCargoInss(textoLabel)
      if(resultado['percinss'] == None):
            return ""    
    
      return resultado                
    
    def selecionarCargoSalPercDecimoTerceiro(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarCargoSalPercDecimoTerceiro(textoLabel)
      if(resultado['sal_12decterc'] == None):
            return ""    
    
      return resultado     
    
    def selecionarCargoPercFerias(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarCargoPercFerias(textoLabel)
      if(resultado['sal_12ferias'] == None):
            return ""    
    
      return resultado                
    
    def selecionarCargoSalPartLucros(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarCargoSalPartLucros(textoLabel)
      if(resultado['sal_partlucr'] == None):
            return ""    
    
      return resultado                
    
    def selecionarCargoHoraExtraMet(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarCargoHoraExtraMet(textoLabel)
      if(resultado['sal_hrextra50'] == None):
            return ""    
    
      return resultado                
    
    def selecionarCargoHoraExtraInt(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarCargoHoraExtraInt(textoLabel)
      if(resultado['sal_hrextra100'] == None):
            return ""    
    
      return resultado                                           
        
    def selecionarCargoSalFamilia(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarCargoSalFamilia(textoLabel)
      if(resultado['sal_familia'] == None):
            return ""    
    
      return resultado         
    
    def selecionarCargoPercfgtsDecTerceiro(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarCargoPercfgtsDecTerceiro(textoLabel)
      if(resultado['sal_fgts12decterc'] == None):
            return ""    
    
      return resultado         
    
    def selecionarCargoPercfgtsDecFerias(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarCargoPercfgtsDecFerias(textoLabel)
      if(resultado['sal_fgts12ferias'] == None):
            return ""    
    
      return resultado         
    
    def selecionarCargoSalCafe(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarCargoSalCafe(textoLabel)
      if(resultado['sal_cafe'] == None):
            return ""    
    
      return resultado         
    
    def selecionarCargoSalUniforme(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarCargoSalUniforme(textoLabel)
      if(resultado['sal_uniforme'] == None):
            return ""    
    
      return resultado         
    
    def selecionarCargoSalRepouso(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarCargoSalRepouso(textoLabel)
      if(resultado['sal_repsemremun'] == None):
            return ""    
    
      return resultado                             

    def selecionarCargoPercPremiode1(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarCargoPercPremiode1(textoLabel)
      if(resultado['de1'] == None):
            return ""    
    
      return resultado      
    
    def selecionarCargoPercPremioate1(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarCargoPercPremioate1(textoLabel)
      if(resultado['ate1'] == None):
            return ""    
    
      return resultado      
    
    def selecionarCargoPercpremio1(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarCargoPercpremio1(textoLabel)
      if(resultado['percprem1'] == None):
            return ""    
    
      return resultado      
    
    def selecionarCargoTipoPercPremio1(self,textoLabel):
      resultados= self.__DepartamentoDao.selecionarCargoTipoPercPremio1(textoLabel)
      retorno = []
      for resultado in resultados:
            retorno.append(resultado['tipprem1'])
      
      return retorno[0]    
    
    def selecionarCargoPercPremiode2(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarCargoPercPremiode2(textoLabel)
      if(resultado['de2'] == None):
            return ""    
    
      return resultado      
    
    def selecionarCargoPercPremioate2(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarCargoPercPremioate2(textoLabel)
      if(resultado['ate2'] == None):
            return ""    
    
      return resultado      
    
    def selecionarCargoPercpremio2(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarCargoPercpremio2(textoLabel)
      if(resultado['percprem2'] == None):
            return ""    
    
      return resultado      
    
    def selecionarCargoTipoPercPremio2(self,textoLabel):
      resultados= self.__DepartamentoDao.selecionarCargoTipoPercPremio2(textoLabel)
      retorno = []
      for resultado in resultados:
            retorno.append(resultado['tipprem2'])
      
      return retorno[0]  
   
    def selecionarCargoPercPremiode3(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarCargoPercPremiode3(textoLabel)
      if(resultado['de3'] == None):
            return ""    
    
      return resultado      
    
    def selecionarCargoPercPremioate3(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarCargoPercPremioate3(textoLabel)
      if(resultado['ate3'] == None):
            return ""    
    
      return resultado      
    
    def selecionarCargoPercpremio3(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarCargoPercpremio3(textoLabel)
      if(resultado['percprem3'] == None):
            return ""    
    
      return resultado      
    
    def selecionarCargoTipoPercPremio3(self,textoLabel):
      resultados= self.__DepartamentoDao.selecionarCargoTipoPercPremio3(textoLabel)
      retorno = []
      for resultado in resultados:
            retorno.append(resultado['tipprem3'])
      
      return retorno[0]      

    def selecionarCargoPercPremiode4(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarCargoPercPremiode4(textoLabel)
      if(resultado['de4'] == None):
            return ""    
    
      return resultado      
    
    def selecionarCargoPercPremioate4(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarCargoPercPremioate4(textoLabel)
      if(resultado['ate4'] == None):
            return ""    
    
      return resultado      
    
    def selecionarCargoPercpremio4(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarCargoPercpremio4(textoLabel)
      if(resultado['percprem4'] == None):
            return ""    
    
      return resultado      
    
    def selecionarCargoTipoPercPremio4(self,textoLabel):
      resultados= self.__DepartamentoDao.selecionarCargoTipoPercPremio4(textoLabel)
      retorno = []
      for resultado in resultados:
            retorno.append(resultado['tipprem4'])
      
      return retorno[0]  
#_____________________________________________________________________Funções________________________________________________
    def ConsultarFuncoes(self):#,usuario,senha,email,nome):  #def configPastaPadrao(self, idQueEuPassaria):
      resultados=self.__DepartamentoDao.consultarFuncoes()
      return  resultados   

    def inserirfuncoes(self, Nome,  Descricao, TipoPagamento, Pagamento, SalarioFuncionario, ProducaoDia,ProducaoHoraNormal,ProducaoHoraExtra,ProducaoHoraDobrada,QuantidadeAdicional,BonusDiario):
            self.__DepartamentoDao.inserirFuncoes(Nome,  Descricao, TipoPagamento, Pagamento, SalarioFuncionario, ProducaoDia,ProducaoHoraNormal,ProducaoHoraExtra,ProducaoHoraDobrada,QuantidadeAdicional,BonusDiario)    
          
    def selecionarNaTabelaFuncoes(self,id): 
       selecionar= self.__DepartamentoDao.selecionarnaTabelaFuncoes(id)
       return selecionar
     
    def selecionarFuncaoNome(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncaoNome(textoLabel)
      if(resultado['nome'] == None):
            return ""    
    
      return resultado 

    def selecionarFuncaoDescTarefa(self,textoLabel):
      return self.__DepartamentoDao.selecionarFuncaoDescTarefa(textoLabel)

    def selecionarFuncaoTipoPagamento(self, textoLabel):
        resultado = self.__DepartamentoDao.selecionarFuncaoTipoPagamento(textoLabel)     
        
        if resultado is not None:
            return resultado
        else:
            return "Usuário não encontrado"     
 
    
    def selecionarFuncaoTipoPagamentoDesp(self):
        resultados = self.__DepartamentoDao.selecionarFuncaoTipoPagamentoDesp()
        return resultados      


    def selecionarFuncaoPagamento(self,textoLabel):
      resultados= self.__DepartamentoDao.selecionarFuncaoPagamento(textoLabel)
      retorno = []
      for resultado in resultados:
             retorno.append(resultado['tipopagamento'])
    
            
      return retorno[0]

    
    def selecionarFuncaoSalarioFuncionario(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncaoSalarioFuncionario(textoLabel)
      if(resultado['salfun'] == None):
            return ""    
    
      return resultado     

    def selecionarFuncaoValorProducaoDia(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncaoValorProducaoDia(textoLabel)
      if(resultado['valproddia'] == None):
            return ""    
    
      return resultado     

    def selecionarFuncaoValorProducaoHoraNormal(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncaoValorProducaoHoraNormal(textoLabel)
      if(resultado['valprodhrnorm'] == None):
            return ""    
    
      return resultado 

    def selecionarFuncaoValorProducaoHoraExtra(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncaoValorProducaoHoraExtra(textoLabel)
      if(resultado['valprodhrext'] == None):
            return ""    
    
      return resultado 

    def selecionarFuncaoValorProducaoHoraDobrada(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncaoValorProducaoHoraDobrada(textoLabel)
      if(resultado['valprodhrdbr'] == None):
            return ""    
    
      return resultado 

    def selecionarFuncaQuantidadeAdicional(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncaQuantidadeAdicional(textoLabel)
      if(resultado['valbonus'] == None):
            return ""    
    
      return resultado 

    def selecionarFuncaValorBonusDiario(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFuncaValorBonusDiario(textoLabel)
      if(resultado['valbonusdia'] == None):
            return ""    
    
      return resultado 

    def EditarFuncoes(self, Nome,  Descricao, TipoPagamento, Pagamento, SalarioFuncionario, ProducaoDia,ProducaoHoraNormal,ProducaoHoraExtra,ProducaoHoraDobrada,QuantidadeAdicional,BonusDiario, id): 
           resultados= self.__DepartamentoDao.EditarFuncoes(Nome,  Descricao, TipoPagamento, Pagamento, SalarioFuncionario, ProducaoDia,ProducaoHoraNormal,ProducaoHoraExtra,ProducaoHoraDobrada,QuantidadeAdicional,BonusDiario, id)  


    def DeletarFuncoes(self,usuario): 
          usuarios=self.__DepartamentoDao.DeletarFuncoes(usuario)            
          return usuarios

#___________________________________________________________________FERIADOS__________________________________________________
  
  
    def ConsultarFeriados(self):#,usuario,senha,email,nome):  #def configPastaPadrao(self, idQueEuPassaria):
      resultados=self.__DepartamentoDao.ConsultarFeriados()
      return  resultados   
  
  
    def selecionarTabelaFeriados(self,id): 
       selecionar= self.__DepartamentoDao.selecionarTabelaFeriados(id)
       return selecionar
   
    def inserirferiados(self, data,descricao):
            self.__DepartamentoDao.inserirFeriado(data,descricao)       
            
    def DeletarFeriados(self,usuario): 
          usuarios=self.__DepartamentoDao.DeletarFeriados(usuario)            
          return usuarios
         
     
    def EditarFeriados(self, data,  Descricao, id): 
           self.__DepartamentoDao.EditarFeriados( data, Descricao,id)                              
   
    def selecionardescricao(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFeriadoDescricao(textoLabel)
      if(resultado['descricao'] == None):
            return ""    
    
      return resultado
   
   
    def ConsultarFilhos(self):#,usuario,senha,email,nome):  #def configPastaPadrao(self, idQueEuPassaria):
      resultados=self.__DepartamentoDao.consultarFilhos()
      return  resultados            
    
    
    def selecionarFeriadoData(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarFeriadoData(textoLabel)
      if(resultado['data'] == None):
            return ""    
    
      return datetime.strftime(resultado['data'],'%d/%m/%Y')

#____________________________________________________Acidentes_____________________________________________

    def ConsultarAcidentes(self):#,usuario,senha,email,nome):  #def configPastaPadrao(self, idQueEuPassaria):
      resultados=self.__DepartamentoDao.ConsultarAcidentes()
      return  resultados 
    
    def inserirAcidentes(self, data,descricao,qt_pessoasafastadas,qt_pessoasnaoafastadas):
            self.__DepartamentoDao.inserirAcidente(data,descricao,qt_pessoasafastadas,qt_pessoasnaoafastadas)  
            
            
    def EditarFeriados(self, data,  Descricao, id): 
           self.__DepartamentoDao.EditarFeriados( data, Descricao,id)     
           
           
    def DeletarAcidente(self,usuario): 
          usuarios=self.__DepartamentoDao.DeletarAcidente(usuario)            
          return usuarios                              
    
    
    def EditarAcidente(self,data, descricao, qt_pessoasafastadas, qt_pessoasnaoafastadas, id): 
           self.__DepartamentoDao.EditarAcidente(data,descricao, qt_pessoasafastadas, qt_pessoasnaoafastadas, id)   
           


    def selecionarAcidentedata(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarAcidenteData(textoLabel)
      if(resultado['data'] == None):
            return ""    
    
      return datetime.strftime(resultado['data'],'%d/%m/%Y') 
           
    def selecionarAcidentedescricao(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarAcidenteDescricao(textoLabel)
      if(resultado['descricao'] == None):
            return ""    
    
      return resultado           
    
    def selecionarAcidenteQuantidadePessoasAfastadas(self,textoLabel):
      resultado= self.__DepartamentoDao.selecionarAcidenteQuantidadepessoasafastadas(textoLabel)
      if(resultado['qt_pessoasafastadas'] == None):
            return ""    
    
      return resultado               
    
    
    def selecionarAcidenteQuantidadePessoasNaoAfastadas(self,textoLabel):
  
      resultado= self.__DepartamentoDao.selecionarAcidenteQuantidadepessoasNaoAfastadas(textoLabel)
      if(resultado['qt_pessoasnaoafastadas'] == None):
            return ""    
    
      return resultado 
    
    
#________________________________________________________________________Trasportes________________________________________________________________          

    def ConsultarTrasporte(self):#,usuario,senha,email,nome):  #def configPastaPadrao(self, idQueEuPassaria):
      resultados=self.__DepartamentoDao.ConsultarTrasporte()
      return  resultados 
    
    
    def inserirTransporte(self, linha, fornecedor,itinerario , valor):
            self.__DepartamentoDao.inserirTransporte(linha, fornecedor, itinerario, valor)   
            
    def DeletarTransporte(self,usuario): 
          usuarios=self.__DepartamentoDao.DeletarTransporte(usuario)            
          return usuarios                

  
    def selecionarTabelaTransporte(self,id): 
       selecionar= self.__DepartamentoDao.selecionarTabelaTransporte(id)
       return selecionar

    def selecionarTransporteLinha(self,textoLabel):
  
      resultado= self.__DepartamentoDao.selecionarTransporteLinha(textoLabel)
      if(resultado['linha'] == None):
            return ""    
    
      return resultado 


    def selecionarTransporteFornecedor(self,textoLabel):
  
      resultado= self.__DepartamentoDao.selecionarTransporteFornecedor(textoLabel)
      if(resultado['fornecedor'] == None):
            return ""    
    
      return resultado 


    def selecionarTransporteItinerario(self,textoLabel):
  
      resultado= self.__DepartamentoDao.selecionarTransporteItinerario(textoLabel)
      if(resultado['itinerario'] == None):
            return ""    
    
      return resultado
    
    
    def selecionarTransporteValor(self,textoLabel):
  
      resultado= self.__DepartamentoDao.selecionarTransporteValor(textoLabel)
      if(resultado['valor'] == None):
            return ""    
    
      return resultado    
    
    
    def EditarTransporte(self,linha, fornecedor,itinerario , valor, id): 
           self.__DepartamentoDao.EditarTransporte(linha, fornecedor,itinerario , valor, id)     

#______________________________________________________OCORRENCiAS___________________________________________________________           
    def ConsultarOcorrencia(self):#,usuario,senha,email,nome):  #def configPastaPadrao(self, idQueEuPassaria):
      resultados=self.__DepartamentoDao.ConsultarOcorrencia()
      return  resultados              
    
    def selecionarTabelaOcorrencia(self,id): 
       selecionar= self.__DepartamentoDao.selecionarTabelaOcorrencia(id)
       return selecionar  
     
     


    
    
    
#_________________________________________________Tabela funcionario    
    def ConsultarOcorrenciafuncionario(self):#,usuario,senha,email,nome):  #def configPastaPadrao(self, idQueEuPassaria):
      resultados=self.__DepartamentoDao.ConsultarOcorrenciaTabelaFuncionario()
      return  resultados         
    
    
#_____________________________________________Imagem BD_________________________________________________________________________________________________    

    def selecionarimagem(self): 
          selecionar= self.__DepartamentoDao.selecionarimagem()
          return selecionar[0]
 #________________________________________________________FOlha de Ponto_________________________________________________________________________________
 #________________________________________________________FOlha de Ponto_________________________________________________________________________________
    def ConsultarFolhadePonto(self):#,usuario,senha,email,nome):  #def configPastaPadrao(self, idQueEuPassaria):
       resultados=self.__DepartamentoDao.ConsultarFolhadePonto()
       return  resultados        
     
    def ConsultarFolhadePontoPorStatusOK(self):#,usuario,senha,email,nome):  #def configPastaPadrao(self, idQueEuPassaria):
       resultados=self.__DepartamentoDao.ConsultarFolhadePontoPorStatusOK()
       return  resultados    
     
    def ConsultarFolhadePontoPorStatusTratar(self):#,usuario,senha,email,nome):  #def configPastaPadrao(self, idQueEuPassaria):
       resultados=self.__DepartamentoDao.ConsultarFolhadePontoPorStatusTratar()
       return  resultados         
     
    def ConsultarFolhadePontoPorFuncionario(self,Funcionario):#,usuario,senha,email,nome):  #def configPastaPadrao(self, idQueEuPassaria):
       resultados=self.__DepartamentoDao.ConsultarFolhadePontoPorFuncionario(Funcionario)
       return  resultados 
     
    def selecionarPorFuncionario(self):#,usuario,senha,email,nome):  #def configPastaPadrao(self, idQueEuPassaria):
       resultados=self.__DepartamentoDao.selecionarPorFuncionario()
       return  resultados        
           
     
    def selecionarFuncionarioPorNome(self):#,usuario,senha,email,nome):  #def configPastaPadrao(self, idQueEuPassaria):
       resultados=self.__DepartamentoDao.selecionarFuncionarioPorNome()
       return  resultados          
       
       
    def ConsultarFolhadePontoPorHoraextra(self):#,usuario,senha,email,nome):  #def configPastaPadrao(self, idQueEuPassaria):
       resultados=self.__DepartamentoDao.ConsultarFolhadePontoPorHoraextra()
       return  resultados                  
    def ConsultarFolhadePontoSemHoraextra(self):#,usuario,senha,email,nome):  #def configPastaPadrao(self, idQueEuPassaria):
       resultados=self.__DepartamentoDao.ConsultarFolhadePontoSemHoraextra()
       return  resultados     
     
    def ConsultarFolhadePontoPordata(self,datainicial,datafinal):#,usuario,senha,email,nome):  #def configPastaPadrao(self, idQueEuPassaria):
       resultados=self.__DepartamentoDao.ConsultarFolhadePontoPordata(datainicial,datafinal)
       return  resultados        
     
    def ConsultarFolhadePontoPordataTratar(self,datainicial,datafinal):#,usuario,senha,email,nome):  #def configPastaPadrao(self, idQueEuPassaria):
       resultados=self.__DepartamentoDao.ConsultarFolhadePontoPordataTratar(datainicial,datafinal)
       return  resultados      
     
    def ConsultarFolhadePontoPordataTratarNome(self,datainicial,datafinal,nome):#,usuario,senha,email,nome):  #def configPastaPadrao(self, idQueEuPassaria):
       resultados=self.__DepartamentoDao.ConsultarFolhadePontoPordataTratarNome(datainicial,datafinal,nome)
       return  resultados        
    
    def ConsultarFolhadePontoPordataOkNome(self,datainicial,datafinal,nome):#,usuario,senha,email,nome):  #def configPastaPadrao(self, idQueEuPassaria):
       resultados=self.__DepartamentoDao.ConsultarFolhadePontoPordataOkNome(datainicial,datafinal,nome)
       return  resultados    
     
    def ConsultarFolhadePontoPordataHoraextraNome(self,datainicial,datafinal,nome):#,usuario,senha,email,nome):  #def configPastaPadrao(self, idQueEuPassaria):
       resultados=self.__DepartamentoDao.ConsultarFolhadePontoPordataHoraextraNome(datainicial,datafinal,nome)
       return  resultados      
     
    def ConsultarFolhadePontoSemdataHoraextraNome(self,datainicial,datafinal,nome):#,usuario,senha,email,nome):  #def configPastaPadrao(self, idQueEuPassaria):
       resultados=self.__DepartamentoDao.ConsultarFolhadePontoPordataSemHoraextraNome(datainicial,datafinal,nome)
       return  resultados                
     
     
     
    def ConsultarFolhadePontoPordataHoraextra(self,datainicial,datafinal):#,usuario,senha,email,nome):  #def configPastaPadrao(self, idQueEuPassaria):
       resultados=self.__DepartamentoDao.ConsultarFolhadePontoPordataHoraextra(datainicial,datafinal)
       return  resultados           
     
    def ConsultarFolhadePontoPordataSemHoraextra(self,datainicial,datafinal):#,usuario,senha,email,nome):  #def configPastaPadrao(self, idQueEuPassaria):
       resultados=self.__DepartamentoDao.ConsultarFolhadePontoPordataSemHoraextra(datainicial,datafinal)
       return  resultados        
     
    def ConsultarFolhadePontoPorFuncionariEData(self,datainicial,datafinal,funcionario):#,usuario,senha,email,nome):  #def configPastaPadrao(self, idQueEuPassaria):
       resultados=self.__DepartamentoDao.ConsultarFolhadePontoPorFuncionariEData(datainicial,datafinal,funcionario)
       return  resultados 
     
    def ConsultarFolhadePontoPordataOk(self,datainicial,datafinal):#,usuario,senha,email,nome):  #def configPastaPadrao(self, idQueEuPassaria):
       resultados=self.__DepartamentoDao.ConsultarFolhadePontoPordataOk(datainicial,datafinal)
       return  resultados          
        
    def InserirControledePonto(self, data,codigo_funcionario, funcionario,horarioEntrada,horarioSaida,entradaAlmoco,saidaAlmoco,entradaIntervalo,saidaIntervalo,status,observacao,imagem):
            self.__DepartamentoDao.InserirControledeponto(data,codigo_funcionario, funcionario,horarioEntrada,horarioSaida,entradaAlmoco,saidaAlmoco,entradaIntervalo,saidaIntervalo,status,observacao,imagem)
            
    def SelecionarIdFolhadePonto(self,id): 
       selecionar= self.__DepartamentoDao.SelecionarIdFolhadePonto(id)
       return selecionar  
     
    def InserirControledepontoImportacao(self, codigo,funcionario,data,horarioEntrada,horarioSaida,entradaAlmoco,saidaAlmoco,entradaIntervalo,saidaIntervalo,status,observacao):
            self.__DepartamentoDao.InserirControledepontoImportacao(codigo,funcionario,data,horarioEntrada,horarioSaida,entradaAlmoco,saidaAlmoco,entradaIntervalo,saidaIntervalo,status,observacao)
                 
     
    def EditarFolhadePonto(self,data,codigo,funcionario,horarioEntrada,horarioSaida,entradaAlmoco,saidaAlmoco,entradaIntervalo,saidaIntervalo,status,observacao,imagem,id): 
           self.__DepartamentoDao.EditarFolhadePonto(data,codigo,funcionario,horarioEntrada,horarioSaida,entradaAlmoco,saidaAlmoco,entradaIntervalo,saidaIntervalo,status,observacao,imagem,id)  
           

    def SelecionarFolhadePontoData(self,textoLabel):
      resultado= self.__DepartamentoDao.SelecionarFolhadePontoData(textoLabel)
      if(resultado['data'] == None):
            return ""    
      return datetime.strftime(resultado['data'],'%d/%m/%Y')           
    
    def SelecionarFolhadePontoFuncionario(self,textoLabel):
      resultado= self.__DepartamentoDao.SelecionarFolhadePontoFuncionario(textoLabel)
      if(resultado['funcionario'] == None):
            return ""    
    
      return resultado          
    
    
    def SelecionarFolhadePontoHorEntrada(self,textoLabel):
      resultado= self.__DepartamentoDao.SelecionarFolhadePontoHorEntrada(textoLabel)
      if(resultado['hrentr'] == None):
            return ""    
    
      return resultado   
    
    
    def SelecionarFolhadePontoHorSaida(self,textoLabel):
      resultado= self.__DepartamentoDao.SelecionarFolhadePontoHorSaida(textoLabel)
      if(resultado['hrsaid'] == None):
            return ""    
    
      return resultado   
    
    
    def SelecionarFolhadePontoInterHorEntrada(self,textoLabel):
      resultado= self.__DepartamentoDao.SelecionarFolhadePontoInterHorEntrada(textoLabel)
      if(resultado['interv2entr'] == None):
            return ""    
    
      return resultado   
    
    
    def SelecionarFolhadePontoInterHorSaida(self,textoLabel):
      resultado= self.__DepartamentoDao.SelecionarFolhadePontoInterHorSaida(textoLabel)
      if(resultado['interv2said'] == None):
            return ""    
    
      return resultado                
    
    
    def SelecionarFolhadePontoHorEntradaEx(self,textoLabel):
      resultado= self.__DepartamentoDao.SelecionarFolhadePontoHorEntradaEx(textoLabel)
      if(resultado['interventr'] == None):
            return ""    
    
      return resultado   
    
    
    def SelecionarFolhadePontoHorSaidaExt(self,textoLabel):
      resultado= self.__DepartamentoDao.SelecionarFolhadePontoHorSaidaExt(textoLabel)
      if(resultado['intervsaid'] == None):
            return ""    
    
      return resultado   
    
    def SelecionarFolhadePontoTotHoras(self,textoLabel):
      resultado= self.__DepartamentoDao.SelecionarFolhadePontoTotHoras(textoLabel)
      if(resultado['tothoras'] == None):
            return ""    
    
      return resultado         
   
    def selecionarFuncionarioJustificativa(self, textoLabel):
        resultado = self.__DepartamentoDao.selecionarFuncionarioJustificativa(textoLabel)
        return resultado
    

    def SelecionarFolhadePontoImagem(self, id):
      caminho_imagem = self.__DepartamentoDao.SelecionarFolhadePontoImagem(id)
      if caminho_imagem is None:
          return None
      return caminho_imagem
    
    def SelecionarFolhadePontoObservacao(self,textoLabel):
      resultado= self.__DepartamentoDao.SelecionarFolhadePontoObservacao(textoLabel)
      if(resultado['observacoes'] == None):
            return ""    
    
      return resultado         
    

              
    def DeletarFolhaDePonto(self,usuario): 
          usuarios=self.__DepartamentoDao.DeletarFolhaDePonto(usuario)            
          return usuarios   
   
    def selecionarFuncionario(self):
      resultado= self.__DepartamentoDao.selecionarFuncionario()
      return resultado          
    
   
    def selecionarFuncionarioNomes(self):
      resultado= self.__DepartamentoDao.selecionarFuncionarioNomes()
      return resultado        
    
    def selecionarFuncionarioNomesAtivo(self):
      resultado= self.__DepartamentoDao.selecionarFuncionarioNomesAtivo()
      return resultado     
    
    def selecionarFuncionarioNomesInativo(self):
      resultado= self.__DepartamentoDao.selecionarFuncionarioNomesInativo()
      return resultado         
    
    def selecionarUsuarioPorNomeeid(self,nome):
      if nome == "":
          return self.__DepartamentoDao.selecionarFuncionarioNomes()
      else:
          return self.__DepartamentoDao.selecionarUsuarioPorNomeeid(nome)      
       
    def selecionarFuncionarioporIDOcorrencia(self, texto):
      resultado = self.__DepartamentoDao.selecionarFuncionarioporIDOcorrencia(texto)
      if resultado is not None:
          return resultado
      else:
          return "Usuário não encontrado"      
    
    def selecionarFuncionarioporID(self, texto):
      resultado = self.__DepartamentoDao.selecionarFuncionarioporID(texto)
      if resultado is not None:
          return resultado
      else:
          return "Usuário não encontrado"    
        
    def selecionarFuncionarioporDesabilitado(self, texto):
      resultado = self.__DepartamentoDao.selecionarFuncionarioporID(texto)
      if resultado is not None:
          return resultado
      else:
          return None    
# __________________________________________________Folha de pagamento_______________________________________________________________
    def ConsultarFolhaDePagamento(self):
       resultados=self.__DepartamentoDao.ConsultarFolhadePAgamento()
       return  resultados                  
     
#_____________________________________________________HORAS EXTRAS______________________________________________________________________ 
    def ConsultarHoraExtra(self):#,usuario,senha,email,nome):  #def configPastaPadrao(self, idQueEuPassaria):
       resultados=self.__DepartamentoDao.ConsultarHoraExtra()
       return  resultados       
     
    def ConsultarHoraExtrasOK(self):#,usuario,senha,email,nome):  #def configPastaPadrao(self, idQueEuPassaria):
       resultados=self.__DepartamentoDao.ConsultarHoraExtrasOK()
       return  resultados    
     
    def ConsultarHoraExtraStatusTratar(self):#,usuario,senha,email,nome):  #def configPastaPadrao(self, idQueEuPassaria):
       resultados=self.__DepartamentoDao.ConsultarHoraExtraStatusTratar()
       return  resultados          
     
            
    def ConsultarHoraExtraPordata(self,datainicial,datafinal):#,usuario,senha,email,nome):  #def configPastaPadrao(self, idQueEuPassaria):
       resultados=self.__DepartamentoDao.ConsultarHoraExtraPordata(datainicial,datafinal)
       return  resultados        
     
    def ConsultarHoraExtraPordataTratar(self,datainicial,datafinal):#,usuario,senha,email,nome):  #def configPastaPadrao(self, idQueEuPassaria):
       resultados=self.__DepartamentoDao.ConsultarHoraExtraPordataTratar(datainicial,datafinal)
       return  resultados                 
     
    def ConsultarHoraExtraPordataOk(self,datainicial,datafinal):#,usuario,senha,email,nome):  #def configPastaPadrao(self, idQueEuPassaria):
       resultados=self.__DepartamentoDao.ConsultarHoraExtraPordataOk(datainicial,datafinal)
       return  resultados          
     
    def SelecionarIdHoraExtra(self,id): 
       selecionar= self.__DepartamentoDao.SelecionarIdHoraExtra(id)
       return selecionar          
     

    def SelecionarHoraExtraData(self,textoLabel):
      resultado= self.__DepartamentoDao.SelecionarHoraExtraData(textoLabel)
      if(resultado['data'] == None):
            return ""    
      return datetime.strftime(resultado['data'],'%d/%m/%Y')       
     
    def SelecionarHoraExtraEntrada(self,textoLabel):
      resultado= self.__DepartamentoDao.SelecionarHoraExtraEntrada(textoLabel)
      if(resultado['he_entrada'] == None):
            return ""    
    
      return resultado   
    
    
    def SelecionarHoraExtraSaida(self,textoLabel):
      resultado= self.__DepartamentoDao.SelecionarHoraExtraSaida(textoLabel)
      if(resultado['he_saida'] == None):
            return ""    
    
      return resultado        
    
    def SelecionarTempoIntervalo(self,textoLabel):
      resultado= self.__DepartamentoDao.SelecionarTempoIntervalo(textoLabel)
      if(resultado['intervalo'] == None):
            return ""    
    
      return resultado         
     
     
    def selecionarFuncionarioporIDHoraExtra(self, texto):
      resultado = self.__DepartamentoDao.selecionarFuncionarioporIDHoraExtra(texto)
      if resultado is not None:
          return resultado
      else:
          return "Usuário não encontrado"    
             
             
    def SelecionarHoraExtraObservacao(self,textoLabel):
      resultado= self.__DepartamentoDao.SelecionarHoraExtraObservacao(textoLabel)
      if(resultado['observacoes'] == None):
            return ""    
    
      return resultado      
    
    def selecionarHoraExtraJustificativa(self, textoLabel):
        resultado = self.__DepartamentoDao.selecionarHoraExtraJustificativa(textoLabel)
        return resultado
    

    def SelecionarHoraExtraImagem(self, id):
      caminho_imagem = self.__DepartamentoDao.SelecionarHoraExtraImagem(id)
      if caminho_imagem is None:
          return None
      return caminho_imagem             
 
    def InserirHoraExtra(self, data,codigo_funcionario, funcionario,entradaIntervalo,saidaIntervalo,intervalo,status,observacao,imagem):
            self.__DepartamentoDao.InserirHoraExtra(data,codigo_funcionario, funcionario,entradaIntervalo,saidaIntervalo,intervalo,status,observacao,imagem)
            
    def EditarHoraExtra(self, data,codigo_funcionario, funcionario,entradaIntervalo,saidaIntervalo,intervalo,status,observacao,imagem,id): 
           self.__DepartamentoDao.EditarHoraExtra(data,codigo_funcionario, funcionario,entradaIntervalo,saidaIntervalo,intervalo,status,observacao,imagem,id)
           
    def InserirHoraExtraPorSenha(self, data, funcionario,entradaIntervalo,saidaIntervalo):
            self.__DepartamentoDao.InserirHoraExtraPorSenha(data, funcionario,entradaIntervalo,saidaIntervalo)           
   
    def DeletarHoraExtra(self,usuario): 
          usuarios=self.__DepartamentoDao.DeletarHoraExtra(usuario)            
          return usuarios   
              
   
#___________________________________________________Relógio de ponto__________________________________________________________________ 
    def ConsultarRelogiodePonto(self):
       resultados=self.__DepartamentoDao.ConsultarRelogiodePonto()
       return  resultados   
     
    def ConsultarRelogiodePontoPordata(self,datainicial,datafinal):
       resultados=self.__DepartamentoDao.ConsultarRelogiodePontoordata(datainicial,datafinal)
       return  resultados           
     
    def InserirRelogiodePontoImportacao(self,cod,tipo, data, hora, pis):
            self.__DepartamentoDao.InserirRelogiodePontoImportacao(cod,tipo, data, hora, pis)     
            
            