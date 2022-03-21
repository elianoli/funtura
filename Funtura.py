
from http.client import INSUFFICIENT_STORAGE
from math import ceil, floor
from pickle import FALSE
import string
import sys
import os
import re
from datetime import date, datetime
from tokenize import String
from typing import List
from PySide6 import QtCore, QtWidgets
import calendar
from qt_core import *
from main_window import UI_MainWindow      
from operacoes_tabela import Tabela
from ValidarCPF import ValidarCPF


#Janela Principal

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Sistema FUNTURA")
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)
        #self.setAttribute(Qt.WA_TranslucentBackground, True)
        #self.setWindowFlag(Qt.FramelessWindowHint)
        
        
        self.removerBotoes() #Botões de Fechar e Minimizar
        self.ajustarVisibilidade() #Visibilidade de botões e frames
        self.ajustarTabelas()
        self.validadoresCamposDouble()
        
        self.valorCaixa = 0
        self.atualizarValorCaixa() #Inserir o primeiro valor de caixa no BD
        
        #self.ui.ui_itemOS.f_adicionar.setShortcut(Qt.Key_Enter)
        #self.ui.ui_pages.frame_19.setEnabled(False)
    
        #Variáveis "globais" para gerenciar inserção de um item
        self.itemOS_id = [] #Lista de listas contendo os ids (idFuncionario,idServico,idProduto,subTotal) para criação do itemOS
        self.itemOS = [] # Apenas para a vizualização dos dados
        self.linhaTabela = 0 #Controle das linhas da tabela de itens da OS. (número de itens também)
        self.id_cliente = ''
        self.id_funcionario = ''
        self.id_servico = '' 
        self.id_produto = ''
        self.subTotal:float = 0
        self.total:float = 0
        
        #Variáveis para guardar campos quanto realizar a EDIÇÃO
        self.campo_referencia = '' #Para IDs
        self.campo_antigo = '' #Para cpf, placa
        
        #Variáveis globais para controle de paginação das tabelas
        self.tam_intervalo = 10 #Quantidade de registros lidos do banco
        self.offset = 0 
        self.num_pagina = 0 #Quantidade de páginas necessárias na paginação 
        self.contador = 0   #Controle das páginas, para não extrapolar para além da quantidade de registros de uma tabela.
        
        self.listarOrdensServicoFiltro() #Primeira chamada sem os filtros

        self.parcela = [] # Variável global de parcela para manipulação no Caixa
        
        
        #### Botões do menu lateral
        
        #Botão Toggle
        self.ui.toggle_button.clicked.connect(self.toggle_button_function)
        #Botão Ordens de Serviço
        self.ui.os_button.clicked.connect(self.show_os_page)
        #Botão clientes
        self.ui.client_button.clicked.connect(self.show_client_page)
        #Botão funcionários
        self.ui.worker_button.clicked.connect(self.show_worker_page)
        #Botão veículos
        self.ui.car_button.clicked.connect(self.show_car_page)
        #Botão produtos
        self.ui.product_button.clicked.connect(self.show_product_page)
        #Botão serviços
        self.ui.service_button.clicked.connect(self.show_service_page)
        #Botão relatórios
        self.ui.report_button.clicked.connect(self.show_report_page)
        #Botão Caixa
        self.ui.finance_button.clicked.connect(self.show_finance_page)
        ###########
        
        
        self.ui.ui_pages.re_visualizar.clicked.connect(self.listarTabelaRelatorios) # !!! Não implementado !!!
        self.ui.ui_pages.re_imprimir.clicked.connect(self.listarTabelaRelatorios) # !!! Não implementado !!!
        self.ui.ui_pages.re_nome.textChanged.connect(self.listarTabelaRelatorios) # A cada mudança no campo nome é atualizada a tabela
        self.ui.ui_pages.re_placa.textChanged.connect(self.listarTabelaRelatorios) # A cada mudança no campo placa é atualizada a tabela
        self.ui.ui_pages.re_data_i.dateChanged.connect(self.checkDatasRelatorios) # A cada mudança no campo data inicial é atualizada a tabela
        self.ui.ui_pages.re_data_f.dateChanged.connect(self.checkDatasRelatorios) # A cada mudança no campo data final é atualizada a tabela
       
       
        #Botões visualizar Ordens de Serviço
        self.ui.ui_pages.tabela_ordem_servico.itemSelectionChanged.connect(self.botaoGerenciarOS)
        self.ui.ui_pages.buscar_os.clicked.connect(self.listarOrdensServicoFiltro)
        self.ui.ui_pages.adicionar_c_filtro.clicked.connect(self.adicionarClienteFiltro)
        self.ui.ui_pages.botao_os_proximo.clicked.connect(lambda: self.botaoProximoTabelas(9))
        self.ui.ui_pages.botao_os_anterior.clicked.connect(lambda: self.botaoAnteriorTabelas(9))
       
        #########Botões Filtro 
        self.ui.ui_pages.checkbox_filtro.stateChanged.connect(self.checkBoxfiltrar)
        self.ui.ui_pages.checkbox_nome.stateChanged.connect(self.checkBoxNome)
        self.ui.ui_pages.checkbox_periodo.stateChanged.connect(self.checkBoxPeriodo)
        self.ui.ui_pages.checkbox_data.stateChanged.connect(self.checkBoxData)
        self.ui.ui_pages.checkbox_mes.stateChanged.connect(self.checkBoxMes)
        self.ui.ui_pages.checkbox_ano.stateChanged.connect(self.checkBoxAno)
        ######Botões cliente selecao
        self.ui.ui_cliente_selecao.buscar_cliente.textChanged.connect(self.listarTabelaClientesSelecao)
        self.ui.ui_cliente_selecao.adicionar.clicked.connect(self.botaoAdicionarCliente)
        self.ui.ui_cliente_selecao.cancelar.clicked.connect(self.botaoCancelarSelecaoCliente)
        self.ui.ui_cliente_selecao.tabela_cliente.itemSelectionChanged.connect(self.clienteSelecionadoTabela)
        self.ui.ui_cliente_selecao.botao_proximo.clicked.connect(lambda: self.botaoProximoTabelas(8))
        self.ui.ui_cliente_selecao.botao_anterior.clicked.connect(lambda: self.botaoAnteriorTabelas(8))
        
        #Botões página OS
        
        self.ui.ui_pages.inserir_item.clicked.connect(self.botaoInserirItem)
        self.ui.ui_pages.remover_item.clicked.connect(self.botaoRemoverItem)
        self.ui.ui_pages.cadastrar_c_os.clicked.connect(self.cadastrarCliente)
        self.ui.ui_pages.cadastrar_v_os.clicked.connect(self.cadastrarVeiculo)
        self.ui.ui_pages.buscar_c_os.textChanged.connect(self.osPreencherCliente)
        self.ui.ui_pages.buscar_v_os.textChanged.connect(self.osPreencherVeiculo)
        self.ui.ui_pages.salvar_os.clicked.connect(self.botaoSalvarOrdemServico)
        self.ui.ui_pages.cancelar_os.clicked.connect(self.botaoCancelarOrdemServico)
        self.ui.ui_pages.visualizar_c_os.clicked.connect(self.visualizarCliente)
        self.ui.ui_pages.valor_entrada.textChanged.connect(self.valorEntradaCampo)
        ### Botões itens OS
        self.ui.ui_itemOS.cancelar.clicked.connect(self.botaoCancelarItemOS)
        self.ui.ui_itemOS.salvar.clicked.connect(self.botaoSalvarItemOS)
        self.ui.ui_itemOS.f_cadastrar.clicked.connect(self.botaoCadastrarFuncionarioItemOS)
        self.ui.ui_itemOS.f_adicionar.clicked.connect(self.botaoAdicionarFuncionarioItemOS)
        self.ui.ui_itemOS.f_remover.clicked.connect(self.botaoRemoverFuncionarioItemOS)
        self.ui.ui_itemOS.s_cadastrar.clicked.connect(self.cadastrarServico)
        self.ui.ui_itemOS.s_adicionar.clicked.connect(self.botaoAdicionarServicoItemOS)
        self.ui.ui_itemOS.tabela_servico.itemDoubleClicked.connect(self.botaoAdicionarServicoItemOS) #Adicionando servico double click
        self.ui.ui_itemOS.s_remover.clicked.connect(self.botaoRemoverServicoItemOS)
        self.ui.ui_itemOS.p_cadastrar.clicked.connect(self.cadastrarProduto)
        self.ui.ui_itemOS.p_adicionar.clicked.connect(self.botaoAdicionarProdutoItemOS)
        self.ui.ui_itemOS.tabela_produto.itemDoubleClicked.connect(self.botaoAdicionarProdutoItemOS) #Adicionando produto double click
        self.ui.ui_itemOS.p_remover.clicked.connect(self.botaoRemoverProdutoItemOS)
        self.ui.ui_itemOS.buscar_funcionario.textChanged.connect(self.osPreencherFuncionario)
        #self.ui.ui_itemOS.buscar_servico.textChanged.connect(self.listarTabelaServicosItemOS)
        #self.ui.ui_itemOS.buscar_produto.textChanged.connect(self.listarTabelaProdutosItemOS)
        self.ui.ui_itemOS.tabWidget_itemOS.currentChanged.connect(self.tabelasItemOSPaginacao) #Paginação das tabelas do itemOS
        self.ui.ui_itemOS.botao_s_proximo.clicked.connect(lambda: self.botaoProximoTabelas(6))
        self.ui.ui_itemOS.botao_s_anterior.clicked.connect(lambda: self.botaoAnteriorTabelas(6))
        self.ui.ui_itemOS.botao_p_proximo.clicked.connect(lambda: self.botaoProximoTabelas(7))
        self.ui.ui_itemOS.botao_p_anterior.clicked.connect(lambda: self.botaoAnteriorTabelas(7))
        
        
        
        #----- Pagamento
        self.ui.ui_pages.vista.clicked.connect(self.pagarVista)
        self.ui.ui_pages.parcelado.clicked.connect(self.pagarParcelado)
        self.ui.ui_pages.num_parcelas.setMinimum(2)
        self.ui.ui_pages.num_parcelas.setMaximum(24)
        self.ui.ui_pages.num_parcelas.setValue(1)#Padrão igual a 1
        self.ui.ui_pages.num_parcelas.setDisabled(True) #Padrão desativado
        self.ui.ui_pages.valor_entrada.setDisabled(True)#Padrão desativado
        self.ui.ui_pages.vista.setChecked(True)
        #------------
        

        '''
        self.ui.ui_pages.os_botao_visualizar.clicked.connect(self.visualizarParcelas)
        self.ui.ui_pages.os_vis_cliente.textChanged.connect(self.listarOS) 
        self.listarOS()
        
        '''
        #Botões da página cliente
        
        self.ui.ui_cliente.botao_salvar.clicked.connect(self.botaoSalvarCliente)
        self.ui.ui_cliente.botao_cancelar.clicked.connect(self.botaoCancelarCliente)
        self.ui.ui_pages.c_botao_cadastrar.clicked.connect(self.cadastrarCliente)
        self.ui.ui_pages.c_botao_editar.clicked.connect(self.botaoEditarCliente)
        self.ui.ui_pages.tabela_clientes.itemDoubleClicked.connect(self.botaoEditarCliente) #Dois cliques no cliente
        self.ui.ui_cliente_edicao.botao_salvar.clicked.connect(self.botaoAtualizarCliente)
        self.ui.ui_cliente_edicao.botao_cancelar.clicked.connect(self.botaoCancelarClienteEdicao)
        self.ui.ui_pages.c_botao_remover.clicked.connect(self.removerCliente)
        self.ui.ui_pages.buscar_cliente.textChanged.connect(self.listarTabelaClientes)
        self.ui.ui_pages.botao_c_proximo.clicked.connect(lambda: self.botaoProximoTabelas(1))
        self.ui.ui_pages.botao_c_anterior.clicked.connect(lambda: self.botaoAnteriorTabelas(1))
        #Cadastro de cliente
        self.ui.ui_cliente.nome.textEdited.connect(self.nomeCliente)
        self.ui.ui_cliente.cpf.textEdited.connect(self.cpfCliente)
        self.ui.ui_cliente.celular.textEdited.connect(self.celularCliente)
        self.ui.ui_cliente.email.textEdited.connect(self.emailCliente)
        #Edição de cliente
        self.ui.ui_cliente.nome.textEdited.connect(self.nomeClienteEdicao)
        self.ui.ui_cliente.cpf.textEdited.connect(self.cpfClienteEdicao)
        self.ui.ui_cliente.celular.textEdited.connect(self.celularClienteEdicao)
        self.ui.ui_cliente.email.textEdited.connect(self.emailClienteEdicao)
        
        
        #Botões da página funcionário
        self.ui.ui_funcionario.botao_salvar.clicked.connect(self.botaoSalvarFuncionario) #Salvar Cadastro
        self.ui.ui_funcionario.botao_cancelar.clicked.connect(self.botaoCancelarFuncionario)
        self.ui.ui_pages.f_botao_cadastrar.clicked.connect(self.cadastrarFuncionario)
        self.ui.ui_pages.f_botao_editar.clicked.connect(self.botaoEditarFuncionario)
        self.ui.ui_pages.tabela_funcionarios.itemDoubleClicked.connect(self.botaoEditarFuncionario)
        self.ui.ui_funcionario_edicao.botao_salvar.clicked.connect(self.botaoAtualizarFuncionario)
        self.ui.ui_funcionario_edicao.botao_cancelar.clicked.connect(self.botaoCancelarFuncionarioEdicao) 
        self.ui.ui_pages.f_botao_remover.clicked.connect(self.removerFuncionario)
        self.ui.ui_pages.buscar_funcionario.textChanged.connect(self.listarTabelaFuncionarios)
        self.ui.ui_pages.botao_f_proximo.clicked.connect(lambda: self.botaoProximoTabelas(2))
        self.ui.ui_pages.botao_f_anterior.clicked.connect(lambda: self.botaoAnteriorTabelas(2))
        #Cadastro de Funcionário
        self.ui.ui_funcionario.nome.textEdited.connect(self.nomeFuncionario)
        self.ui.ui_funcionario.cpf.textEdited.connect(self.cpfFuncionario)
        self.ui.ui_funcionario.celular.textEdited.connect(self.celularFuncionario)
        self.ui.ui_funcionario.email.textEdited.connect(self.emailFuncionario)
        #Edição de Funcionário
        self.ui.ui_funcionario.nome.textEdited.connect(self.nomeFuncionarioEdicao)
        self.ui.ui_funcionario.cpf.textEdited.connect(self.cpfFuncionarioEdicao)
        self.ui.ui_funcionario.celular.textEdited.connect(self.celularFuncionarioEdicao)
        self.ui.ui_funcionario.email.textEdited.connect(self.emailFuncionarioEdicao)
        
        #Botões da página veículos
        
        self.ui.ui_veiculo.botao_salvar.clicked.connect(self.botaoSalvarVeiculo)
        self.ui.ui_veiculo.botao_cancelar.clicked.connect(self.botaoCancelarVeiculo)
        self.ui.ui_pages.v_botao_cadastrar.clicked.connect(self.cadastrarVeiculo)
        self.ui.ui_pages.v_botao_editar.clicked.connect(self.editarVeiculo)
        self.ui.ui_pages.tabela_veiculos.itemDoubleClicked.connect(self.editarVeiculo)
        self.ui.ui_veiculo_edicao.botao_salvar.clicked.connect(self.botaoSalvarAtualizacaoVeiculo) 
        self.ui.ui_veiculo_edicao.botao_cancelar.clicked.connect(self.botaoCancelarVeiculoEdicao)
        self.ui.ui_pages.v_botao_remover.clicked.connect(self.removerVeiculo) 
        self.ui.ui_pages.buscar_veiculo.textChanged.connect(self.listarTabelaVeiculos)
        self.ui.ui_pages.botao_v_proximo.clicked.connect(lambda: self.botaoProximoTabelas(3))
        self.ui.ui_pages.botao_v_anterior.clicked.connect(lambda: self.botaoAnteriorTabelas(3))
        #Cadastro de Veículo
        self.ui.ui_veiculo.placa.textEdited.connect(self.placaVeiculo)
        self.ui.ui_veiculo.marca.textEdited.connect(self.marcaVeiculo)
        self.ui.ui_veiculo.ano_fab.textEdited.connect(self.anoVeiculo)
        #Edição de Veículo
        self.ui.ui_veiculo.placa.textEdited.connect(self.placaVeiculoEdicao)
        self.ui.ui_veiculo.marca.textEdited.connect(self.marcaVeiculoEdicao)
        self.ui.ui_veiculo.ano_fab.textEdited.connect(self.anoVeiculoEdicao)
        
        #Botões da página serviços
        
        self.ui.ui_servico.botao_salvar.clicked.connect(self.botaoSalvarServico)
        self.ui.ui_servico.botao_cancelar.clicked.connect(self.botaoCancelarServico)
        self.ui.ui_pages.s_botao_cadastrar.clicked.connect(self.cadastrarServico)
        self.ui.ui_pages.s_botao_remover.clicked.connect(self.removerServico) 
        self.ui.ui_pages.buscar_servico.textChanged.connect(self.listarTabelaServicos)
        self.ui.ui_pages.botao_s_proximo.clicked.connect(lambda: self.botaoProximoTabelas(4))
        self.ui.ui_pages.botao_s_anterior.clicked.connect(lambda: self.botaoAnteriorTabelas(4))
        self.ui.ui_pages.s_botao_editar.clicked.connect(self.botaoEditarServico)
        self.ui.ui_pages.tabela_servicos.itemDoubleClicked.connect(self.botaoEditarServico)
        self.ui.ui_servico_edicao.botao_salvar.clicked.connect(self.botaoSalvarAtualizacaoServico)
        self.ui.ui_servico_edicao.botao_cancelar.clicked.connect(self.botaoCancelarServicoEdicao)
        
        #Botões da página produtos
        self.ui.ui_pages.gerenciar_os.setEnabled(False)
        self.ui.ui_produto.botao_salvar.clicked.connect(self.botaoSalvarProduto)
        self.ui.ui_produto.botao_cancelar.clicked.connect(self.botaoCancelarProduto)
        self.ui.ui_pages.p_botao_cadastrar.clicked.connect(self.cadastrarProduto)
        self.ui.ui_pages.p_botao_remover.clicked.connect(self.removerProduto)  
        self.ui.ui_pages.buscar_produto.textChanged.connect(self.listarTabelaProdutos)
        self.ui.ui_pages.botao_p_proximo.clicked.connect(lambda: self.botaoProximoTabelas(5))
        self.ui.ui_pages.botao_p_anterior.clicked.connect(lambda: self.botaoAnteriorTabelas(5)) 
        self.ui.ui_pages.p_botao_editar.clicked.connect(self.botaoEditarProduto)
        self.ui.ui_pages.tabela_produtos.itemDoubleClicked.connect(self.botaoEditarProduto)
        self.ui.ui_produto_edicao.botao_salvar.clicked.connect(self.botaoSalvarAtualizacaoProduto)
        self.ui.ui_produto_edicao.botao_cancelar.clicked.connect(self.botaoCancelarProdutoEdicao)
        
        
        
        # Botões da página caixa
        self.ui.ui_pages.ca_botao_efetuar.clicked.connect(self.movimentarCaixa)
        self.ui.ui_pages.ca_receber_p.clicked.connect(self.mostrarReceberParcela)
        self.ui.ui_pages.ca_pagar_f.clicked.connect(print("self.ui.ui_pages.ca_pagar_f.clicked.connect()")) # !!!
        self.ui.ui_pages.desfazer_mov.clicked.connect(print("self.ui.ui_pages.desfazer_mov.clicked.connect()")) # !!!
        self.ui.ui_pages.btn_anterior.clicked.connect(print("self.ui.ui_pages.btn_anterior.clicked.connect()")) # !!!
        self.ui.ui_pages.btn_proximo.clicked.connect(print("self.ui.ui_pages.btn_proximo.clicked.connect()")) # !!!

        self.ui.ui_receber_parcela.line_os.textChanged.connect(self.ajustarTabelaReceberParcela)
        self.ui.ui_receber_parcela.btn_procurar.clicked.connect(self.mostrarProcurarOS)
        self.ui.ui_receber_parcela.btn_pagar.clicked.connect(self.btnPagarParcela)
        self.ui.ui_receber_parcela.btn_cancelar.clicked.connect(self.fecharReceberParcela)
        self.ui.ui_receber_parcela.btn_anterior.clicked.connect(print("self.ui.ui_receber_parcela.btn_anterior.clicked.connect()")) # !!!
        self.ui.ui_receber_parcela.btn_proximo.clicked.connect(print("self.ui.ui_receber_parcela.btn_proximo.clicked.connect()")) # !!!

        self.ui.ui_procurar_os.line_cliente.textChanged.connect(self.ajustarTabelaProcurarOS)
        self.ui.ui_procurar_os.btn_selecionar.clicked.connect(self.btnSelecionarOS)
        self.ui.ui_procurar_os.btn_cancelar.clicked.connect(self.fecharProcurarOS)
        self.ui.ui_procurar_os.btn_anterior.clicked.connect(print("self.ui.ui_procurar_os.btn_anterior.clicked.connect()")) # !!!
        self.ui.ui_procurar_os.btn_proximo.clicked.connect(print("self.ui.ui_procurar_os.btn_proximo.clicked.connect()")) # !!!

        self.ui.ui_pagar_parcela.btn_pagar.clicked.connect(print("self.ui.ui_pagar_parcela.btn_pagar.clicked.connect")) # !!!
        self.ui.ui_pagar_parcela.btn_cancelar.clicked.connect(self.fecharPagarParcela)
        
        #Exibe a janela
        self.show() 

    
    def clienteSelecionadoTabela(self): 
        self.ui.ui_cliente_selecao.adicionar.setEnabled(True)
    
    def botaoCancelarSelecaoCliente(self):
        self.ui.cliente_selecao.close()
    
    
    def botaoAdicionarCliente(self):
        linha = self.ui.ui_cliente_selecao.tabela_cliente.currentRow()
        self.id_cliente = self.ui.ui_cliente_selecao.tabela_cliente.item(linha,0).text() #ID
        self.ui.ui_pages.nome_cliente_filtro.setText(self.ui.ui_cliente_selecao.tabela_cliente.item(linha,1).text()) #Nome
        self.ui.cliente_selecao.close()
    
    def adicionarClienteFiltro(self):
        self.ui.ui_cliente_selecao.adicionar.setEnabled(False)
        self.listarTabelaClientesSelecao()
        self.contador = 0
        self.offset = 0
        self.ui.cliente_selecao.show()
    
    def listarOrdensServicoFiltro(self):
        self.ui.ui_pages.tabela_ordem_servico.clearSelection()
        self.ui.ui_pages.tabela_ordem_servico.reset() 
        
        nomeTabela = "ordemservico"
        tabela = Tabela("tabelas.yaml", nomeTabela)
        columns = 8
        campos_numericos = [1,2,3,5,6,7] #Para ajustar o alinhamento na tabela
        inicio = ''
        final = ''
        
        if self.ui.ui_pages.checkbox_nome.isChecked():
            if self.ui.ui_pages.nome_cliente_filtro.text() == '':
                print("Adicionar nome do cliente!")
            else:
                id = self.id_cliente
                inicio = "idCliente = '{}' AND".format(id)
        else:
            inicio = '' #Para buscar todos nomes no banco
            
        estado_os = self.ui.ui_pages.estado_os_filtro.currentText()
        print(estado_os)
        
        if self.ui.ui_pages.checkbox_nenhum.isChecked():
            final = ''
        else:
            
            if self.ui.ui_pages.checkbox_periodo.isChecked(): #Período
                data_de = datetime.strptime(self.ui.ui_pages.data_de.text(), '%d/%m/%Y').strftime('%Y-%m-%d')
                data_ate = datetime.strptime(self.ui.ui_pages.data_ate.text(), '%d/%m/%Y').strftime('%Y-%m-%d')
                final = "AND date(dataHoraAbertura) >= '{}' AND date(dataHoraAbertura) <= '{}'".format(data_de,data_ate)
                
            if self.ui.ui_pages.checkbox_data.isChecked(): #Data específica
                data= datetime.strptime(self.ui.ui_pages.data_os.text(), '%d/%m/%Y').strftime('%Y-%m-%d')
                final = "AND date(dataHoraAbertura) = '{}'".format(data)
                
            if self.ui.ui_pages.checkbox_mes.isChecked():
                mes = self.ui.ui_pages.mes_os.currentIndex() + 1 #Começa em 0 por isso +1
                final = "AND month(dataHoraAbertura) = '{}'".format(mes) 
                
            if self.ui.ui_pages.checkbox_ano.isChecked():
                ano = self.ui.ui_pages.ano_os.text()
                final = "AND year(dataHoraAbertura) = '{}'".format(ano) 
       
        self.num_pagina = ceil(self.numeroRegistrosTabelaOrdemServico(inicio,estado_os,final)/self.tam_intervalo)      
        os:List = tabela.listar_ordem_servico(inicio, estado_os, final,self.tam_intervalo, self.offset)
        
        tam = len(os)
        self.ui.ui_pages.tabela_ordem_servico.setRowCount(tam)
        
        for i in range(0,tam):
            for j in range(0, columns):  
                item = QTableWidgetItem(str(os[i][j])) 
                if j in campos_numericos:
                    item.setTextAlignment(Qt.AlignRight)
                    self.ui.ui_pages.tabela_ordem_servico.setItem(i,j,item)
                else:
                    item.setTextAlignment(Qt.AlignLeft)
                    self.ui.ui_pages.tabela_ordem_servico.setItem(i,j,item) 
        

    
    def botaoGerenciarOS(self):
        self.ui.ui_pages.gerenciar_os.setEnabled(True)

    
    def ajustarVisibilidade(self):
        self.ui.ui_cliente_selecao.adicionar.setEnabled(False)
        self.ui.ui_pages.buscar_os.setEnabled(False)
        self.ui.ui_pages.frame_filtro.setEnabled(False)
        self.ui.ui_pages.nome_cliente_filtro.setEnabled(False)
        self.ui.ui_pages.data_de.setEnabled(False)
        self.ui.ui_pages.data_ate.setEnabled(False)
        self.ui.ui_pages.data_os.setEnabled(False)
        self.ui.ui_pages.mes_os.setEnabled(False)
        self.ui.ui_pages.ano_os.setEnabled(False)
        self.ui.ui_pages.adicionar_c_filtro.setEnabled(False) 
        self.ui.ui_pages.checkbox_nenhum.setChecked(True)
        data_atual = datetime.now()
        self.ui.ui_pages.data_de.setDate(data_atual)
        self.ui.ui_pages.data_ate.setDate(data_atual)
        self.ui.ui_pages.data_os.setDate(data_atual)
        
    def checkBoxfiltrar(self):
        
        if self.ui.ui_pages.checkbox_filtro.isChecked():
            self.ui.ui_pages.buscar_os.setEnabled(True)
            self.ui.ui_pages.frame_filtro.setEnabled(True)
        else:
            self.ui.ui_pages.checkbox_nenhum.setChecked(True)
            data_atual = datetime.now()
            self.ui.ui_pages.data_de.setDate(data_atual)
            self.ui.ui_pages.data_ate.setDate(data_atual)
            self.ui.ui_pages.data_os.setDate(data_atual)
            self.ui.ui_pages.mes_os.setCurrentIndex(0)
            self.ui.ui_pages.estado_os_filtro.setCurrentIndex(0)
            self.ui.ui_pages.buscar_os.setEnabled(False)
            self.ui.ui_pages.frame_filtro.setEnabled(False)
            self.listarOrdensServicoFiltro()
        self.ui.ui_pages.gerenciar_os.setEnabled(False)
            
    def checkBoxNome(self):
        if self.ui.ui_pages.checkbox_nome.isChecked():
            self.ui.ui_pages.nome_cliente_filtro.setEnabled(True)
            self.ui.ui_pages.adicionar_c_filtro.setEnabled(True)
        else:
            self.ui.ui_pages.nome_cliente_filtro.clear()
            self.ui.ui_pages.nome_cliente_filtro.setEnabled(False)
            self.ui.ui_pages.adicionar_c_filtro.setEnabled(False)  
            
    def checkBoxPeriodo(self):
        if self.ui.ui_pages.checkbox_periodo.isChecked():
            self.ui.ui_pages.data_de.setEnabled(True)
            self.ui.ui_pages.data_ate.setEnabled(True)
        else:
            self.ui.ui_pages.data_de.setEnabled(False)
            self.ui.ui_pages.data_ate.setEnabled(False)
            
    def checkBoxData(self):
        if self.ui.ui_pages.checkbox_data.isChecked():
            self.ui.ui_pages.data_os.setEnabled(True)
        else:
            self.ui.ui_pages.data_os.setEnabled(False)
            
    def checkBoxMes(self):
        if self.ui.ui_pages.checkbox_mes.isChecked():
            self.ui.ui_pages.mes_os.setEnabled(True)
        else:
            self.ui.ui_pages.mes_os.setEnabled(False)
            
    def checkBoxAno(self):
        if self.ui.ui_pages.checkbox_ano.isChecked():
            self.ui.ui_pages.ano_os.setEnabled(True)
        else:
            self.ui.ui_pages.ano_os.setEnabled(False)
        
    def removerBotoes(self):
        '''
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(9)
        shadow.setColor(QColor(0, 0, 0, 0))
        shadow.setOffset(4.0)
        self.ui.cliente.setGraphicsEffect(shadow)
        '''
        #Remove a barra de botões (fechar, minimizar, maximizar)
        self.ui.cliente.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.cliente_edicao.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.funcionario.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.funcionario_edicao.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.veiculo.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.veiculo_edicao.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.produto.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.produto_edicao.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.servico.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.servico_edicao.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.itemOS.setWindowFlag(Qt.FramelessWindowHint)   
         
    #Valor de entrada da ordem de serviço
    def valorEntradaCampo(self):
        self.ui.ui_pages.valor_entrada.setStyleSheet('border-radius: 5px; border: 0.5px solid #44475a; font:11pt "MS Shell Dlg 2";padding: 1px;')
    #Cadastro de Cliente
    def nomeCliente(self):
        self.ui.ui_cliente.nome.setStyleSheet("border-color: #44475a") 
    def cpfCliente(self):   
        self.ui.ui_cliente.cpf.setStyleSheet("border-color: #44475a")        
    def celularCliente(self):
        self.ui.ui_cliente.celular.setStyleSheet("border-color: #44475a")
    def emailCliente(self):
        self.ui.ui_cliente.email.setStyleSheet("border-color: #44475a")
    #Edição de Cliente
    def nomeClienteEdicao(self):
        self.ui.ui_cliente_edicao.nome.setStyleSheet("border-color: #44475a") 
    def cpfClienteEdicao(self):   
        self.ui.ui_cliente_edicao.cpf.setStyleSheet("border-color: #44475a")        
    def celularClienteEdicao(self):
        self.ui.ui_cliente_edicao.celular.setStyleSheet("border-color: #44475a")
    def emailClienteEdicao(self):
        self.ui.ui_cliente_edicao.email.setStyleSheet("border-color: #44475a")
    #Cadastro de Funcionário
    def nomeFuncionario(self):
        self.ui.ui_funcionario.nome.setStyleSheet("border-color: #44475a") 
    def cpfFuncionario(self):   
        self.ui.ui_funcionario.cpf.setStyleSheet("border-color: #44475a")        
    def celularFuncionario(self):
        self.ui.ui_funcionario.celular.setStyleSheet("border-color: #44475a")
    def emailFuncionario(self):
        self.ui.ui_funcionario.email.setStyleSheet("border-color: #44475a")
    #Edição de Funcionário
    def nomeFuncionarioEdicao(self):
        self.ui.ui_funcionario_edicao.nome.setStyleSheet("border-color: #44475a") 
    def cpfFuncionarioEdicao(self):   
        self.ui.ui_funcionario_edicao.cpf.setStyleSheet("border-color: #44475a")        
    def celularFuncionarioEdicao(self):
        self.ui.ui_funcionario_edicao.celular.setStyleSheet("border-color: #44475a")
    def emailFuncionarioEdicao(self):
        self.ui.ui_funcionario_edicao.email.setStyleSheet("border-color: #44475a")    
    #Cadastro de Veículo
    def placaVeiculo(self):
        self.ui.ui_veiculo.placa.setStyleSheet("border-color: #44475a") 
    def marcaVeiculo(self):   
        self.ui.ui_veiculo.marca.setStyleSheet("border-color: #44475a")        
    def anoVeiculo(self):
        self.ui.ui_veiculo.ano_fab.setStyleSheet("border-color: #44475a")
    #Edição de Veículo
    def placaVeiculoEdicao(self):
        self.ui.ui_veiculo_edicao.placa.setStyleSheet("border-color: #44475a") 
    def marcaVeiculoEdicao(self):   
        self.ui.ui_veiculo_edicao.marca.setStyleSheet("border-color: #44475a")        
    def anoVeiculoEdicao(self):
        self.ui.ui_veiculo_edicao.ano_fab.setStyleSheet("border-color: #44475a")
    
    
    # Método auxiliar no processo de paginação das tabelas  
    def numeroRegistrosTabela(self, nome_tabela):
        nomeTabela = nome_tabela
        tabela = Tabela("tabelas.yaml", nomeTabela)
        num_registros = tabela.num_registros_tabela()
        num_registros = int(num_registros[0])
        
        return num_registros 
      
    #Para a tabela de ordem servico
    def numeroRegistrosTabelaOrdemServico(self,inicio,estado,final):
        nomeTabela = "ordemservico"
        tabela = Tabela("tabelas.yaml", nomeTabela)
        num_registros = tabela.num_registros_tabela_os(inicio,estado,final)
        num_registros = int(num_registros[0])
        return num_registros
    
    
    def validarCamposString(self, msg): #Função auxiliar usada na validação dos campos nomes (Clientes e Funcionários)
        msg = msg.replace(" ","")
        if msg.isalpha():
            print("Contém apenas letras")
            return 0
        if msg.isnumeric():
            print("Contém números")
            return 1
        if msg.isalnum():
            print("Contém letras e números")
            return 2
    
    def validarCamposCadastroCF(self, dados, opcao): #Validação dos campos de cadastro de clientes e funcionários
        validado = 1
        
        if opcao == 1:
            nomeTabela = "cliente"
            tabela = Tabela("tabelas.yaml", nomeTabela) 
            nome = tabela.buscar("nomeC", dados[0]) #Busca o nome nos clientes habilitados
            cpf = tabela.buscar("cpfC", dados[1]) #Busca o cpf nos clientes habilitados
            #nome_nao_hab = tabela.buscar_registro_desabilitado("nomeC", dados[0])
            cpf_nao_hab = tabela.buscar_registro_desabilitado("cpfC", dados[1])
            
        elif opcao == 2:
            nomeTabela = "funcionario"
            tabela = Tabela("tabelas.yaml", nomeTabela) 
            nome = tabela.buscar("nomeF", dados[0])
            cpf = tabela.buscar("cpfF", dados[1])
            #nome_nao_hab = tabela.buscar_registro_desabilitado("nomeF", dados[0])
            cpf_nao_hab = tabela.buscar_registro_desabilitado("cpfF", dados[1])
            
        if dados[0] != '':
            '''
            if len(nome_nao_hab) != 0: #Existe um nome já cadastrado nos não habilitados
                validado = 0
                
                if opcao == 1: #cliente
                    msg = QMessageBox.question(self.ui.cliente,"Confirmação","Este cliente está excluído.Deseja reabilitá-lo?",QMessageBox.Yes|QMessageBox.No)
            
                    if msg == QMessageBox.Yes: #Sim
                        tabela.atualizar_campo_habilitado(1,"idCliente",nome_nao_hab[0][0])
                        self.listarTabelaClientes()
                        self.ui.cliente.close()
                elif opcao == 2: #funcionário
                    msg = QMessageBox.question(self.ui.cliente,"Confirmação","Este funcionário está excluído.Deseja reabilitá-lo?",QMessageBox.Yes|QMessageBox.No)
            
                    if msg == QMessageBox.Yes: #Sim
                        tabela.atualizar_campo_habilitado(1,"idFuncionario",nome_nao_hab[0][0])
                        self.listarTabelaFuncionarios()
                        self.ui.funcionario.close()
            ''' 
            '''  
            if len(nome) == 0: #Verifica se já existe um nome igual 
                print("Nome válido!")
            else:
                validado = 0
                print("Nome já cadastrado!")
            '''
            if self.validarCamposString(dados[0]) != 0: #Nome não possuí apenas letras
                validado = 0
                if opcao == 1:
                    self.ui.ui_cliente.nome.setStyleSheet("border: 2px solid red;") 
                elif opcao == 2:
                    self.ui.ui_funcionario.nome.setStyleSheet("border: 2px solid red;")
                print("Nome rejeitado")
        else:
            validado = 0
            if opcao == 1:
                    self.ui.ui_cliente.nome.setStyleSheet("border: 2px solid red;") 
            elif opcao == 2:
                    self.ui.ui_funcionario.nome.setStyleSheet("border: 2px solid red;")
            print("Nome não preenchido")  
              
        #Validar e-mail
        if dados[5] != '':
            padrao = r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
            if bool(re.match(padrao, dados[5])) == True:
                print("E-mail válido!")
            else:
                validado = 0
                if opcao == 1:
                    self.ui.ui_cliente.email.setStyleSheet("border: 2px solid red;") 
                elif opcao == 2:
                    self.ui.ui_funcionario.email.setStyleSheet("border: 2px solid red;")
                print("E-mail inválido!")
                
        #Validar CPF
        if len(dados[1]) == 14:
            
            if len(cpf_nao_hab) != 0: #Existe um cpf salvo nos registros desabilitados
                validado = 0
                if opcao == 1: #cliente
                    msg = QMessageBox.question(self.ui.cliente,"Confirmação","Este cliente está excluído.Deseja reabilitá-lo?",QMessageBox.Yes|QMessageBox.No)
            
                    if msg == QMessageBox.Yes: #Sim
                        tabela.atualizar_campo_habilitado(1,"idCliente",cpf_nao_hab[0][0])
                        self.listarTabelaClientes()
                        self.ui.cliente.close()
                        
                elif opcao == 2: #funcionário
                    msg = QMessageBox.question(self.ui.funcionario,"Confirmação","Este funcionário está excluído.Deseja reabilitá-lo?",QMessageBox.Yes|QMessageBox.No)
            
                    if msg == QMessageBox.Yes: #Sim
                        tabela.atualizar_campo_habilitado(1,"idFuncionario",cpf_nao_hab[0][0])
                        self.listarTabelaFuncionarios()
                        self.ui.funcionario.close()
                
            if len(cpf) == 0: # Registros habilitados
                print("CPF ainda não cadastrado")
            else:
                validado = 0
                if opcao == 1:
                    self.ui.ui_cliente.cpf.setStyleSheet("border: 2px solid red;") 
                elif opcao == 2:
                    self.ui.ui_funcionario.cpf.setStyleSheet("border: 2px solid red;")
                print("CPF já existente")
                
            if ValidarCPF(dados[1]).validar() == True: #Valida o CPF
                print("CPF válido")
            else:
                validado = 0
                if opcao == 1:
                    self.ui.ui_cliente.cpf.setStyleSheet("border: 2px solid red;") 
                elif opcao == 2:
                    self.ui.ui_funcionario.cpf.setStyleSheet("border: 2px solid red;")
                print("CPF inválido")
        else:
            validado = 0
            if opcao == 1:
                    self.ui.ui_cliente.cpf.setStyleSheet("border: 2px solid red;") 
            elif opcao == 2:
                    self.ui.ui_funcionario.cpf.setStyleSheet("border: 2px solid red;")
            print("CPF incompleto!") 
            
        #Validar Telefone  
        if len(dados[4]) != 15:
            validado = 0
            if opcao == 1:
                    self.ui.ui_cliente.celular.setStyleSheet("border: 2px solid red;") 
            elif opcao == 2:
                    self.ui.ui_funcionario.celular.setStyleSheet("border: 2px solid red;")
            print("Telefone incompleto!")
        
        #Validar data de nascimento
        data = datetime.strptime(dados[3], '%Y-%m-%d').strftime('%Y-%m-%d')
        data_atual = datetime.now().strftime('%Y-%m-%d')
        if data >= data_atual:
            validado = 0
            print("Data futura!")
        else:
            print("Data válida!")
        
        return validado
    
    
    def validarCamposEdicaoCF(self, dados, opcao): #Validação dos campos de edição de clientes e funcionários
        #opcao == 1 -> Cliente, opcao == 2 -> Funcionário#
        validado = 1
        if opcao == 1:
            nomeTabela = "cliente"
            tabela = Tabela("tabelas.yaml", nomeTabela) 
            c_nao_hab = tabela.buscar_registro_desabilitado("cpfC", dados[2])
            c_edicao = tabela.buscar_edicao("cpfC", dados[2], self.campo_antigo)
            
        elif opcao == 2:
            nomeTabela = "funcionario"
            tabela = Tabela("tabelas.yaml", nomeTabela) 
            c_nao_hab = tabela.buscar_registro_desabilitado("cpfF", dados[2])
            c_edicao = tabela.buscar_edicao("cpfF", dados[2], self.campo_antigo) #Ver se existe cpf 
        
        if dados[1] != '':
            if self.validarCamposString(dados[1]) != 0: #Nome não possuí apenas letras
                validado = 0
                print("Nome rejeitado")
                if opcao == 1: #Cliente
                    self.ui.ui_cliente_edicao.nome.setStyleSheet("border: 2px solid red;") 
                elif opcao == 2: #Funcionario
                    self.ui.ui_funcionario_edicao.nome.setStyleSheet("border: 2px solid red;")
        else:
            validado = 0
            print("Nome não preenchido")   
            if opcao == 1: #Cliente
                self.ui.ui_cliente_edicao.nome.setStyleSheet("border: 2px solid red;") 
            elif opcao == 2: #Funcionario
                self.ui.ui_funcionario_edicao.nome.setStyleSheet("border: 2px solid red;") 
        #Validar e-mail
        if dados[6] != '':
            padrao = r"/^[a-z0-9.]+@[a-z0-9]+.([a-z]+)?$/i"
            if bool(re.match(padrao, dados[6])) == True:
                print("E-mail válido!")
            else:
                validado = 0
                print("E-mail inválido!")
                if opcao == 1: #Cliente
                    self.ui.ui_cliente_edicao.email.setStyleSheet("border: 2px solid red;") 
                elif opcao == 2: #Funcionario
                    self.ui.ui_funcionario_edicao.email.setStyleSheet("border: 2px solid red;")
                
        #Validar CPF
        if len(dados[2]) == 14: 
            if len(c_nao_hab) != 0: #Existe um cpf salvo nos registros desabilitados
                validado = 0
                if opcao == 1: #cliente
                    msg = QMessageBox.question(self.ui.cliente,"Confirmação","Este cliente está excluído.Deseja reabilitá-lo?",QMessageBox.Yes|QMessageBox.No)
            
                    if msg == QMessageBox.Yes: #Sim
                        tabela.atualizar_campo_habilitado(1,"idCliente",c_nao_hab[0][0])
                        self.listarTabelaClientes()
                        self.ui.cliente_edicao.close()
                        
                elif opcao == 2: #funcionário
                    msg = QMessageBox.question(self.ui.funcionario,"Confirmação","Este funcionário está excluído.Deseja reabilitá-lo?",QMessageBox.Yes|QMessageBox.No)
            
                    if msg == QMessageBox.Yes: #Sim
                        tabela.atualizar_campo_habilitado(1,"idFuncionario",c_nao_hab[0][0])
                        self.listarTabelaFuncionarios()
                        self.ui.funcionario_edicao.close()
            
            if len(c_edicao) == 0: # Registros habilitados
                print("CPF ainda não cadastrado")
            else:
                validado = 0
                if opcao == 1: #Cliente
                    self.ui.ui_cliente_edicao.cpf.setStyleSheet("border: 2px solid red;") 
                elif opcao == 2: #Funcionario
                    self.ui.ui_funcionario_edicao.cpf.setStyleSheet("border: 2px solid red;")
                print("CPF já existente - Edição")
                
               
            if ValidarCPF(dados[2]).validar() == True: #Valida o CPF
                print("CPF válido")
            else:
                validado = 0
                print("CPF inválido")
                if opcao == 1: #Cliente
                    self.ui.ui_cliente_edicao.cpf.setStyleSheet("border: 2px solid red;") 
                elif opcao == 2: #Funcionario
                    self.ui.ui_funcionario_edicao.cpf.setStyleSheet("border: 2px solid red;")
        else:
            validado = 0
            print("CPF incompleto!")
            if opcao == 1: #Cliente
                self.ui.ui_cliente_edicao.cpf.setStyleSheet("border: 2px solid red;") 
            elif opcao == 2: #Funcionario
                self.ui.ui_funcionario_edicao.cpf.setStyleSheet("border: 2px solid red;")
            
        #Validar Celular
        if len(dados[5]) != 15:
            validado = 0
            print("Telefone incompleto!")
            if opcao == 1: #Cliente
                self.ui.ui_cliente_edicao.celular.setStyleSheet("border: 2px solid red;") 
            elif opcao == 2: #Funcionario
                self.ui.ui_funcionario_edicao.celular.setStyleSheet("border: 2px solid red;")
        
        #Validar data de nascimento
        data = datetime.strptime(dados[4], '%Y-%m-%d').strftime('%Y-%m-%d')
        data_atual = datetime.now().strftime('%Y-%m-%d')
        if data >= data_atual:
            validado = 0
            print("Data futura!")
        else:
            print("Data válida!")
           
        return validado
    
    def validarCamposSP(self, dados, opcao): #Validar campos do cadastro de serviços e produtos
        #Obrigatório o campo nome estar preenchido 
        if opcao == 1: #Janela de Cadastro
            nome = dados[0]
        elif opcao == 2: #Janela de Edição
            nome = dados[1]
        if nome == '':
            print("Preencher o nome!") 
            return 0
        else:
            return 1
        
    def validarCamposVeiculo(self, dados, opcao):
        nomeTabela = "veiculo"
        tabela = Tabela("tabelas.yaml", nomeTabela) 
        validado = 1
        if opcao == 1: #Cadastro
            #dados = (placa,ano,cor,marca,desc)
            placa_dados = dados[0]
            placa_hab = tabela.buscar("placa", dados[0])
            v_nao_hab = tabela.buscar_registro_desabilitado("placa", dados[0])
            v_edicao = tabela.buscar_edicao("placa", dados[0], self.campo_antigo)
            marca = dados[3]
            ano_fab = dados[1]
            
        elif opcao == 2: #Edição 
            #dados = (self.campo_referencia,placa,ano_fab,cor,marca,desc)
            placa_dados = dados[1]
            placa_hab = tabela.buscar("placa", dados[1])
            v_nao_hab = tabela.buscar_registro_desabilitado("placa", dados[1])
            v_edicao = tabela.buscar_edicao("placa", dados[1],self.campo_antigo)
            marca = dados[4]
            ano_fab = dados[2]
        
        if placa_dados == '': #Não foi inserida a placa
            print("Preencher a placa!")
            validado = 0
            if opcao == 1:
                self.ui.ui_veiculo.placa.setStyleSheet("border: 2px solid red;") 
            elif opcao == 2:
                self.ui.ui_veiculo_edicao.placa.setStyleSheet("border: 2px solid red;")
        
        #Quando o veículo está excluido  
        if len(v_nao_hab) == 0:
            print("Veículo válido! - não existe nos excluídos")
        else:
            print("Veículo inválido! - existe nos excluídos")
            validado = 0
            msg = QMessageBox.question(self.ui.veiculo,"Confirmação","Deseja reabilitá-lo?",QMessageBox.Yes|QMessageBox.No)
            
            if msg == QMessageBox.Yes: #Sim
                tabela.atualizar_campo_habilitado(1,"idVeiculo",v_nao_hab[0][0])
                self.listarTabelaVeiculos()
                if opcao == 1:
                    self.ui.veiculo.close()
                elif opcao == 2:  
                    self.ui.veiculo_edicao.close()
        
        #Quando o veículo está habilitado e já existe um cadastro com a placa inserida
        if opcao == 1: #Só para Cadastro, para edição a placa vai existir
            if len(placa_hab) == 0:
                print("Veículo válido")        
            else:
                validado = 0
                print("Veículo já Cadastrado!") 
                self.ui.ui_veiculo.placa.setStyleSheet("border: 2px solid red;") 
        elif opcao == 2: #Edição
            if len(v_edicao) == 0:
                print("Veículo válido - Edição")        
            else:
                validado = 0
                print("Veículo já Cadastrado!") 
                self.ui.ui_veiculo_edicao.placa.setStyleSheet("border: 2px solid red;") 
              
        if marca == '':
            validado = 0
            print("Preencher marca!")
            if opcao == 1:
                self.ui.ui_veiculo.marca.setStyleSheet("border: 2px solid red;") 
            elif opcao == 2:
                self.ui.ui_veiculo_edicao.marca.setStyleSheet("border: 2px solid red;")
        
        if len(ano_fab) < 4  or (int(ano_fab) < 1780):
            validado = 0
            print("Ano inválido!")
            if opcao == 1:
                self.ui.ui_veiculo.ano_fab.setStyleSheet("border: 2px solid red;") 
            elif opcao == 2:
                self.ui.ui_veiculo_edicao.ano_fab.setStyleSheet("border: 2px solid red;")
            
        return validado
     
    # ------------------- Ordens de Serviço --------------------
        
    def botaoCancelarItemOS(self):
        self.id_funcionario = ''
        self.id_produto = ''
        self.id_servico = ''
        self.subTotal = 0
        self.itemOS.clear()
        self.itemOS_id.clear()
        self.ui.itemOS.close()
    
    def verificarCamposItemOS(self):   
        
        #Obrigatório inserir o funcionário e o serviço
        
        if self.ui.ui_itemOS.printar_funcionario.text() == '':
            print("Preencher Funcionário!")
            return 0
        if  self.ui.ui_itemOS.printar_servico.text() == '':
            print("Preencher Serviço!")
            return 0
        
        return 1
      
    def botaoSalvarItemOS(self):
            
        if self.verificarCamposItemOS() == 1:
        
            funcionario = self.ui.ui_itemOS.printar_funcionario.text() 
            servico = self.ui.ui_itemOS.printar_servico.text() 
            produto = self.ui.ui_itemOS.printar_produto.text()     
            
            self.total += self.subTotal
            item_id = [self.id_funcionario,self.id_servico,self.id_produto, self.subTotal]
            self.subTotal = 0
            
            item = [funcionario, servico, produto]
            self.itemOS_id.append(item_id)
            self.itemOS.append(item)
            
            self.ui.ui_pages.tabela_itens.insertRow(self.linhaTabela)
            
            for i in range(0, 1):
                for j in range(0, 3):
                    self.ui.ui_pages.tabela_itens.setItem(self.linhaTabela,j,QtWidgets.QTableWidgetItem(item[j]))
            
            self.ui.ui_pages.total.setText(str(self.total))
            self.linhaTabela += 1
            
            print("Total:", self.total)
            print("SubTotal:", self.subTotal)          
            self.ui.itemOS.close()
            
    
    def botaoRemoverItem(self):
        linha = self.ui.ui_pages.tabela_itens.currentRow()

        if linha == -1: #Nenhum nome foi selecionado
            resp = QMessageBox.information(self, 'Seleção','Selecione um item!')
            return
        
        resp = QMessageBox.question(self, 'Remover itemOS','Deseja remover o item?',QMessageBox.Yes|QMessageBox.No)
        
        if resp == QMessageBox.Yes:
            self.total -= self.itemOS_id[linha][3] #total menos o subtotal do item
            self.ui.ui_pages.total.setText(str(self.total))
            
            self.itemOS_id.pop(linha)
            self.ui.ui_pages.tabela_itens.removeRow(linha)
            self.linhaTabela -= 1
            self.ui.ui_pages.tabela_itens.reset()
                       
            
    def botaoInserirItem(self):
        self.restaurarJanelaItemOS()
        self.listarTabelaServicosItemOS()
        self.listarTabelaProdutosItemOS()
        #self.ui.ui_itemOS.f_adicionar.setEnabled(False)
        self.ui.itemOS.show()
    
    def botaoCadastrarFuncionarioItemOS(self):
        self.ui.funcionario.show()
    
    def botaoRemoverFuncionarioItemOS(self):
        self.id_funcionario = ''
        self.ui.ui_itemOS.printar_funcionario.clear()
        self.ui.ui_itemOS.funcionario.clear()
    
    def validarFuncionarioItemOS(self):
        nome_funcionario = self.ui.ui_itemOS.buscar_funcionario.text()
        if nome_funcionario == '':
            print("Preencher o nome do Funcionário!")
            return 0
        else: #Quando coloca-se um nome que não existe no Banco de Dados
            nomeTabela = "funcionario"
            tabela= Tabela("tabelas.yaml", nomeTabela)
            funcionarios:List = tabela.buscar("nomeF", nome_funcionario)
            if funcionarios == []:
                print("Funcionário não encontrado!")
                return 0
            else:
                self.id_funcionario = funcionarios[0][0] #Adiciona o ID do funcionário
                return 1
    
    def botaoAdicionarFuncionarioItemOS(self):
        
        if self.validarFuncionarioItemOS() == 1:
        
            nome_funcionario = self.ui.ui_itemOS.buscar_funcionario.text()
            self.ui.ui_itemOS.printar_funcionario.setText(nome_funcionario)
            self.ui.ui_itemOS.funcionario.setText(nome_funcionario)
            self.ui.ui_itemOS.buscar_funcionario.clear()  
    
            
    def osPreencherFuncionario(self):
        
        nomeTabela = "funcionario"
        tab_funcionario = Tabela("tabelas.yaml", nomeTabela)
        funcionario = []
        
        if self.ui.ui_itemOS.buscar_funcionario.cursorPosition() >= 1:
            #self.ui.ui_itemOS.f_adicionar.setEnabled(True)
            nome = self.ui.ui_itemOS.buscar_funcionario.text()
            funcionarios = tab_funcionario.buscar("nomeF", nome)
            
            if len(funcionarios) > 0:
                for i in range(len(funcionarios)):
                    funcionario.append(funcionarios[i][1])
                
                completer = QCompleter(funcionario)
                self.ui.ui_itemOS.buscar_funcionario.setCompleter(completer) 
                
    def listarTabelaServicosItemOS(self):
        nomeTabela = "servico"
        tab_servico = Tabela("tabelas.yaml", nomeTabela)
        columns = 4
        campos_numericos = [0,2]
        servicos = []

        self.ui.ui_itemOS.tabela_servico.reset() #Limpar a seleção da tabela cliente
        
        if self.ui.ui_itemOS.buscar_servico.text() == "":
            servicos = tab_servico.buscar_tabela("nomeServico", self.tam_intervalo, self.offset)
        else:
            string = self.ui.ui_itemOS.buscar_servico.text()
        
            servicos = tab_servico.buscar("nomeServico", string)
            
        self.ui.ui_itemOS.tabela_servico.setRowCount(len(servicos))
        tam = len(servicos)
        
        for i in range(0,tam):
            for j in range(0, columns):
                item = QTableWidgetItem(str(servicos[i][j]))
                if j in campos_numericos:
                    item.setTextAlignment(Qt.AlignRight)
                    self.ui.ui_itemOS.tabela_servico.setItem(i,j,item)
                else:
                    item.setTextAlignment(Qt.AlignLeft)
                    self.ui.ui_itemOS.tabela_servico.setItem(i,j,item)
    
    def listarTabelaProdutosItemOS(self):
        nomeTabela = "produto"
        tabela = Tabela("tabelas.yaml", nomeTabela)
        columns = 4
        campos_numericos = [0,2]
        produto = []

        self.ui.ui_itemOS.tabela_produto.reset() #Limpar a seleção da tabela cliente
        
        if self.ui.ui_itemOS.buscar_produto.text() == "":
            produtos = tabela.buscar_tabela("nomeProduto", self.tam_intervalo, self.offset)
        else:
            string = self.ui.ui_itemOS.buscar_produto.text()
        
            produtos = tabela.buscar("nomeProduto", string)
            
        self.ui.ui_itemOS.tabela_produto.setRowCount(len(produtos))
        tam = len(produtos)
        
        for i in range(0,tam):
            for j in range(0, columns):
                item = QTableWidgetItem(str(produtos[i][j]))
                if j in campos_numericos:
                    item.setTextAlignment(Qt.AlignRight)
                    self.ui.ui_itemOS.tabela_produto.setItem(i,j,item)
                else:
                    item.setTextAlignment(Qt.AlignLeft)
                    self.ui.ui_itemOS.tabela_produto.setItem(i,j,item)
    
    def botaoAdicionarServicoItemOS(self):
        self.ui.ui_itemOS.tabela_servico.clearSelection()
        nomeTabela = "servico"
        tabela = Tabela("tabelas.yaml", nomeTabela)
        linha = self.ui.ui_itemOS.tabela_servico.currentRow()
        if linha != -1: #Algum servico foi selecionado
            self.id_servico = self.ui.ui_itemOS.tabela_servico.item(linha,0).text()
            nome = self.ui.ui_itemOS.tabela_servico.item(linha,1).text()
            valor = self.ui.ui_itemOS.tabela_servico.item(linha,2).text()
            desc = self.ui.ui_itemOS.tabela_servico.item(linha,3).text() 
            
            self.subTotal += float(valor)  #Adicionar valor do serviço          
            msg = nome + ' | ' + valor + ' | ' + desc
            self.ui.ui_itemOS.printar_servico.setText(msg)
            self.ui.ui_itemOS.servico.setText(msg)
            self.ui.ui_itemOS.subtotal.setText(str(self.subTotal))
            
            
        
    def botaoRemoverServicoItemOS(self):
        nomeTabela = "servico"
        tabela = Tabela("tabelas.yaml", nomeTabela)
        if self.ui.ui_itemOS.printar_servico != '':
            servico = tabela.selecionar(self.id_servico)
            valor = servico[2]
            self.subTotal -= valor
        self.id_servico = ''
        self.ui.ui_itemOS.printar_servico.clear()
        self.ui.ui_itemOS.servico.clear()
        self.ui.ui_itemOS.subtotal.setText(str(self.subTotal))
     
     
    def botaoAdicionarProdutoItemOS(self):
        self.ui.ui_itemOS.tabela_produto.clearSelection()
        nomeTabela = "produto"
        tabela = Tabela("tabelas.yaml", nomeTabela)
        linha = self.ui.ui_itemOS.tabela_produto.currentRow()
        
        if linha != -1: #Algum servico foi selecionado
            self.id_produto = self.ui.ui_itemOS.tabela_produto.item(linha,0).text()
            nome = self.ui.ui_itemOS.tabela_produto.item(linha,1).text()
            valor = self.ui.ui_itemOS.tabela_produto.item(linha,2).text()
            desc = self.ui.ui_itemOS.tabela_produto.item(linha,3).text()
            
            self.subTotal += float(valor) #Adicionar valor do produto
            
            msg = nome + ' | ' + valor + ' | ' + desc
            self.ui.ui_itemOS.printar_produto.setText(msg)
            self.ui.ui_itemOS.produto.setText(msg)
            self.ui.ui_itemOS.subtotal.setText(str(self.subTotal))
        
    def botaoRemoverProdutoItemOS(self):
        nomeTabela = "produto"
        tabela = Tabela("tabelas.yaml", nomeTabela)
        if self.ui.ui_itemOS.printar_produto != '':
            produto = tabela.selecionar(self.id_produto)
            valor = produto[2]
            self.subTotal -= valor
        self.id_produto = ''
        self.ui.ui_itemOS.printar_produto.clear()  
        self.ui.ui_itemOS.produto.clear()   
        self.ui.ui_itemOS.subtotal.setText(str(self.subTotal))   
         
    def restaurarJanelaItemOS(self):
        
        self.ui.ui_itemOS.tabWidget_itemOS.setCurrentIndex(0) #Inicia em funcionário 
        self.ui.ui_itemOS.funcionario.clear()
        self.ui.ui_itemOS.servico.clear()
        self.ui.ui_itemOS.produto.clear()
        
        self.ui.ui_itemOS.printar_funcionario.clear()
        self.ui.ui_itemOS.printar_servico.clear()
        self.ui.ui_itemOS.printar_produto.clear() 
        self.ui.ui_itemOS.subtotal.clear() 
          
        self.ui.ui_itemOS.buscar_funcionario.clear()
        self.ui.ui_itemOS.buscar_servico.clear()
        self.ui.ui_itemOS.buscar_produto.clear()
        
       
    def tabelasItemOSPaginacao(self):
        self.contador = 0
        self.offset = 0
        if self.ui.ui_itemOS.tabWidget_itemOS.currentIndex() == 1: #Serviço
            self.num_pagina = ceil(self.numeroRegistrosTabela("servico")/self.tam_intervalo)
            self.ui.ui_itemOS.buscar_servico.clear()
            self.listarTabelaServicosItemOS()
            return
        
        if self.ui.ui_itemOS.tabWidget_itemOS.currentIndex() == 2: #Produto
            self.num_pagina = ceil(self.numeroRegistrosTabela("produto")/self.tam_intervalo)
            self.ui.ui_itemOS.buscar_produto.clear()
            self.listarTabelaProdutosItemOS()
            return    
    
    def limparCamposOrdemServico(self):
        self.ui.ui_pages.buscar_c_os.clear()
        self.ui.ui_pages.buscar_v_os.clear()
        self.ui.ui_pages.vista.setChecked(True)
        self.pagarVista()
        self.ui.ui_pages.tabela_itens.setRowCount(0)
        self.ui.ui_pages.tabela_itens.clearContents()
        self.ui.ui_pages.total.clear()
    
    def validarCamposOrdemServico(self):
        validado = 1
        #Validação do cliente
        nome_cliente = self.ui.ui_pages.buscar_c_os.text()
        if nome_cliente == '':
            validado = 0
            print("Preencher o nome do Cliente!")
            self.ui.ui_pages.buscar_c_os.setStyleSheet("border: 2px solid red;") 
        else:
            nomeTabela = "cliente"
            tabela= Tabela("tabelas.yaml", nomeTabela)
            clientes:List = tabela.buscar("nomeC", nome_cliente)
            if clientes == []:
                validado = 0
                print("Cliente não encontrado!")
                self.ui.ui_pages.buscar_c_os.setStyleSheet("border: 2px solid red;") 
                
        placa = self.ui.ui_pages.buscar_v_os.text()
        if placa == '':
            validado = 0
            print("Preencher a placa do Veículo!")
            self.ui.ui_pages.buscar_v_os.setStyleSheet("border: 2px solid red;") 
        else:
            nomeTabela = "veiculo"
            tabela= Tabela("tabelas.yaml", nomeTabela)
            veiculos:List = tabela.buscar("placa", placa)
            if veiculos == []:
                validado = 0
                print("Veículo não encontrado!")
                self.ui.ui_pages.buscar_v_os.setStyleSheet("border: 2px solid red;") 
            
        #Nenhum item foi inserido
        if self.linhaTabela == 0: 
            validado = 0
            print("Nenhum item foi inserido!")
        #Quando o valor de entrada é maior que o valor total da ordem de serviço
        if self.ui.ui_pages.parcelado.isChecked():
            if self.ui.ui_pages.valor_entrada.text() == '':
                validado = 0
                print("Preencher valor de entrada!")
                self.ui.ui_pages.valor_entrada.setStyleSheet('border-radius: 5px; border: 2px solid red; font:11pt "MS Shell Dlg 2";padding: 1px;') 
            else:
                if self.ui.ui_pages.total.text() != '':
                    if float(self.ui.ui_pages.valor_entrada.text().replace(",",".")) > float(self.ui.ui_pages.total.text()):
                        validado = 0    
                        print("Valor de entrada maior que o Total!")
                        self.ui.ui_pages.valor_entrada.setStyleSheet('border-radius: 5px; border: 2px solid red; font:11pt "MS Shell Dlg 2";padding: 1px;') 
                
        return validado
        
    def botaoSalvarOrdemServico(self):
        #ID do cliente (precisa verificar a inserção de clientes com mesmo nome)
        
        print(self.ui.ui_pages.vista.isChecked())
        '''
        if self.validarCamposOrdemServico() == 1:
            self.limparCamposOrdemServico() #Ao clicar em salvar, após a validação dos dados, limpa-se os campos
            nomeTabela = "cliente"
            tabela= Tabela("tabelas.yaml", nomeTabela)
            
            cliente = self.ui.ui_pages.buscar_c_os.text()
            clientes = tabela.buscar("nomeC", cliente)
            id_cliente = clientes[0][0]
            
            #Placa do veículo
            nomeTabela = "veiculo"
            tabela= Tabela("tabelas.yaml", nomeTabela)
            
            placa = self.ui.ui_pages.buscar_v_os.text()
            veiculos = tabela.buscar("placa", placa )
            id_veiculo = veiculos[0][0]
            
            nomeTabela = "ordemservico"
            tabela= Tabela("tabelas.yaml", nomeTabela)

            
            if self.ui.ui_pages.vista.isChecked() == True: #A vista
                valor_entrada = 0
                num_parcelas = 0
                print("Entrou vista")
            elif self.ui.ui_pages.parcelado.isChecked() == True:
                valor_entrada = float(self.ui.ui_pages.valor_entrada.text().replace(",","."))
                num_parcelas = int(self.ui.ui_pages.num_parcelas.text())
                print("Entrou parcelado")
            
            if self.ui.ui_pages.total.text() != '': #Quando não tem itens adicionados
                total_OS = float(self.ui.ui_pages.total.text())
                print("Entrou total")
            else:
                total_OS = 0
                print("Entrou total 0")
            
            estado_OS = 'ABERTA'
            hab = 1 #habilitado
            datahora_abertura = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            print(datahora_abertura,estado_OS,total_OS,valor_entrada,num_parcelas,hab,id_cliente,id_veiculo)
            
            tabela.inserir_ordem_servico(datahora_abertura,estado_OS,total_OS,valor_entrada,num_parcelas,hab,id_cliente,id_veiculo)
            
            id_OS = int(tabela.ultimo_id_inserido("idOS")[0])

            #inserção dos itens da ordem de serviço
            nomeTabela = "itemos"
            tabela= Tabela("tabelas.yaml", nomeTabela)
        
            for i in range(0, self.linhaTabela):
                total_item = float(self.itemOS_id[i][3])
                idF = int(self.itemOS_id[i][0])
                idS = int(self.itemOS_id[i][1])
                idP = int(self.itemOS_id[i][2])
                tabela.inserir_item_os(total_item,id_OS,idF,idS,idP)
        '''    
            
        
        
    def botaoCancelarOrdemServico(self):
        self.limparCamposOrdemServico()
        
    # ----------------------------------------------------------
    

    # ----------------------- Cliente -------------------------- 
    
    def restaurarStyleSheetCliente(self):
        self.nomeCliente()
        self.cpfCliente()
        self.celularCliente()
        self.emailCliente()
        
    def restaurarStyleSheetClienteEdicao(self):
        self.nomeClienteEdicao()
        self.cpfClienteEdicao()
        self.celularClienteEdicao()
        self.emailClienteEdicao()
    
    def listarTabelaClientes(self):
        self.ui.ui_pages.tabela_clientes.clearSelection()
        nomeTabela = "cliente"
        tab_cliente = Tabela("tabelas.yaml", nomeTabela)
        columns = 11
        clientes = []
        campos_numericos = [0,2,4,5,10] 
        
        self.ui.ui_pages.tabela_clientes.reset() #Limpar a seleção da tabela cliente
        self.num_pagina = ceil(self.numeroRegistrosTabela("cliente")/self.tam_intervalo)
        
        if self.ui.ui_pages.buscar_cliente.text() == "":
            clientes = tab_cliente.buscar_tabela("nomeC",self.tam_intervalo,self.offset)
        else:
            string = self.ui.ui_pages.buscar_cliente.text()
            clientes = tab_cliente.buscar("nomeC", string)
            
        self.ui.ui_pages.tabela_clientes.setRowCount(len(clientes))
        tam = len(clientes)
        
        for i in range(0,tam):
            for j in range(0, columns):
                item = QTableWidgetItem(str(clientes[i][j]))
                if j in campos_numericos: #Colunas (cpf,dataNasc,telefone,numCasa)
                    item.setTextAlignment(Qt.AlignRight)
                    self.ui.ui_pages.tabela_clientes.setItem(i,j,item)
                else:
                    item.setTextAlignment(Qt.AlignLeft)
                    self.ui.ui_pages.tabela_clientes.setItem(i,j,item)
    
    
    def limparCamposCliente(self):

        self.ui.ui_cliente.nome.clear()
        self.ui.ui_cliente.cpf.clear()
        self.ui.ui_cliente.celular.clear()
        self.ui.ui_cliente.email.clear()
        self.ui.ui_cliente.logradouro.clear()
        self.ui.ui_cliente.cidade.clear()
        self.ui.ui_cliente.bairro.clear()
        self.ui.ui_cliente.numero.clear()
        data = QDate(2000,1,1)
        self.ui.ui_cliente.data_nasc.setDate(data)
        self.ui.ui_cliente.sexo.setCurrentIndex(0)
            
    def limparCamposClienteEdicao(self):
              
        self.ui.ui_cliente_edicao.nome.clear()
        self.ui.ui_cliente_edicao.cpf.clear()
        self.ui.ui_cliente_edicao.celular.clear()
        self.ui.ui_cliente_edicao.email.clear()
        self.ui.ui_cliente_edicao.logradouro.clear()
        self.ui.ui_cliente_edicao.cidade.clear()
        self.ui.ui_cliente_edicao.bairro.clear()
        self.ui.ui_cliente_edicao.numero.clear()
        data = QDate(2000,1,1)
        self.ui.ui_cliente_edicao.data_nasc.setDate(data)
        self.ui.ui_cliente_edicao.sexo.setCurrentIndex(0)
    
       
    def botaoSalvarCliente(self, dados):
        
        nomeTabela = "cliente"
        tabela = Tabela("tabelas.yaml", nomeTabela)    
        #Falta verificar os campos obrigatórios (Nome, CPF, celular)  
        
        nome = (self.ui.ui_cliente.nome.text()).strip()
        cpf = self.ui.ui_cliente.cpf.text()
        cel = self.ui.ui_cliente.celular.text()
        email = (self.ui.ui_cliente.email.text()).strip()
        cidade = (self.ui.ui_cliente.cidade.text()).strip()
        logradouro = (self.ui.ui_cliente.logradouro.text()).strip()
        bairro = (self.ui.ui_cliente.bairro.text()).strip()
        num_casa = (self.ui.ui_cliente.numero.text()).strip()
        data_nasc = self.ui.ui_cliente.data_nasc.date().toString(Qt.ISODate)
        sexo = self.ui.ui_cliente.sexo.currentText()
        habilitado = 1
            
        dados = (nome,cpf,sexo,data_nasc,cel,email,logradouro,cidade,bairro,num_casa,habilitado)
        
        if self.validarCamposCadastroCF(dados, 1) == 1:
            tabela.inserir(dados)      
            self.limparCamposCliente()
            self.listarTabelaClientes()
            self.ui.cliente.close()
    
    def cadastrarCliente(self):
        self.limparCamposCliente()
        self.restaurarStyleSheetCliente()
        self.ui.cliente.show()
    
    
    def botaoCancelarCliente(self):
        self.limparCamposCliente()
        self.restaurarStyleSheetCliente()
        self.ui.ui_pages.tabela_clientes.clearSelection()
        self.ui.ui_pages.tabela_clientes.reset()
        self.ui.cliente.close()
        
    def botaoCancelarClienteEdicao(self):
        self.limparCamposClienteEdicao()
        self.restaurarStyleSheetClienteEdicao()
        self.ui.ui_pages.tabela_clientes.clearSelection()
        self.ui.ui_pages.tabela_clientes.reset()
        self.ui.cliente_edicao.close()
    
    def botaoAtualizarCliente(self):
        
        nomeTabela = "cliente"
        tabela = Tabela("tabelas.yaml", nomeTabela) 
                  
        nome = self.ui.ui_cliente_edicao.nome.text()
        cpf = self.ui.ui_cliente_edicao.cpf.text() 
        cel = self.ui.ui_cliente_edicao.celular.text()
        email = self.ui.ui_cliente_edicao.email.text()
        cidade = self.ui.ui_cliente_edicao.cidade.text()
        logradouro = self.ui.ui_cliente_edicao.logradouro.text()
        bairro = self.ui.ui_cliente_edicao.bairro.text()
        num_casa = self.ui.ui_cliente_edicao.numero.text()
        data_nasc = self.ui.ui_cliente_edicao.data_nasc.date().toString(Qt.ISODate)
        sexo = self.ui.ui_cliente_edicao.sexo.currentText()
        hab = '1'
        dados = (self.campo_referencia,nome,cpf,sexo,data_nasc,cel,email,logradouro,cidade,bairro,num_casa,hab)
        
        if self.validarCamposEdicaoCF(dados,1) == 1:
            tabela.atualizar(dados)
            self.campo_referencia = ''
            self.campo_antigo = ''
            self.listarTabelaClientes()
            self.ui.cliente_edicao.close()
        
    def osPreencherCliente(self):
        
        self.ui.ui_pages.buscar_c_os.setStyleSheet("border-color: #44475a") 
        nomeTabela = "cliente"
        tabela = Tabela("tabelas.yaml", nomeTabela)
        cliente = []
        
        if self.ui.ui_pages.buscar_c_os.cursorPosition() >= 1:
            nome = self.ui.ui_pages.buscar_c_os.text()
            clientes = tabela.buscar("nomeC", nome)
            
            if len(clientes) > 0:
                for i in range(len(clientes)):
                    cliente.append(clientes[i][1])
                
                completer = QCompleter(cliente)
                
                self.ui.ui_pages.buscar_c_os.setCompleter(completer)    
    
    def botaoEditarCliente(self):
        
        nomeTabela = "cliente"
        tab_cliente = Tabela("tabelas.yaml", nomeTabela)        
        linha = self.ui.ui_pages.tabela_clientes.currentRow()

        if linha == -1: #Nenhum nome foi selecionado
            resp = QMessageBox.information(self, 'Seleção','Selecione um cliente!')
        else:
            id = self.ui.ui_pages.tabela_clientes.item(linha,0).text()
            cpf = self.ui.ui_pages.tabela_clientes.item(linha,2).text()
            
            self.ui.ui_cliente_edicao.nome.setText(self.ui.ui_pages.tabela_clientes.item(linha,1).text())
            self.ui.ui_cliente_edicao.cpf.setText(self.ui.ui_pages.tabela_clientes.item(linha,2).text())
            data = self.ui.ui_pages.tabela_clientes.item(linha,4).text()
            data = datetime.strptime(data, '%Y-%m-%d').date()
            self.ui.ui_cliente_edicao.data_nasc.setDate(data)
            self.ui.ui_cliente_edicao.celular.setText(self.ui.ui_pages.tabela_clientes.item(linha,5).text())
            self.ui.ui_cliente_edicao.email.setText(self.ui.ui_pages.tabela_clientes.item(linha,6).text())
            self.ui.ui_cliente_edicao.logradouro.setText(self.ui.ui_pages.tabela_clientes.item(linha,7).text())
            self.ui.ui_cliente_edicao.cidade.setText(self.ui.ui_pages.tabela_clientes.item(linha,8).text())
            self.ui.ui_cliente_edicao.bairro.setText(self.ui.ui_pages.tabela_clientes.item(linha,9).text())
            self.ui.ui_cliente_edicao.numero.setText(self.ui.ui_pages.tabela_clientes.item(linha,10).text())
            if self.ui.ui_pages.tabela_clientes.item(linha,3).text() == "Masculino":
                self.ui.ui_cliente_edicao.sexo.setCurrentIndex(0)
            else:
                self.ui.ui_cliente_edicao.sexo.setCurrentIndex(1)
            
            self.campo_referencia = id
            self.campo_antigo = cpf
            self.restaurarStyleSheetClienteEdicao()
            self.ui.cliente_edicao.show()
        
    def removerCliente(self):
        nomeTabela = "cliente"
        tabela = Tabela("tabelas.yaml", nomeTabela)    
        linha = self.ui.ui_pages.tabela_clientes.currentRow()

        if linha == -1: #Nenhum nome foi selecionado
            resp = QMessageBox.information(self, 'Seleção','Selecione um cliente!')
        else:
            msg = QMessageBox.question(self.ui.cliente,"Confirmação","Confirma a remoção?",QMessageBox.Yes|QMessageBox.No)
            if msg == QMessageBox.Yes:
                id = self.ui.ui_pages.tabela_clientes.item(linha,0).text()
                tabela.atualizar_campo_habilitado(0,"idCliente",id)
                self.listarTabelaClientes()
            
    def visualizarCliente(self):
        nomeTabela = "cliente"
        tabela = Tabela("tabelas.yaml", nomeTabela) 
        
        nome_cliente = self.ui.ui_pages.buscar_c_os.text()
        cliente = tabela.buscar("nomeC", nome_cliente)
        
        if nome_cliente == '':
            print("Preencher nome!")
            self.ui.ui_pages.buscar_c_os.setStyleSheet("border: 2px solid red;") 
        else:
            if len(cliente) == 0:
                print("Cliente não encontrado!")
                self.ui.ui_pages.buscar_c_os.setStyleSheet("border: 2px solid red;") 
            else:
                #dados = (self.campo_referencia,nome,cpf,sexo,data_nasc,cel,email,logradouro,cidade,bairro,num_casa,hab)
                self.ui.ui_cliente_vizualizacao.nome.setText(cliente[0][1])
                self.ui.ui_cliente_vizualizacao.cpf.setText(cliente[0][2])
                self.ui.ui_cliente_vizualizacao.sexo.setText(cliente[0][3])
                data = datetime.strftime(cliente[0][4], '%d/%m/%Y')
                self.ui.ui_cliente_vizualizacao.data_nasc.setText(data) 
                self.ui.ui_cliente_vizualizacao.celular.setText(cliente[0][5])
                self.ui.ui_cliente_vizualizacao.email.setText(cliente[0][6])
                self.ui.ui_cliente_vizualizacao.logradouro.setText(cliente[0][7])
                self.ui.ui_cliente_vizualizacao.cidade.setText(cliente[0][8])
                self.ui.ui_cliente_vizualizacao.bairro.setText(cliente[0][9])
                self.ui.ui_cliente_vizualizacao.numero.setText(cliente[0][10])
                self.ui.cliente_vizualizacao.show() 
                
    # ----------------------------------------------------------
    
    # ------------------ Funcionário ---------------------------
    def restaurarStyleSheetFuncionario(self):
        self.nomeFuncionario()
        self.cpfFuncionario()
        self.celularFuncionario()
        self.emailFuncionario()
        
    def restaurarStyleSheetFuncionarioEdicao(self):
        self.nomeFuncionarioEdicao()
        self.cpfFuncionarioEdicao()
        self.celularFuncionarioEdicao()
        self.emailFuncionarioEdicao()
    
    def listarTabelaFuncionarios(self):
        self.ui.ui_pages.tabela_funcionarios.clearSelection()
        self.ui.ui_pages.tabela_funcionarios.reset()
        
        nomeTabela = "funcionario"
        tabela = Tabela("tabelas.yaml", nomeTabela)
        columns = 11
        funcionarios = []
        campos_numericos = [0,2,4,5,10] 
      
        #self.ui.ui_pages.tabela_funcionarios.reset() #Limpar a seleção da tabela cliente
        self.num_pagina = ceil(self.numeroRegistrosTabela("funcionario")/self.tam_intervalo)
        
        if self.ui.ui_pages.buscar_funcionario.text() == "":
            funcionarios = tabela.buscar_tabela("nomeF", self.tam_intervalo, self.offset)
        else:
            string = self.ui.ui_pages.buscar_funcionario.text()
            funcionarios = tabela.buscar("nomeF", string)
            
        self.ui.ui_pages.tabela_funcionarios.setRowCount(len(funcionarios))
        tam = len(funcionarios)
        
        for i in range(0,tam):
            for j in range(0, columns):
                item = QTableWidgetItem(str(funcionarios[i][j]))
                if j in campos_numericos: #Colunas (cpf,dataNasc,telefone,numCasa)
                    item.setTextAlignment(Qt.AlignRight)
                    self.ui.ui_pages.tabela_funcionarios.setItem(i,j,item)
                else:
                    item.setTextAlignment(Qt.AlignLeft)
                    self.ui.ui_pages.tabela_funcionarios.setItem(i,j,item)
        
    def limparCamposFuncionario(self):
        
        self.ui.ui_funcionario.nome.clear()
        self.ui.ui_funcionario.cpf.clear()
        self.ui.ui_funcionario.celular.clear()
        self.ui.ui_funcionario.email.clear()
        self.ui.ui_funcionario.logradouro.clear()
        self.ui.ui_funcionario.cidade.clear()
        self.ui.ui_funcionario.bairro.clear()
        self.ui.ui_funcionario.numero.clear()
        data = QDate(2000,1,1)
        self.ui.ui_funcionario.data_nasc.setDate(data)
        self.ui.ui_funcionario.sexo.setCurrentIndex(0)

    def limparCamposFuncionarioEdicao(self):
        
        self.ui.ui_funcionario_edicao.nome.clear()
        self.ui.ui_funcionario_edicao.cpf.clear()
        self.ui.ui_funcionario_edicao.celular.clear()
        self.ui.ui_funcionario_edicao.email.clear()
        self.ui.ui_funcionario_edicao.logradouro.clear()
        self.ui.ui_funcionario_edicao.cidade.clear()
        self.ui.ui_funcionario_edicao.bairro.clear()
        self.ui.ui_funcionario_edicao.numero.clear()
        data = QDate(2000,1,1)
        self.ui.ui_funcionario_edicao.data_nasc.setDate(data)
        self.ui.ui_funcionario_edicao.sexo.setCurrentIndex(0)
    
    def botaoCancelarFuncionario(self):
        self.limparCamposFuncionario()
        self.restaurarStyleSheetFuncionario()
        self.ui.ui_pages.tabela_funcionarios.clearSelection()
        self.ui.ui_pages.tabela_funcionarios.reset()
        self.ui.funcionario.close()
    
    def botaoCancelarFuncionarioEdicao(self):
        self.limparCamposFuncionarioEdicao()
        self.restaurarStyleSheetFuncionarioEdicao()
        self.ui.ui_pages.tabela_funcionarios.clearSelection()
        self.ui.ui_pages.tabela_funcionarios.reset()
        self.ui.funcionario_edicao.close()
   
    def botaoSalvarFuncionario(self):
        
        nomeTabela = "funcionario"
        tabela = Tabela("tabelas.yaml", nomeTabela)    
        #Falta verificar os campos obrigatórios (Nome, CPF, celular)  
        
        nome = self.ui.ui_funcionario.nome.text()
        cpf = self.ui.ui_funcionario.cpf.text()
        cel = self.ui.ui_funcionario.celular.text()
        email = self.ui.ui_funcionario.email.text()
        cidade = self.ui.ui_funcionario.cidade.text()
        logradouro = self.ui.ui_funcionario.logradouro.text()
        bairro = self.ui.ui_funcionario.bairro.text()
        num_casa = self.ui.ui_funcionario.numero.text()
        data_nasc = self.ui.ui_funcionario.data_nasc.date().toString(Qt.ISODate)
        sexo = self.ui.ui_funcionario.sexo.currentText()
        habilitado = 1
        
        dados = (nome,cpf,sexo,data_nasc,cel,email,logradouro,cidade,bairro,num_casa,habilitado)
        
        if self.validarCamposCadastroCF(dados, 2) == 1:
            tabela.inserir(dados)       
            self.limparCamposFuncionario()
            self.listarTabelaFuncionarios()
            self.ui.funcionario.close()
    
    def cadastrarFuncionario(self):
        self.limparCamposFuncionario()
        self.restaurarStyleSheetFuncionario()
        self.ui.funcionario.show()
    
    def botaoEditarFuncionario(self):
        
        nomeTabela = "funcionario"
        tabela = Tabela("tabelas.yaml", nomeTabela)        
        linha = self.ui.ui_pages.tabela_funcionarios.currentRow()

        if linha == -1: #Nenhum nome foi selecionado
            resp = QMessageBox.information(self, 'Seleção','Selecione um cliente!')
        else:
            id = self.ui.ui_pages.tabela_funcionarios.item(linha,0).text()
            cpf = self.ui.ui_pages.tabela_funcionarios.item(linha,2).text()
            #funcionario = tabela.selecionar(id)
            self.ui.ui_funcionario_edicao.nome.setText(self.ui.ui_pages.tabela_funcionarios.item(linha,1).text())
            self.ui.ui_funcionario_edicao.cpf.setText(self.ui.ui_pages.tabela_funcionarios.item(linha,2).text())
            data = self.ui.ui_pages.tabela_funcionarios.item(linha,4).text()
            data = datetime.strptime(data, '%Y-%m-%d').date()
            self.ui.ui_funcionario_edicao.data_nasc.setDate(data)
            self.ui.ui_funcionario_edicao.celular.setText(self.ui.ui_pages.tabela_funcionarios.item(linha,5).text())
            self.ui.ui_funcionario_edicao.email.setText(self.ui.ui_pages.tabela_funcionarios.item(linha,6).text())
            self.ui.ui_funcionario_edicao.logradouro.setText(self.ui.ui_pages.tabela_funcionarios.item(linha,7).text())
            self.ui.ui_funcionario_edicao.cidade.setText(self.ui.ui_pages.tabela_funcionarios.item(linha,8).text())
            self.ui.ui_funcionario_edicao.bairro.setText(self.ui.ui_pages.tabela_funcionarios.item(linha,9).text())
            self.ui.ui_funcionario_edicao.numero.setText(self.ui.ui_pages.tabela_funcionarios.item(linha,10).text())
            if self.ui.ui_pages.tabela_funcionarios.item(linha,3).text() == "Masculino":
                self.ui.ui_funcionario_edicao.sexo.setCurrentIndex(0)
            else:
                self.ui.ui_funcionario_edicao.sexo.setCurrentIndex(1)
            
            self.campo_referencia = id
            self.campo_antigo = cpf
            self.restaurarStyleSheetFuncionarioEdicao()
            self.ui.funcionario_edicao.show()
    
    def botaoAtualizarFuncionario(self):
        
        nomeTabela = "funcionario"
        tabela = Tabela("tabelas.yaml", nomeTabela) 
                  
        nome = self.ui.ui_funcionario_edicao.nome.text()
        cpf = self.ui.ui_funcionario_edicao.cpf.text() 
        cel = self.ui.ui_funcionario_edicao.celular.text()
        email = self.ui.ui_funcionario_edicao.email.text()
        cidade = self.ui.ui_funcionario_edicao.cidade.text()
        logradouro = self.ui.ui_funcionario_edicao.logradouro.text()
        bairro = self.ui.ui_funcionario_edicao.bairro.text()
        num_casa = self.ui.ui_funcionario_edicao.numero.text()
        data_nasc = self.ui.ui_funcionario_edicao.data_nasc.date().toString(Qt.ISODate)
        sexo = self.ui.ui_funcionario_edicao.sexo.currentText()
        hab = '1'
        dados = (self.campo_referencia,nome,cpf,sexo,data_nasc,cel,email,logradouro,cidade,bairro,num_casa,hab)
        
        if self.validarCamposEdicaoCF(dados,2) == 1:
            tabela.atualizar(dados) 
            self.campo_referencia = ''
            self.campo_antigo = ''
            self.listarTabelaFuncionarios()
            self.ui.funcionario_edicao.close()
    
    
    def removerFuncionario(self):
        nomeTabela = "funcionario"
        tabela = Tabela("tabelas.yaml", nomeTabela)    
        linha = self.ui.ui_pages.tabela_funcionarios.currentRow()

        if linha == -1: #Nenhum nome foi selecionado
            resp = QMessageBox.information(self, 'Seleção','Selecione um funcionário!')
        else:
            msg = QMessageBox.question(self.ui.funcionario,"Confirmação","Confirma a remoção?",QMessageBox.Yes|QMessageBox.No)
            if msg == QMessageBox.Yes:
                id = self.ui.ui_pages.tabela_funcionarios.item(linha,0).text()
                tabela.atualizar_campo_habilitado(0,"idFuncionario",id)
                self.listarTabelaFuncionarios()
    
     
    def listarTabelaClientesSelecao(self):
        
        self.ui.ui_cliente_selecao.tabela_cliente.clearSelection()
        self.ui.ui_cliente_selecao.tabela_cliente.reset() 
        self.ui.ui_cliente_selecao.adicionar.setEnabled(False)
        
        nomeTabela = "cliente"
        tabela = Tabela("tabelas.yaml", nomeTabela)
        columns = 3
        clientes = []
        campos_numericos = [0,2,3] 
        
        
        self.num_pagina = ceil(self.numeroRegistrosTabela("cliente")/self.tam_intervalo)
        
        if self.ui.ui_cliente_selecao.buscar_cliente.text() == "":
            clientes = tabela.buscar_tabela("nomeC",self.tam_intervalo,self.offset)
        else:
            string = self.ui.ui_cliente_selecao.buscar_cliente.text()
            clientes = tabela.buscar("nomeC", string)
            
        self.ui.ui_cliente_selecao.tabela_cliente.setRowCount(len(clientes))
        tam = len(clientes)
        
        for i in range(0,tam):
            for j in range(0, columns):
                item = QTableWidgetItem(str(clientes[i][j]))
                if j in campos_numericos: 
                    item.setTextAlignment(Qt.AlignRight)
                    self.ui.ui_cliente_selecao.tabela_cliente.setItem(i,j,item)
                else:
                    item.setTextAlignment(Qt.AlignLeft)
                    self.ui.ui_cliente_selecao.tabela_cliente.setItem(i,j,item)
            celular =  QTableWidgetItem(str(clientes[i][5]))
            celular.setTextAlignment(Qt.AlignRight)
            self.ui.ui_cliente_selecao.tabela_cliente.setItem(i,3,celular) #Inserção do celular
              
    #-----------------------------------------------------------
    
    # ---------------------- Veículo ---------------------------
    
    def restaurarStyleSheetVeiculo(self):
        self.placaVeiculo()
        self.marcaVeiculo()
        self.anoVeiculo()
    
    def restaurarStyleSheetVeiculoEdicao(self):
        self.placaVeiculoEdicao()
        self.marcaVeiculoEdicao()
        self.anoVeiculoEdicao()    
    
    def listarTabelaVeiculos(self):
        self.ui.ui_pages.tabela_veiculos.clearSelection()
        self.ui.ui_pages.tabela_veiculos.reset() #Limpar a seleção da tabela veículos
        
        nomeTabela = "veiculo"
        tab_veiculo = Tabela("tabelas.yaml", nomeTabela)
        columns = 6
        campos_numericos= [0,1,2]
        veiculos = []
        
        
        self.num_pagina = ceil(self.numeroRegistrosTabela("veiculo")/self.tam_intervalo)
    
        if self.ui.ui_pages.buscar_veiculo.text() == "":
            veiculos = tab_veiculo.buscar_tabela("placa", self.tam_intervalo, self.offset)
        else:
            string = self.ui.ui_pages.buscar_veiculo.text()
        
            veiculos = tab_veiculo.buscar("placa", string)
            
        self.ui.ui_pages.tabela_veiculos.setRowCount(len(veiculos))
        tam = len(veiculos)
        
        for i in range(0,tam):
            for j in range(0, columns):  
                item = QTableWidgetItem(str(veiculos[i][j])) 
                if j in campos_numericos:
                    item.setTextAlignment(Qt.AlignRight)
                    self.ui.ui_pages.tabela_veiculos.setItem(i,j,item)
                else:
                    item.setTextAlignment(Qt.AlignLeft)
                    self.ui.ui_pages.tabela_veiculos.setItem(i,j,item)    
                
    
    def limparCamposVeiculo(self):
        
        self.ui.ui_veiculo.placa.clear()
        self.ui.ui_veiculo.ano_fab.clear()
        self.ui.ui_veiculo.cor.clear()
        self.ui.ui_veiculo.marca.clear()
        self.ui.ui_veiculo.desc.clear()
    
    def limparCamposVeiculoEdicao(self):
        
        self.ui.ui_veiculo_edicao.placa.clear()
        self.ui.ui_veiculo_edicao.ano_fab.clear()
        self.ui.ui_veiculo_edicao.cor.clear()
        self.ui.ui_veiculo_edicao.marca.clear()
        self.ui.ui_veiculo_edicao.desc.clear()
    
    def botaoSalvarVeiculo(self):
        
        nomeTabela = "veiculo"
        tab_veiculo = Tabela("tabelas.yaml", nomeTabela)
       
        marca = self.ui.ui_veiculo.marca.text()
        cor = self.ui.ui_veiculo.cor.text()
        placa = self.ui.ui_veiculo.placa.text()
        ano = self.ui.ui_veiculo.ano_fab.text()
        desc = self.ui.ui_veiculo.desc.text()
        habilitado = 1
          
        veiculo = (placa,ano,cor,marca,desc,habilitado)
        if self.validarCamposVeiculo(veiculo, 1) == 1:
            tab_veiculo.inserir(veiculo)
            self.limparCamposVeiculo()
            self.listarTabelaVeiculos()
            self.ui.veiculo.close()
    
    def botaoCancelarVeiculo(self):
        self.limparCamposVeiculo()
        self.restaurarStyleSheetVeiculo()
        self.ui.ui_pages.tabela_veiculos.clearSelection()
        self.ui.ui_pages.tabela_veiculos.reset()
        self.ui.veiculo.close()
    
    def botaoCancelarVeiculoEdicao(self):
        self.limparCamposVeiculoEdicao()
        self.restaurarStyleSheetVeiculoEdicao()
        self.ui.ui_pages.tabela_veiculos.clearSelection()
        self.ui.ui_pages.tabela_veiculos.reset()
        self.ui.veiculo_edicao.close()
            
    def cadastrarVeiculo(self):
        self.limparCamposVeiculo()
        self.restaurarStyleSheetVeiculo()
        self.ui.veiculo.show()
    
    def osPreencherVeiculo(self):
        
        self.ui.ui_pages.buscar_v_os.setStyleSheet("border-color: #44475a")
        nomeTabela = "veiculo"
        tabela = Tabela("tabelas.yaml", nomeTabela)
        veiculo = []
        
        if self.ui.ui_pages.buscar_v_os.cursorPosition() >= 1:
            placa = self.ui.ui_pages.buscar_v_os.text()
            veiculos = tabela.buscar("Placa", placa)
            
            if len(veiculos) > 0:
                for i in range(len(veiculos)):
                    veiculo.append(veiculos[i][1])
                
                completer = QCompleter(veiculo)
                self.ui.ui_pages.buscar_v_os.setCompleter(completer)
    
    def editarVeiculo(self):
       
        nomeTabela = "veiculo"
        tabela = Tabela("tabelas.yaml", nomeTabela)        
        linha = self.ui.ui_pages.tabela_veiculos.currentRow()

        if linha == -1: #Nenhum nome foi selecionado
            resp = QMessageBox.information(self, 'Seleção','Selecione um cliente!')
        else:
            id = self.ui.ui_pages.tabela_veiculos.item(linha,0).text()
            placa = self.ui.ui_pages.tabela_veiculos.item(linha,1).text()
            
            self.ui.ui_veiculo_edicao.placa.setText(self.ui.ui_pages.tabela_veiculos.item(linha,1).text())
            self.ui.ui_veiculo_edicao.ano_fab.setText(self.ui.ui_pages.tabela_veiculos.item(linha,2).text())
            self.ui.ui_veiculo_edicao.cor.setText(self.ui.ui_pages.tabela_veiculos.item(linha,3).text())
            self.ui.ui_veiculo_edicao.marca.setText(self.ui.ui_pages.tabela_veiculos.item(linha,4).text())
            self.ui.ui_veiculo_edicao.desc.setText(self.ui.ui_pages.tabela_veiculos.item(linha,5).text())
            
            self.campo_referencia = id
            self.campo_antigo = placa
            self.restaurarStyleSheetVeiculoEdicao()
            self.ui.veiculo_edicao.show()
            
    def botaoSalvarAtualizacaoVeiculo(self):
        
        nomeTabela = "veiculo"
        tabela = Tabela("tabelas.yaml", nomeTabela) 
                  
        placa = self.ui.ui_veiculo_edicao.placa.text()
        ano_fab = self.ui.ui_veiculo_edicao.ano_fab.text()
        cor = self.ui.ui_veiculo_edicao.cor.text()
        marca = self.ui.ui_veiculo_edicao.marca.text()
        desc = self.ui.ui_veiculo_edicao.desc.text()
        hab = '1' #Campo habilitado
        
        dados = (self.campo_referencia,placa,ano_fab,cor,marca,desc,hab)
        if self.validarCamposVeiculo(dados, 2) == 1:
            tabela.atualizar(dados)
            self.campo_referencia = ''
            self.campo_antigo = ''
            self.listarTabelaVeiculos()
            self.ui.veiculo_edicao.close()
    
    def removerVeiculo(self):
        nomeTabela = "veiculo"
        tabela = Tabela("tabelas.yaml", nomeTabela)    
        linha = self.ui.ui_pages.tabela_veiculos.currentRow()

        if linha == -1: #Nenhum nome foi selecionado
            resp = QMessageBox.information(self, 'Seleção','Selecione um veículos!')
        else:
            msg = QMessageBox.question(self.ui.veiculo,"Confirmação","Confirma a remoção?",QMessageBox.Yes|QMessageBox.No)
            if msg == QMessageBox.Yes:
                id = self.ui.ui_pages.tabela_veiculos.item(linha,0).text()
                tabela.atualizar_campo_habilitado(0,"idVeiculo",id)
                self.listarTabelaVeiculos()
    
    
    #-----------------------------------------------------------
    
    # ---------------------- Serviço ---------------------------
    
    def listarTabelaServicos(self):
        self.ui.ui_pages.tabela_servicos.clearSelection()
        nomeTabela = "servico"
        tab_servico = Tabela("tabelas.yaml", nomeTabela)
        columns = 4
        campos_numericos = [0,2]
        servicos = []

        self.ui.ui_pages.tabela_servicos.reset() #Limpar a seleção da tabela cliente
        self.num_pagina = ceil(self.numeroRegistrosTabela("servico")/self.tam_intervalo)
        
        if self.ui.ui_pages.buscar_servico.text() == "":
            
            servicos = tab_servico.buscar_tabela("nomeServico", self.tam_intervalo, self.offset)
        else:
            string = self.ui.ui_pages.buscar_servico.text()
        
            servicos = tab_servico.buscar("nomeServico", string)
            
        self.ui.ui_pages.tabela_servicos.setRowCount(len(servicos))
        tam = len(servicos)
        
        for i in range(0,tam):
            for j in range(0, columns):
                item = QTableWidgetItem(str(servicos[i][j]))
                if j in campos_numericos:
                    item.setTextAlignment(Qt.AlignRight)
                    self.ui.ui_pages.tabela_servicos.setItem(i,j,item)
                else:
                    item.setTextAlignment(Qt.AlignLeft)
                    self.ui.ui_pages.tabela_servicos.setItem(i,j,item)
                    
    
    
    def limparCamposServico(self):
        
        self.ui.ui_servico.nome.clear()
        self.ui.ui_servico.valor.clear()
        self.ui.ui_servico.descricao.clear()
    
    def limparCamposServicoEdicao(self):
        
        self.ui.ui_servico_edicao.nome.clear()
        self.ui.ui_servico_edicao.valor.clear()
        self.ui.ui_servico_edicao.descricao.clear()
    
    def botaoSalvarServico(self):
        
        nomeTabela = "servico"
        tab_servico = Tabela("tabelas.yaml", nomeTabela)
        
        nome = self.ui.ui_servico.nome.text()
        valor = self.ui.ui_servico.valor.text().replace(",",".")
        desc = self.ui.ui_servico.descricao.text()
        habilitado = 1
        
        servico = (nome,valor,desc,habilitado)
        if self.validarCamposSP(servico, 1) == 1:
            tab_servico.inserir(servico)
            self.limparCamposServico()
            self.listarTabelaServicos()
            self.listarTabelaServicosItemOS()
            self.ui.servico.close()
    
    def botaoCancelarServico(self):
        self.limparCamposServico()
        self.ui.ui_pages.tabela_servicos.clearSelection()
        self.ui.ui_pages.tabela_servicos.reset()
        self.ui.servico.close()
    
    def botaoCancelarServicoEdicao(self):
        self.limparCamposServicoEdicao()
        self.ui.ui_pages.tabela_servicos.clearSelection()
        self.ui.ui_pages.tabela_servicos.reset()
        self.ui.servico_edicao.close()
    
    def cadastrarServico(self):
        self.limparCamposServico()
        self.ui.servico.show()
    
    def botaoEditarServico(self):
          
        nomeTabela = "servico"
        tabela = Tabela("tabelas.yaml", nomeTabela)        
        linha = self.ui.ui_pages.tabela_servicos.currentRow()
        if linha == -1: #Nenhum nome foi selecionado
            resp = QMessageBox.information(self, 'Seleção','Selecione um cliente!')
        else:
            id = self.ui.ui_pages.tabela_servicos.item(linha,0).text() 
            self.ui.ui_servico_edicao.nome.setText(self.ui.ui_pages.tabela_servicos.item(linha,1).text())
            self.ui.ui_servico_edicao.valor.setText(self.ui.ui_pages.tabela_servicos.item(linha,2).text().replace(".",","))
            self.ui.ui_servico_edicao.descricao.setText(self.ui.ui_pages.tabela_servicos.item(linha,3).text())
            self.campo_referencia = id
            self.ui.servico_edicao.show()    
        
    def botaoSalvarAtualizacaoServico(self):
        
        nomeTabela = "servico"
        tabela = Tabela("tabelas.yaml", nomeTabela) 
          
        nome = self.ui.ui_servico_edicao.nome.text()
        valor = self.ui.ui_servico_edicao.valor.text().replace(",",".")
        desc = self.ui.ui_servico_edicao.descricao.text()
        
        dados = (self.campo_referencia,nome,valor,desc)
        
        if self.validarCamposSP(dados, 2) == 1:
            tabela.atualizar(dados)      
            self.campo_referencia = ''
            self.listarTabelaServicos()
            self.ui.servico_edicao.close() 
            
            
    def removerServico(self):
        nomeTabela = "servico"
        tabela = Tabela("tabelas.yaml", nomeTabela)    
        linha = self.ui.ui_pages.tabela_servicos.currentRow()

        if linha == -1: #Nenhum nome foi selecionado
            resp = QMessageBox.information(self, 'Seleção','Selecione um servico!')
        else:
            msg = QMessageBox.question(self.ui.servico,"Confirmação","Confirma a remoção?",QMessageBox.Yes|QMessageBox.No)
            if msg == QMessageBox.Yes:
                id = self.ui.ui_pages.tabela_servicos.item(linha,0).text()
                tabela.atualizar_campo_habilitado(0,"idServico",id)
                self.listarTabelaServicos()
    #-----------------------------------------------------------
    
    # ---------------------- Produto ---------------------------
    
    def listarTabelaProdutos(self):
        self.ui.ui_pages.tabela_produtos.clearSelection()
        self.ui.ui_pages.tabela_produtos.reset() #Limpar a seleção da tabela cliente
        
        nomeTabela = "produto"
        tab_produto = Tabela("tabelas.yaml", nomeTabela)
        columns = 4
        campos_numericos = [0,2]
        produtos = []
        
        
        self.num_pagina = ceil(self.numeroRegistrosTabela("produto")/self.tam_intervalo)
        
        if self.ui.ui_pages.buscar_produto.text() == "":
            produtos = tab_produto.buscar_tabela("nomeProduto", self.tam_intervalo, self.offset)
            
        else:
            string = self.ui.ui_pages.buscar_produto.text()
        
            produtos = tab_produto.buscar("nomeProduto", string)
            
        self.ui.ui_pages.tabela_produtos.setRowCount(len(produtos))
        tam = len(produtos)
       
        for i in range(0,tam):
            for j in range(0, columns):
                item = QTableWidgetItem(str(produtos[i][j]))
                if j in campos_numericos: # Campo Valor da Tabela produtos
                    item.setTextAlignment(Qt.AlignRight) #Muda o texto para a direita
                    self.ui.ui_pages.tabela_produtos.setItem(i,j,item)
                else:
                    item.setTextAlignment(Qt.AlignLeft) 
                    self.ui.ui_pages.tabela_produtos.setItem(i,j,item)
    
    
    def limparCamposProduto(self):
        
        self.ui.ui_produto.nome.clear()
        self.ui.ui_produto.valor.clear()
        self.ui.ui_produto.descricao.clear()
    
    def limparCamposProdutoEdicao(self):
        
        self.ui.ui_produto_edicao.nome.clear()
        self.ui.ui_produto_edicao.valor.clear()
        self.ui.ui_produto_edicao.descricao.clear() 
    
    
    def botaoSalvarProduto(self):
        
        nomeTabela = "produto"
        tab_produto = Tabela("tabelas.yaml", nomeTabela)
      
        nome = self.ui.ui_produto.nome.text()
        valor = self.ui.ui_produto.valor.text().replace(",",".")
        desc = self.ui.ui_produto.descricao.text()
        habilitado = 1
        
        produto = (nome,valor,desc,habilitado)
        if self.validarCamposSP(produto, 1) == 1:
            tab_produto.inserir(produto)
            self.limparCamposProduto()
            self.listarTabelaProdutos()
            self.listarTabelaProdutosItemOS()
            self.ui.produto.close()
        
    
    def botaoCancelarProduto(self):
        self.limparCamposProduto()
        self.ui.ui_pages.tabela_produtos.clearSelection()
        self.ui.ui_pages.tabela_produtos.reset()
        self.ui.produto.close()
    
    def botaoCancelarProdutoEdicao(self):
        self.limparCamposProdutoEdicao()
        self.ui.ui_pages.tabela_produtos.clearSelection()
        self.ui.ui_pages.tabela_produtos.reset()
        self.ui.produto_edicao.close() 
         
    def cadastrarProduto(self):
        self.limparCamposProduto()
        self.ui.produto.show()
    
            
    def botaoEditarProduto(self):        
            
            nomeTabela = "produto"
            tabela = Tabela("tabelas.yaml", nomeTabela)        
            linha = self.ui.ui_pages.tabela_produtos.currentRow()

            if linha == -1: #Nenhum nome foi selecionado
                resp = QMessageBox.information(self, 'Seleção','Selecione um cliente!')
            else:
                id = self.ui.ui_pages.tabela_produtos.item(linha,0).text()
                
                self.ui.ui_produto_edicao.nome.setText(self.ui.ui_pages.tabela_produtos.item(linha,1).text())
                self.ui.ui_produto_edicao.valor.setText(self.ui.ui_pages.tabela_produtos.item(linha,2).text().replace(".",","))
                self.ui.ui_produto_edicao.descricao.setText(self.ui.ui_pages.tabela_produtos.item(linha,3).text())
                self.campo_referencia = id
                self.ui.produto_edicao.show()       
            
    def botaoSalvarAtualizacaoProduto(self):    
        
        nomeTabela = "produto"
        tabela = Tabela("tabelas.yaml", nomeTabela) 
      
        nome = self.ui.ui_produto_edicao.nome.text()
        valor = self.ui.ui_produto_edicao.valor.text().replace(",",".")
        desc = self.ui.ui_produto_edicao.descricao.text()
        
        dados = (self.campo_referencia,nome,valor,desc)
        
        if self.validarCamposSP(dados, 2) == 1:
            tabela.atualizar(dados)    
            self.campo_referencia = ''
            self.listarTabelaProdutos()
            self.ui.produto_edicao.close()
            
    def removerProduto(self):
        nomeTabela = "produto"
        tabela = Tabela("tabelas.yaml", nomeTabela)    
        linha = self.ui.ui_pages.tabela_produtos.currentRow()

        if linha == -1: #Nenhum nome foi selecionado
            resp = QMessageBox.information(self, 'Seleção','Selecione um produto!')
        else:
            msg = QMessageBox.question(self.ui.produto,"Confirmação","Confirma a remoção?",QMessageBox.Yes|QMessageBox.No)
            if msg == QMessageBox.Yes:
                id = self.ui.ui_pages.tabela_produtos.item(linha,0).text()
                tabela.atualizar_campo_habilitado(0,"idProduto",id)
                self.listarTabelaProdutos()
    
    #-----------------------------------------------------------
    
    #---------------------------Relatorios----------------------
    def listarTabelaRelatorios(self):
        nomeTabela = 'ordemservico' # Nome da tabela para acesso ao banco de dados
        tab_relatorios = Tabela('tabelas.yaml', nomeTabela) # Variável para acesso as funções das tabelas
        relatorios = [] # Variável para receber os relatórios
        valores = [] # Variável para receber os valores monetários dos relatórios
        dic_OS = {0:'', 1:'ABERTA', 2:'QUITADA', 3:'CANCELADA'} # Dicionário para traduzir os valores recebidos dos estados das OS
        dic_parcela = {0:'', 1:'ABERTA', 2:'QUITADA'} # Dicionário para traduzir os valores recebidos dos estados das parcelas

        self.ui.ui_pages.re_tabela.reset() # Reseta a tabelas anterior

        # Atribuições dos valores presentes nos seus respctivos campos
        nome = self.ui.ui_pages.re_nome.text()
        placa = self.ui.ui_pages.re_placa.text()
        data_i = self.ui.ui_pages.re_data_i.date()
        data_f  = self.ui.ui_pages.re_data_f.date() 
        estado_OS = self.ui.ui_pages.re_estado_os.currentIndex()
        estado_parcela = self.ui.ui_pages.re_estado_p.currentIndex()

        tab_colunas = ("nomeC, placa, estadoOS, concat( numParcela, ' de ', numParcelas), valorParcela, dataVencimento") # Campos para serem inseridos na interface da tabela de relatórios
        tab_filtro = ("where nomeC like '%{}%' " # Filtro para essa consulta baseado nos campos obtidos anteriormente
                        "and placa like '%{}%' "
                        "and (dataVencimento between {} and {}) "
                        "and estadoOS like '%{}%' "
                        "and estadoParcela like '%{}%' ".format(nome, placa, data_i.toString('yyyy-MM-dd'), data_f.toString('yyyy-MM-dd'), dic_OS[estado_OS], dic_parcela[estado_parcela]))

        relatorios = tab_relatorios.listar_relatorios(tab_colunas, tab_filtro) # Busca feita pela função implementada no objeto Tabela em operacoes_tabela.py

        tab_colunas = ("sum(case when estadoParcela = 'QUITADA' then valorParcela else 0 end), " # !!! Novos campos para busca dos valores, falta implementar mais dois valores !!!
                        "sum(case when estadoParcela = 'ABERTA' then valorParcela else 0 end) ")

        valores = tab_relatorios.listar_relatorios(tab_colunas, tab_filtro) # Mesma busca realizada para tab_colunas mas com as colunas diferentes

        # !!! Os valores ajustados nas QlineEdit vão precisar utilizar também os movimentos de caixa, irá ser implementado depois !!!
        self.ui.ui_pages.re_recebido.setText(valores[0][0]) # !!! Valor das parcelas pagas, falta adicionar o valor de entrada pelos movimentos de caixa !!!
        # self.ui.ui_pages.re_retirado.setText() # !!! Precisa dos movimentos de caixa e do pagamento de funcionários !!!
        # self.ui.ui_pages.re_liquido.setText() # !!! Precisa do valore retirado para fazer a diferença entre recebido - retirado !!!
        self.ui.ui_pages.re_receber.setText(valores[0][1]) # Valor das parcelas não pagas

        colunas = 6 # O número de colunas definida para a tabela de relatórios
        linhas = 10 # O número de linhas definida para a tabela de relatórios
        self.ui.ui_pages.re_tabela.setRowCount(linhas) # Ajusta o número de linhas

        if relatorios: # Se relatórios possuir algo então
            for i in range(0, linhas):
                for j in range(0, colunas):
                    self.ui.ui_pages.re_tabela.setItem(i, j, QtWidgets.QTableWidgetItem(str(relatorios[i][j]))) # Insere valor em cada célula da tabela de relatórios

    def checkDatasRelatorios(self): # Função de checagem a cada alteração nos campos de data

        data_i = self.ui.ui_pages.re_data_i.date() # Atribuição da data presente no campo inicial 
        data_f = self.ui.ui_pages.re_data_f.date() # Atribuição da data presente no campo final

        self.ui.ui_pages.re_data_i.setMaximumDate(data_f) # Ajusta a data final como a máxima para a data inicial
        self.ui.ui_pages.re_data_f.setMinimumDate(data_i) # Ajusta a data inicial como a mínima para a data final

        self.listarTabelaRelatorios() # Atualiza a tabela de relatórios com os valores novos

    def setDatasRelatorios(self): # Na chamada da tela de relatórios é feito a ajuste das datas
        
        hoje = datetime.now() # Pega o dia de hoje para ajustar os campos de data
        dia = calendar.monthrange(hoje.year, hoje.month) # Pega o menor e o maior dia daquele mês e ano específico
        data_i = QDate(hoje.year, hoje.month, dia[0]) # Ajusta a data para o dia primeiro do mês
        data_f = QDate(hoje.year, hoje.month, dia[1]) # Ajusta a data para o último dia do mês
        self.ui.ui_pages.re_data_i.setDate(data_i) # Atribui ao campo re_data_i
        self.ui.ui_pages.re_data_f.setDate(data_f) # Atribui ao campo re_data_f
        self.checkDatasRelatorios() # Checa as datas dos relatórios
        
    #-----------------------------------------------------------  
    #------------ Paginações das tabelas ----------------------- 
    def listarTabela(self, opcao):
        if opcao == 1:
            self.listarTabelaClientes() 
            return  
        if opcao == 2:
            self.listarTabelaFuncionarios()
            return  
        if opcao == 3:
            self.listarTabelaVeiculos()
            return
        if opcao == 4:
            self.listarTabelaServicos()
            return
        if opcao == 5:
            self.listarTabelaProdutos()
            return
        if opcao == 6:
            self.listarTabelaServicosItemOS()
            return
        if opcao == 7:
            self.listarTabelaProdutosItemOS()
            return
        if opcao == 8:
            self.listarTabelaClientesSelecao()
            return
        if opcao == 9:
            self.listarOrdensServicoFiltro()
            return
            
            
    def botaoProximoTabelas(self, opcao):
        #print(self.contador,self.offset)
        if self.num_pagina > 0:
            if self.contador == self.num_pagina - 1:
                self.offset = self.offset
                self.contador = self.contador
            else:
                self.offset += self.tam_intervalo
                self.contador += 1
            
            self.listarTabela(opcao)
        
    def botaoAnteriorTabelas(self, opcao):
        #print(self.contador,self.offset)
        if self.num_pagina > 0:
            if self.contador != 0:
                self.offset -= self.tam_intervalo
                self.contador -= 1
            
            self.listarTabela(opcao)
        
    #-------------------------------------------------  
    def pagarParcelado(self):
        self.ui.ui_pages.num_parcelas.setValue(1)
        self.ui.ui_pages.num_parcelas.setDisabled(False)
        self.ui.ui_pages.valor_entrada.setDisabled(False)
        
        
    def pagarVista(self):
        self.ui.ui_pages.num_parcelas.setValue(1)
        self.ui.ui_pages.valor_entrada.clear()
        self.ui.ui_pages.valor_entrada.setDisabled(True)
        self.ui.ui_pages.num_parcelas.setDisabled(True)
        self.valorEntradaCampo() #Aplica StyleSheet padrão
    #---------------------------------------------------
  
    #--------------------------Caixa----------------------------
    def limparCamposCaixa(self):
        self.ui.ui_pages.ca_valor.clear()
        self.ui.ui_pages.ca_aporte.setCheckable(False)
        self.ui.ui_pages.ca_saque.setCheckable(False)
        self.ui.ui_pages.ca_aporte.setCheckable(True)
        self.ui.ui_pages.ca_saque.setCheckable(True)
    
    
    def listarOS(self):
        nomeTabela = "ordemservico"
        tab_os = Tabela("tabelas.yaml", nomeTabela)
        os = []

        self.ui.ui_pages.os_tabelas_os.reset() #Limpar a seleção da tabela cliente
        
        if self.ui.ui_pages.os_vis_cliente.text() == "":
            os = tab_os.listar_ordem_servico("")
        else:
            string = self.ui.ui_pages.os_vis_cliente.text()
            os = tab_os.listar_ordem_servico("WHERE nomeC like '%{}%' and estadoOS = 'ABERTA'".format(string))
        
        
        if os:    
            self.ui.ui_pages.os_tabelas_os.setRowCount(len(os))
            tam = len(os)
            
            for i in range(0,tam):
                for j in range(0, 8):
                    self.ui.ui_pages.os_tabelas_os.setItem(i,j,QtWidgets.QTableWidgetItem(str(os[i][j])))

        self.ui.ui_pages.os_tabela_parcela.setRowCount(0)
        self.ui.ui_pages.os_tabelas_os.reset()
        
    def visualizarParcelas(self):
        parcelas = []
        linha = self.ui.ui_pages.os_tabelas_os.currentRow()
       
        if linha == -1: #Nenhuma os foi selecionada
            resp = QMessageBox.information(self, 'Seleção','Selecione uma ordem de serviço!')
            return
        
        id_os = self.ui.ui_pages.os_tabelas_os.item(linha,1)
        id_os = id_os.text()
        
        
        nomeTabela = "parcela"
        tab_parcela = Tabela("tabelas.yaml",nomeTabela)
        parcelas = tab_parcela.listar_parcelas_os(id_os)
        
        self.ui.ui_pages.os_tabela_parcela.setRowCount(len(parcelas))
        for i in range(0,len(parcelas)):
            for j in range(0, 4):
                self.ui.ui_pages.os_tabela_parcela.setItem(i,j,QtWidgets.QTableWidgetItem(str(parcelas[i][j+1])))
        
        
        self.ui.ui_pages.os_tabelas_os.reset()
        
        
    def movimentarCaixa(self):
        nomeTabela = "caixa"
        tab_caixa = Tabela("tabelas.yaml", nomeTabela)
        
        caixa = tab_caixa.buscar_tabela()
        
        id = str(caixa[-1][0])
        abertura = str(caixa[-1][1])
        fechamento = str(caixa[-1][2])
        
        if self.ui.ui_pages.ca_valor.text() == "":
            msg = QMessageBox.information(self,"Informação","Preencha o campo valor!")
            return
        valor  = self.ui.ui_pages.ca_valor.text() == ""
        
        if  self.ui.ui_pages.ca_aporte.isChecked() == False and self.ui.ui_pages.ca_saque.isChecked() == False:
            msg = QMessageBox.information(self,"Informação","Escolha um tipo de movimentação!")
            return
        
        if self.ui.ui_pages.ca_aporte.isChecked():
            valor = float(self.ui.ui_pages.ca_valor.text()) 
            self.valorCaixa += valor
            valor = str(self.valorCaixa)
            caixa = (id,abertura,fechamento,valor)
            
            msg = QMessageBox.question(self,"Confirmação","Confirma o aporte?",QMessageBox.Yes|QMessageBox.No)
            
            if msg == QMessageBox.Yes:
                tab_caixa.atualizar(caixa)
                dataHora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                msg = QMessageBox.information(self,"Informação","Aporte realizado!")
                
                # Tabela tipo de movimento
                nomeTabela = "tipomovimento"
                tab_tipo_mov = Tabela("tabelas.yaml", nomeTabela)
                tipo_mov = ("APORTE",self.ui.ui_pages.ca_desc.text())
                tab_tipo_mov.inserir(tipo_mov)
                    
                #Tabela movimento caixa
                id_tm = tab_tipo_mov.buscar_tabela()
                id_tm = id_tm[-1][0] #id do último tipo de movimento 
                    
                nomeTabela = "movimentocaixa"
                tab_mov_caixa = Tabela("tabelas.yaml", nomeTabela)
                valor = float(self.ui.ui_pages.ca_valor.text()) 
                tab_mov_caixa.inserir_mov_caixa(dataHora,valor,id,id_tm) # ***
                self.limparCamposCaixa() 
                         
            if msg == QMessageBox.No:
                 msg = QMessageBox.information(self,"Informação","Aporte cancelado!")
            
        if self.ui.ui_pages.ca_saque.isChecked():
            valor = float(self.ui.ui_pages.ca_valor.text()) 
             
            if valor <= self.valorCaixa:
                self.valorCaixa -= valor
                valor = str(self.valorCaixa)
                caixa = (id,abertura,fechamento,valor)
                
                msg = QMessageBox.question(self,"Confirmação","Confirma o saque?",QMessageBox.Yes|QMessageBox.No)
            
                if msg == QMessageBox.Yes:
                    tab_caixa.atualizar(caixa)
                    dataHora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    msg = QMessageBox.information(self,"Informação","Saque realizado!")
                    
                    
                    # Tabela tipo de movimento
                    nomeTabela = "tipomovimento"
                    tab_tipo_mov = Tabela("tabelas.yaml", nomeTabela)
                    tipo_mov = ("SAQUE",self.ui.ui_pages.ca_desc.text())
                    tab_tipo_mov.inserir(tipo_mov)
                    
                    #Tabela moviemnto caixa
                    id_tm = tab_tipo_mov.buscar_tabela()
                    id_tm = id_tm[-1][0] #id do último tipo de movimento 
                    
                    nomeTabela = "movimentocaixa"
                    tab_mov_caixa = Tabela("tabelas.yaml", nomeTabela)
                    valor = float(self.ui.ui_pages.ca_valor.text()) 
                    tab_mov_caixa.inserir_mov_caixa(dataHora,valor,id,id_tm) # ***
                    self.limparCamposCaixa()
                    
                if msg == QMessageBox.No:
                    msg = QMessageBox.information(self,"Informação","Saque cancelado!")
                
            else:
                msg = QMessageBox.information(self,"Informação","Não há dinheiro suficiente no caixa!")
        
        self.ui.ui_pages.ca_valor.clear()
        self.ui.ui_pages.ca_desc.clear()
         
        self.atualizarValorCaixa()
        
    def atualizarValorCaixa(self):
        nomeTabela = "caixa"
        tab_caixa = Tabela("tabelas.yaml", nomeTabela)  
        valor = tab_caixa.buscar_coluna("valorCaixa")
        
        if not valor: #Primeira inserção do caixa no banco de dados
            abertura = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            caixa = (abertura,abertura,"0")
            tab_caixa.inserir(caixa)
            self.ui.ui_pages.ca_saldo.setText("0.0")
        else:
            valor = valor[-1][0]
            self.ui.ui_pages.ca_saldo.setText(str(valor))
            self.valorCaixa = valor

    def ajustarTabelaProcurarOS(self):
        nomeTabela = "ordemservico"
        tab_os = Tabela("tabelas.yaml", nomeTabela)
        campos_numericos = [0, 4, 5, 6]

        nomeCliente = self.ui.ui_procurar_os.line_cliente.text()

        if nomeCliente == "":
            ordemservicos = tab_os.buscar_filtro("*", "v_tabela_os", "limit 10")
        else:
            ordemservicos = tab_os.buscar_filtro("*", "v_tabela_os", "where nomeC like '%{}%' limit 10".format(nomeCliente))

        linhas = len(ordemservicos)
        colunas = 10
        
        self.ui.ui_procurar_os.tab_os.reset()
        self.ui.ui_procurar_os.tab_os.setRowCount(linhas)

        for i in range(0, linhas):
            for j in range(0, colunas):
                item = QTableWidgetItem(str(ordemservicos[i][j]))
                if j in campos_numericos:
                    item.setTextAlignment(Qt.AlignRight)
                    self.ui.ui_procurar_os.tab_os.setItem(i,j,item)
                else:
                    item.setTextAlignment(Qt.AlignLeft)
                    self.ui.ui_procurar_os.tab_os.setItem(i,j,item)

    def ajustarTabelaReceberParcela(self):
        nomeTabela = "parcela"
        tab_rec_par = Tabela("tabelas.yaml", nomeTabela)
        campos_numericos = [0, 1, 2, 3, 4]

        os = self.ui.ui_receber_parcela.line_os.text()

        if os == "":
            parcelas = tab_rec_par.buscar_filtro("idParcela, numParcela, valorParcela, dataVencimento, dataPagto, estadoParcela", "parcela", "limit 10")
        else:
            parcelas = tab_rec_par.buscar_filtro("idParcela, numParcela, valorParcela, dataVencimento, dataPagto, estadoParcela", "parcela",
                                                 "where idOS like '%{}%' limit 10".format(os))

        linhas = len(parcelas)
        colunas = 10
        
        self.ui.ui_receber_parcela.tab_rec_par.reset()
        self.ui.ui_receber_parcela.tab_rec_par.setRowCount(linhas)

        for i in range(0, linhas):
            for j in range(0, colunas):
                item = QTableWidgetItem(str(os[i][j]))
                if j in campos_numericos:
                    item.setTextAlignment(Qt.AlignRight)
                    self.ui.ui_receber_parcela.tab_rec_par.setItem(i,j,item)
                else:
                    item.setTextAlignment(Qt.AlignLeft)
                    self.ui.ui_receber_parcela.tab_rec_par.setItem(i,j,item)

    def ajustarCamposParcela(self):
        self.ui.ui_pagar_parcela.line_id.setText(self.parcela[0])
        self.ui.ui_pagar_parcela.line_numero.setText(self.parcela[1])
        self.ui.ui_pagar_parcela.line_valor.setText(self.parcela[2])
        self.ui.ui_pagar_parcela.line_vencimento.setText(self.parcela[3])
        self.ui.ui_pagar_parcela.line_pagamento.setText(self.parcela[4])
        self.ui.ui_pagar_parcela.line_estado.setText(self.parcela[5])


    def btnSelecionarOS(self):
        linha = self.ui.ui_procurar_os.tab_os.currentRow()
        idOS = self.ui.ui_procurar_os.tab_os.item(linha, 0)

        if linha == -1:
            print("Linha não selecionada!")
            return
        
        self.ui.ui_receber_parcela.line_os.setText(idOS)
        self.fecharProcurarOS()

    def btnPagarParcela(self):
        linha = self.ui.ui_receber_parcela.tab_rec_par.currentRow()
        idParcela = self.ui.ui_receber_parcela.tab_rec_par.item(linha, 0)

        if linha == -1:
            print("Linha não selecionada!")
            #return

        nomeTabela = "parcela"
        parcela = Tabela("tabelas.yaml", nomeTabela)
        self.parcela = parcela.buscar_filtro("idParcela, numParcela, dataVencimento, dataPagto, valorParcela, estadoParcela", 
                                             "parcela", "")#, "where idParcela = {}".format(idParcela)
        
        self.mostrarPagarParcela()

    def btnConfirmarPagamentoParcela(self):
        nomeTabela = "parcela"
        parcela = Tabela("tabelas.yaml", nomeTabela)
        parcela.pagar_parcela_filtro("where idParcela = {}".format())

    def mostrarReceberParcela(self):
        self.ajustarTabelaReceberParcela()
        self.ui.receber_p.show()

    def fecharReceberParcela(self):
        self.ui.receber_p.close()

    def mostrarProcurarOS(self):
        self.ajustarTabelaProcurarOS()
        self.ui.procurar_os.show()

    def fecharProcurarOS(self):
        self.ui.procurar_os.close()

    def mostrarPagarParcela(self):
        self.ajustarCamposParcela()
        self.ui.pagar_parcela.show()

    def fecharPagarParcela(self):
        self.ui.pagar_parcela.close()

    
    #-----------------------------------------------------------

    ######## Funções do menu lateral
           
    def show_os_page(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.os_page)
        self.ui.os_button.set_active(True)
        self.contador = 0
        self.offset = 0
        self.ui.ui_pages.gerenciar_os.setEnabled(False)
        self.listarOrdensServicoFiltro()
        
    
    def show_client_page(self):
        
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.client_page)
        self.ui.client_button.set_active(True)
        self.contador = 0
        self.offset = 0
        self.num_pagina = ceil(self.numeroRegistrosTabela("cliente")/self.tam_intervalo)
        self.listarTabelaClientes()
        
    
    def show_worker_page(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.worker_page)
        self.ui.worker_button.set_active(True)
        self.contador = 0
        self.offset = 0
        self.num_pagina = ceil(self.numeroRegistrosTabela("funcionario")/self.tam_intervalo)
        self.listarTabelaFuncionarios()
        
    
    def show_car_page(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.car_page)
        self.ui.car_button.set_active(True)
        self.contador = 0
        self.offset = 0
        self.num_pagina = ceil(self.numeroRegistrosTabela("veiculo")/self.tam_intervalo)
        self.listarTabelaVeiculos()
        
    
    def show_product_page(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.product_page)
        self.ui.product_button.set_active(True)
        self.contador = 0
        self.offset = 0
        self.num_pagina = ceil(self.numeroRegistrosTabela("produto")/self.tam_intervalo)
        self.listarTabelaProdutos()
        
        
    def show_service_page(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.service_page)
        self.ui.service_button.set_active(True)
        self.contador = 0
        self.offset = 0
        self.num_pagina = ceil(self.numeroRegistrosTabela("servico")/self.tam_intervalo)
        self.listarTabelaServicos()
        
        
    def show_report_page(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.report_page)
        self.ui.report_button.set_active(True)
        self.setDatasRelatorios()
        
        
    def show_finance_page(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.finance_page)
        self.ui.finance_button.set_active(True)
        self.limparCamposCaixa()
    
    
    ###########  
      
    def reset_selection(self):
        for btn in self.ui.menu.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except:
                #print("")
                #Quando o estilo criado não é utilizado
                pass
            
    #Função para expandir o menu lateral 
    def toggle_button_function(self):
        #Largura do menu
        menu_width = self.ui.menu.width()
        
        width = 50
        if menu_width == 50:
            width = 200
        #Animação 
        self.animation = QPropertyAnimation(self.ui.menu,b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)
        self.animation.start()
   
        
    def ajustarTabelas(self):
        
        #Tabela Ordens de Serviço
        self.ui.ui_pages.tabela_ordem_servico.horizontalHeader().setMinimumSectionSize(130)
        self.ui.ui_pages.tabela_ordem_servico.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)  
        self.ui.ui_pages.tabela_ordem_servico.horizontalHeader().setStretchLastSection(True)  
        self.ui.ui_cliente_selecao.tabela_cliente.setColumnHidden(0,True) #Omitindo a coluna id do cliente
        #Tabela itens
        self.ui.ui_pages.tabela_itens.horizontalHeader().setMinimumSectionSize(200)
        self.ui.ui_pages.tabela_itens.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)  
        self.ui.ui_pages.tabela_itens.horizontalHeader().setStretchLastSection(True)  
        #Tabela Clientes  
        self.ui.ui_pages.tabela_clientes.horizontalHeader().setMinimumSectionSize(100)
        self.ui.ui_pages.tabela_clientes.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)  
        self.ui.ui_pages.tabela_clientes.horizontalHeader().setStretchLastSection(True) 
        self.ui.ui_pages.tabela_clientes.setColumnHidden(0,True) #Omitindo a coluna ID
        self.ui.ui_pages.tabela_clientes.setColumnHidden(3,True) #Omitindo a coluna sexo do cliente
        #self.ui.ui_pages.tabela_clientes.setColumnHidden(4,True) #Omitindo a coluna data de nascimento
        #Tabela Funcionários
        self.ui.ui_pages.tabela_funcionarios.horizontalHeader().setMinimumSectionSize(100)
        self.ui.ui_pages.tabela_funcionarios.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)  
        self.ui.ui_pages.tabela_funcionarios.horizontalHeader().setStretchLastSection(True) 
        self.ui.ui_pages.tabela_funcionarios.setColumnHidden(0,True) 
        self.ui.ui_pages.tabela_funcionarios.setColumnHidden(3,True) #Omitindo a coluna sexo do funcionário
        #self.ui.ui_pages.tabela_funcionarios.setColumnHidden(4,True) #Omitindo a coluna data de nascimento
        #Tabela Veículos
        self.ui.ui_pages.tabela_veiculos.horizontalHeader().setMinimumSectionSize(100)
        self.ui.ui_pages.tabela_veiculos.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)  
        self.ui.ui_pages.tabela_veiculos.horizontalHeader().setStretchLastSection(True) 
        self.ui.ui_pages.tabela_veiculos.setColumnHidden(0,True)
        #Tabela Produtos
        self.ui.ui_pages.tabela_produtos.horizontalHeader().setMinimumSectionSize(100)
        self.ui.ui_pages.tabela_produtos.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)  
        self.ui.ui_pages.tabela_produtos.horizontalHeader().setStretchLastSection(True) 
        self.ui.ui_pages.tabela_produtos.setColumnHidden(0,True)
        #Tabela Serviços
        self.ui.ui_pages.tabela_servicos.horizontalHeader().setMinimumSectionSize(100)
        self.ui.ui_pages.tabela_servicos.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)  
        self.ui.ui_pages.tabela_servicos.horizontalHeader().setStretchLastSection(True) 
        self.ui.ui_pages.tabela_servicos.setColumnHidden(0,True)
        #Tabela Serviços ItemOS
        self.ui.ui_itemOS.tabela_servico.horizontalHeader().setMinimumSectionSize(100)
        self.ui.ui_itemOS.tabela_servico.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)  
        self.ui.ui_itemOS.tabela_servico.horizontalHeader().setStretchLastSection(True) 
        self.ui.ui_itemOS.tabela_servico.setColumnHidden(0,True)
        #Tabela Produtos ItemOS
        self.ui.ui_itemOS.tabela_produto.horizontalHeader().setMinimumSectionSize(100)
        self.ui.ui_itemOS.tabela_produto.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)  
        self.ui.ui_itemOS.tabela_produto.horizontalHeader().setStretchLastSection(True) 
        self.ui.ui_itemOS.tabela_produto.setColumnHidden(0,True)
        # Tabela Histórico de Movimentos de Caixa
        self.ui.ui_pages.ca_tabela.horizontalHeader().setMinimumSectionSize(100)
        self.ui.ui_pages.ca_tabela.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.ui_pages.ca_tabela.horizontalHeader().setStretchLastSection(True)
        # Tabela Procurar OS
        self.ui.ui_procurar_os.tab_os.horizontalHeader().setMinimumSectionSize(100)
        self.ui.ui_procurar_os.tab_os.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.ui_procurar_os.tab_os.horizontalHeader().setStretchLastSection(True)
        # Tabela Receber Parcela
        self.ui.ui_receber_parcela.tab_rec_par.horizontalHeader().setMinimumSectionSize(100)
        self.ui.ui_receber_parcela.tab_rec_par.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.ui_receber_parcela.tab_rec_par.horizontalHeader().setStretchLastSection(True)
        
    #Validadores das entradas dos dados
    def validadoresCamposDouble(self):
     
        validator = QDoubleValidator()
        validator.setRange(0.0,1000000.0,2)
        self.ui.ui_servico.valor.setValidator(validator) #Campo valor da janela de Cadastro de Serviço
        self.ui.ui_produto.valor.setValidator(validator) #Campo valor da janela de Cadastro de Produto
        self.ui.ui_servico_edicao.valor.setValidator(validator) #Campo valor da janela de Edição de Serviço
        self.ui.ui_produto_edicao.valor.setValidator(validator) #Campo valor da janela de Edição de Produto
        self.ui.ui_pages.valor_entrada.setValidator(validator) #Campo valor de entrada da OS
    
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    
    #Tradutor para as funções internas do Qt
    translator = QtCore.QTranslator(app)
    locale = QtCore.QLocale.system().name()
    path = QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.TranslationsPath)
    translator.load("qt_%s" % locale, path)
    app.installTranslator(translator)
    
    window.setMinimumHeight(600)
    window.setMinimumWidth(1250)
    #window.setMaximumWidth(940)
    #window.setMaximumHeight(540)
    
    
    window.resize(1300,640)
    
    ##Centralizar a janela principal
    center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
    geo = window.frameGeometry()
    geo.moveCenter(center)
    window.move(geo.topLeft())
    
    sys.exit(app.exec())