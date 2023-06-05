class PermDeptPEssoal:
    def __init__(self,dept_id, perm_caddept, perm_caddept_funcionarios, perm_caddept_cargos, perm_caddept_funcoes, perm_caddept_transportes, perm_caddept_acidentes, perm_caddept_ocorrencias, perm_caddept_feriados, perm_funcionarios_incluir, perm_funcionarios_editar, perm_funcionarios_excluir, perm_cargps_incluir, perm_cargps_editar, perm_cargos_excluir, 
                 perm_funcoes_incluir, perm_funcoes_editar, perm_funcoes_excluir, perm_transportes_incluir, perm_transportes_editar, perm_transportes_excluir,  perm_acidentes_incluir, perm_acidentes_editar,
                 perm_acidentes_excluir, perm_ocorrencias_incluir, perm_ocorrencias_editar, perm_ocorrencias_excluir,perm_feriados_incluir,perm_feriados_editar,perm_feriados_excluir,perm_folhadeponto,perm_hr_extra,perm_relatorios,
                 perm_rel_cons_hextra,perm_rel_bhora,perm_rel_cfrequencia,perm_rel_fpagamento,perm_relogio_ponto):
        
        self.dept_id = dept_id
        self.perm_caddept = perm_caddept 
        self.perm_caddept_funcionarios=perm_caddept_funcionarios 
        self.perm_caddept_cargos=perm_caddept_cargos
        self.perm_caddept_funcoes = perm_caddept_funcoes 
        self.perm_caddept_transportes = perm_caddept_transportes 
        self.perm_caddept_acidentes  = perm_caddept_acidentes 
        self.perm_caddept_ocorrencias = perm_caddept_ocorrencias 
        self.perm_caddept_feriados = perm_caddept_feriados 
        self.perm_funcionarios_incluir = perm_funcionarios_incluir
        self.perm_funcionarios_editar = perm_funcionarios_editar 
        self.perm_funcionarios_excluir =perm_funcionarios_excluir 
        self.perm_cargps_incluir=perm_cargps_incluir
        self.perm_cargps_editar=perm_cargps_editar
        self.perm_cargos_excluir=perm_cargos_excluir
        self.perm_funcoes_incluir=perm_funcoes_incluir
        self.perm_funcoes_editar=perm_funcoes_editar
        self.perm_funcoes_excluir=perm_funcoes_excluir
        self.perm_transportes_incluir=perm_transportes_incluir
        self.perm_transportes_editar=perm_transportes_editar
        self.perm_transportes_excluir=perm_transportes_excluir
        self.perm_acidentes_incluir =perm_acidentes_incluir 
        self.perm_acidentes_editar = perm_acidentes_editar 
        self.perm_acidentes_excluir = perm_acidentes_excluir 
        self.perm_ocorrencias_incluir =perm_ocorrencias_incluir 
        self.perm_ocorrencias_editar = perm_ocorrencias_editar 
        self.perm_ocorrencias_excluir = perm_ocorrencias_excluir
        self.perm_feriados_incluir =perm_feriados_incluir 
        self.perm_feriados_editar = perm_feriados_editar 
        self.perm_feriados_excluir = perm_feriados_excluir 
        self.perm_folhadeponto =perm_folhadeponto 
        self.perm_hr_extra = perm_hr_extra 
        self.perm_relatorios =perm_relatorios 
        self.perm_rel_cons_hextra = perm_rel_cons_hextra 
        self.perm_rel_bhora = perm_rel_bhora 
        self.perm_rel_cfrequencia =perm_rel_cfrequencia 
        self.perm_rel_fpagamento = perm_rel_fpagamento  
        self.perm_relogio_ponto = perm_relogio_ponto       
        
        