from workalendar.america import Brazil
from datetime import date, datetime
import calendar

class Salario:
    def __init__(self, salario_base, inss, salario_funcao,salario_liquido,decimo_terceiro,comissoese_premio,ferias,insalubridade,fgts,vale_transporte,max_vale_transporte,Seguro,Cesta_Basica,gremio,pensao_alimenticia,
                 participacao_lucros,horas_extras_50,horas_extras_100,Salario_Familia,fgts_decimo_terceiro,Fgts_ferias,cafe_da_manha,uniforme,Repouso_sem_remuneracao,salario_total,total_beneficios,customensal,custodiario,custohora,
                 dias_uteis_entrada,dias_uteis_saida,intervalo_saida,intervalo_entrada):
        self.salario_base = salario_base
        self.inss=inss
        self.salario_funcao = salario_funcao
        self.salario_liquido=salario_liquido
        self.decimo_terceiro=decimo_terceiro
        self.comissoese_premio=comissoese_premio
        self.ferias=ferias
        self.insalubridade=insalubridade
        self.fgts=fgts
        self.vale_transporte=vale_transporte
        self.max_vale_transporte=max_vale_transporte
        self.Seguro=Seguro
        self.Cesta_Basica=Cesta_Basica
        self.gremio=gremio
        self.pensao_alimenticia=pensao_alimenticia
        self.participacao_lucros=participacao_lucros
        self.horas_extras_50=horas_extras_50
        self.horas_extras_100=horas_extras_100
        self.Salario_Familia=Salario_Familia
        self.fgts_decimo_terceiro=fgts_decimo_terceiro
        self.Fgts_ferias=Fgts_ferias
        self.cafe_da_manha=cafe_da_manha
        self.uniforme=uniforme
        self.Repouso_sem_remuneracao=Repouso_sem_remuneracao
        self.salario_total=salario_total
        self.total_beneficios=total_beneficios
        self.customensal=customensal
        self.custodiario=custodiario
        self.custohora=custohora
        self.dias_uteis_entrada=dias_uteis_entrada
        self.dias_uteis_saida=dias_uteis_saida
        self.intervalo_saida=intervalo_saida
        self.intervalo_entrada=intervalo_entrada
        
    def calcular_salario_total(self):
        return self.salario_base + self.salario_funcao
    
    def calcular_beneficios(self):
       return self.decimo_terceiro*0.0833 + self.comissoese_premio + self.ferias*0.0833 + self.insalubridade + self.vale_transporte + self.Seguro + self.Cesta_Basica + self.gremio + self.pensao_alimenticia + self.horas_extras_50 + self.horas_extras_100 +self.Salario_Familia + self.fgts_decimo_terceiro +self.Fgts_ferias+ self.cafe_da_manha + self.uniforme + self.Repouso_sem_remuneracao 
    cal = Brazil()
    now = datetime.now()
    start_date = date(now.year, now.month, 1)
    end_date = date(now.year, now.month, calendar.monthrange(now.year, now.month)[1])
    qtd_dias_uteis = cal.get_working_days_delta(start_date, end_date)      
    def calcular_custo_mensal(self):
        return   self.salario_base + self.salario_funcao + self.decimo_terceiro*0.0833 + self.comissoese_premio + self.ferias*0.0833 + self.insalubridade + self.vale_transporte + self.Seguro + self.Cesta_Basica + self.gremio + self.pensao_alimenticia + self.horas_extras_50 + self.horas_extras_100 +self.Salario_Familia + self.fgts_decimo_terceiro +self.Fgts_ferias+ self.cafe_da_manha + self.uniforme + self.Repouso_sem_remuneracao 
    def calcular_custo_diario(self):
        return 
    def calcular_custo_hora(self):
        return