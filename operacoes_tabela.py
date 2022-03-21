import mysql.connector
import yaml


class Tabela:
    def __init__(self, arquivoYaml, nomeTabela):
        self.nome = nomeTabela
        try:
            with open(arquivoYaml, "rt", encoding = "utf8") as arquivo:
                tabelaConfig = yaml.safe_load(arquivo)
            self.arquivoTabela = tabelaConfig[self.nome]
        except IOError:
            print("\nFalha ao acessar arquivo de configurações YAML")
        try:
            self.banco = mysql.connector.connect(
                host    = "localhost",
                user    = "root",
                passwd  = "",
                database = "funtura"
            )
            self.cursor = self.banco.cursor()
        except IOError:
            print("\nFalha ao acessar base de dados")
    
    def inserir(self, valores_inseridos):

        self.parametros = ["(", "("]

        for i in range(1, self.arquivoTabela["quantidade"]):
            if i != 1:
                self.parametros[0] += ","
                self.parametros[1] += ","
            self.parametros[0] += self.arquivoTabela["nomes_tabelas"][i]
            self.parametros[1] += "%s"

        self.parametros[0] += ")"
        self.parametros[1] += ")"
        
        self.comando_sql = "INSERT INTO {} {} VALUES {}".format(self.nome, self.parametros[0], self.parametros[1])
        self.cursor.execute(self.comando_sql, valores_inseridos)
        
        self.banco.commit()
        
    def inserir_mov_caixa(self, dataHora,valor,id_caixa,id_tm): #Fução para inserir movimento de caixa quando não tem um IdOS
        
        self.comando_sql = "INSERT INTO {} (dataHoraMov,valorMov,idOS,idCaixa,idTipoMovimento) VALUES ('{}','{}',NULL,'{}','{}')".format(self.nome,dataHora,valor,id_caixa,id_tm)
        self.cursor.execute(self.comando_sql)
        self.banco.commit()
    
    def inserir_ordem_servico(self, dataHora, estado, total, entrada, num, hab, idC, idV): 
        
        self.comando_sql = "INSERT INTO {} (dataHoraAbertura,estadoOS,valorTotal,valorEntrada,numParcelas,habilitado,idCliente,idVeiculo) VALUES ('{}','{}',{},'{}','{}','{}','{}','{}')".format(self.nome,dataHora,estado,total,entrada,num,hab,idC,idV)
        print(self.comando_sql)
        self.cursor.execute(self.comando_sql)
        self.banco.commit()
    
    def inserir_item_os(self, valorItem, idOS, idF, idS, idP): 
        
        self.comando_sql = "INSERT INTO {} (valorItemOS,idOS,idFuncionario,idServico,idProduto) VALUES ('{}','{}',{},'{}','{}')".format(self.nome,valorItem,idOS,idF,idS,idP)
        self.cursor.execute(self.comando_sql)
        self.banco.commit()
       
    #Filtro de buscas
    def listar_ordem_servico(self, inicio, estado, final, tam, offset): #Busca view v_ordemservico 
        #"select distinct * from v_ordemservico {}".format(estado)
        self.comando_sql = "SELECT * FROM v_ordemservico WHERE {} estadoOS LIKE '{}' {} LIMIT {} OFFSET {}".format(inicio,estado,final,tam,offset)
        self.cursor.execute(self.comando_sql)
        return self.cursor.fetchall()
        
    def listar_parcelas_os(self, id): #Busca view v_ordemservico
        self.comando_sql = "select * from v_parcelas where idOS = {}".format(id)
        self.cursor.execute(self.comando_sql)
        return self.cursor.fetchall()
        
    def buscar_registro_desabilitado(self, coluna, condicao): #Busca nos registros não habilitados
        self.comando_sql = "SELECT * FROM {} WHERE {} LIKE '{}' AND habilitado = 0 LIMIT 10".format(self.nome, coluna, condicao) #Colocar ORDER BY
        self.cursor.execute(self.comando_sql)
        return self.cursor.fetchall()
    
    #Usado nas tabelas e para completar as buscas
    def buscar(self, coluna, condicao):#busca registros habilitados
        self.comando_sql = "SELECT * FROM {} WHERE {} LIKE '{}%' AND habilitado = 1 LIMIT 10".format(self.nome, coluna, condicao) #Colocar ORDER BY
        self.cursor.execute(self.comando_sql)
        return self.cursor.fetchall()
    
    #Buscar registros menos o atual
    def buscar_edicao(self, coluna, condicao, valor):#busca registros habilitados
        self.comando_sql = "SELECT * FROM {} WHERE {} LIKE '{}' AND habilitado = 1 AND {} <> '{}' LIMIT 10".format(self.nome, coluna, condicao, coluna, valor) #Colocar ORDER BY
        self.cursor.execute(self.comando_sql)
        return self.cursor.fetchall()

    #Usado na Paginação
    def buscar_tabela(self, coluna, tamanho, offset):#busca registros habilitados
        self.comando_sql = "SELECT * FROM {} WHERE habilitado = 1 ORDER BY {} ASC LIMIT {} OFFSET {}".format(self.nome, coluna, tamanho, offset)
        self.cursor.execute(self.comando_sql)
        return self.cursor.fetchall()
    '''
    def buscar_tabela_completa(self, coluna):
        self.comando_sql = "SELECT * FROM {} ORDER BY {} ASC".format(self.nome, coluna)
        self.cursor.execute(self.comando_sql)
        return self.cursor.fetchall()
    '''
    def buscar_coluna(self, coluna):
        self.comando_sql = "SELECT {} FROM {}".format(coluna, self.nome)
        self.cursor.execute(self.comando_sql)
        return self.cursor.fetchall()
    
    def selecionar(self, id):
        self.comando_sql = "SELECT * FROM {} WHERE {} = {}".format(self.nome, self.arquivoTabela["nomes_tabelas"][0], id)
        self.cursor.execute(self.comando_sql)
        return self.cursor.fetchone()
    
    def atualizar(self, valores_alterados):
        self.conjunto = ""
        self.contador = 0

        for i in range(self.arquivoTabela["quantidade"]):
            if valores_alterados[i] != "":
                if self.contador != 0:
                    self.conjunto += ","
                self.conjunto += self.arquivoTabela["nomes_tabelas"][i]
                self.conjunto += "="
                self.conjunto += "'" + valores_alterados[i] + "'"
                self.contador += 1
            
        
        self.comando_sql = "UPDATE {} SET {} WHERE {} = {}".format(self.nome, self.conjunto, self.arquivoTabela["nomes_tabelas"][0], valores_alterados[0])
        self.cursor.execute(self.comando_sql)
        self.banco.commit()
    '''
    def deletar(self, id):

        print("CHECAR PENDENCIAS!")

        self.comando_sql = "DELETE FROM {} WHERE {} = {}".format(self.nome, self.arquivoTabela["nomes_tabelas"][0], id)
        self.cursor.execute(self.comando_sql)
        self.banco.commit()
    '''
    def num_registros_tabela(self): # funciona para tabelas que contém o campo habilitado (Cliente, Func, Ser, Prod, Veiculo)
        self.comando_sql = "SELECT COUNT(*) FROM {} WHERE habilitado = 1".format(self.nome)
        self.cursor.execute(self.comando_sql)
        return self.cursor.fetchone()
    
    #Contar registros na view v_ordemservico de acordo com o filtro
    def num_registros_tabela_os(self,inicio,estado,final):
        self.comando_sql = "SELECT COUNT(*) FROM v_ordemservico WHERE {} estadoOS LIKE '{}' {}".format(inicio,estado,final)
        print(self.comando_sql)
        self.cursor.execute(self.comando_sql)
        return self.cursor.fetchone()
    
    # Faz a busca no banco de dados específico para a tabela em relatórios
    def listar_relatorios(self, colunas, filtro):
        self.comando_sql = ("select {} from v_tabela_relatorios {}".format(colunas, filtro))
        self.cursor.execute(self.comando_sql)
        return self.cursor.fetchall()
    
    #Usado para pegar o ID da última ordem de serviço inserida no banco
    def ultimo_id_inserido(self, campo): #Campo ID do último registro inserido em uma tabela,  funciona para tabelas que contém o campo habilitado
        self.comando_sql = "SELECT MAX({}) FROM {} WHERE habilitado = 1".format(campo, self.nome)
        self.cursor.execute(self.comando_sql)
        return self.cursor.fetchone()
    
    def atualizar_campo_habilitado(self, valor_hab, campo, id): #Remover registro de uma tabela
        self.comando_sql = "UPDATE {} SET habilitado = {} WHERE {} = {}".format(self.nome, valor_hab, campo, id)
        self.cursor.execute(self.comando_sql)
        self.banco.commit()

    def pagar_parcela_filtro(self, filtro):
        self.comando_sql = ("update estadoParcela set 'quitada' {}".format(filtro))
        self.cursor.execute(self.comando_sql)
        self.banco.commit()
        
    def listar_relatorios(self, colunas, filtro):
        self.comando_sql = ("select {} "
                            "from v_tabela_relatorios {}".format(colunas, filtro))
        self.cursor.execute(self.comando_sql)
        return self.cursor.fetchall()

    def buscar_filtro(self, colunas, fonte, filtro):
        self.comando_sql = ("select {} from {} {}".format(colunas, fonte, filtro))
        self.cursor.execute(self.comando_sql)
        return self.cursor.fetchall()