
#from pages.pergunta_metodos import Pergunta_Metodos
from qt_core import *

from widgets.push_button import PushButton
#Páginas criadas no QtDesigner
from pages.pages import Ui_StackedWidget
from pages.cliente import *
from pages.funcionario import *
from pages.veiculo import *
from pages.produto import *
from pages.servico import *
from pages.cliente_edicao import *
from pages.funcionario_edicao import *
from pages.veiculo_edicao import *
from pages.itemOS import *
from pages.servico_edicao import *
from pages.produto_edicao import *
from pages.cliente_visualizacao import *
from pages.funcionario_visualizao import *
from pages.veiculo_visualizacao import *
from pages.cliente_selecao import *
from pages.receber_parcela import *
from pages.procurar_os import *
from pages.pagar_parcela import *

class UI_MainWindow(object):
    
    def setup_ui(self, parent):
        
        if not parent.objectName():
            parent.setObjectName("MainWindow")
        #Paramêtros da tela
        #parent.resize(1200, 540)
        #parent.setMinimumSize(960, 540)
        
        #Criação do frame central
        self.central_frame = QFrame()
        self.central_frame.setStyleSheet("background: white")
        #Definir frame central 
        parent.setCentralWidget(self.central_frame) 
        
        #Criação do layout principal
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)
        
        #Menu esquerdo
        self.menu = QFrame()
        self.menu.setStyleSheet("background-color: #4B7584")
        self.menu.setMaximumWidth(50)
        self.menu.setMinimumWidth(50)
        
        #Layout menu esquerdo
        self.menu_layout = QVBoxLayout(self.menu)
        self.menu_layout.setContentsMargins(0,0,0,0)
        self.menu_layout.setSpacing(0)
        
        #Frame superior do menu
        self.menu_top_frame = QFrame()
        self.menu_top_frame.setMinimumHeight(50)
        self.menu_top_frame.setStyleSheet("background-color: #4B7584")#44475a
        
        #Layout para os botões 
        self.menu_top_frame_layout = QVBoxLayout(self.menu_top_frame)
        self.menu_top_frame_layout.setContentsMargins(0,0,0,0)
        self.menu_top_frame_layout.setSpacing(0)
        
        #Botões do menu
        self.toggle_button = PushButton(text="Ocultar Menu", icon_path="menu.svg", icon_color="white")
        self.os_button = PushButton( text="Ordens de Serviço",icon_path="ordemServico.svg", icon_color="white",is_active=True)
        self.client_button = PushButton(text="Clientes", icon_path="cliente.svg", icon_color="white")
        self.worker_button = PushButton(text="Funcionários", icon_path="funcionario.svg", icon_color="white")
        self.car_button = PushButton(text="Veículos", icon_path="veiculo.svg", icon_color="white")
        self.product_button = PushButton(text="Produtos", icon_path="produto.svg", icon_color="white")
        self.service_button = PushButton(text="Serviços", icon_path="servico.svg", icon_color="white")
        self.report_button = PushButton(text="Relatórios", icon_path="relatorio", icon_color="white")
        self.finance_button = PushButton(text="Caixa", icon_path="caixa.svg", icon_color="white")
        
        #Adicionando os botões ao layout
        self.menu_top_frame_layout.addWidget(self.toggle_button)
        self.menu_top_frame_layout.addWidget(self.os_button)
        self.menu_top_frame_layout.addWidget(self.client_button)
        self.menu_top_frame_layout.addWidget(self.worker_button)
        self.menu_top_frame_layout.addWidget(self.car_button)
        self.menu_top_frame_layout.addWidget(self.product_button)
        self.menu_top_frame_layout.addWidget(self.service_button)
        self.menu_top_frame_layout.addWidget(self.report_button)
        self.menu_top_frame_layout.addWidget(self.finance_button)
        
        #Espaço até o final do menu
        self.menu_spacer = QSpacerItem(20,20,QSizePolicy.Minimum, QSizePolicy.Expanding)
        
        #Adicionando widgets no menu 
        self.menu_layout.addWidget(self.menu_top_frame)
        self.menu_layout.addItem(self.menu_spacer)
        
        #Área principal
        self.area = QFrame()
        #self.area.setStyleSheet("background-color: white")
        
        #Layout área principal
        self.area_layout = QVBoxLayout(self.area)
        self.area_layout.setContentsMargins(0,0,0,0)
        self.area_layout.setSpacing(0)
        
        #Menu superior da área principal
        self.top_bar = QFrame()
        self.top_bar.setMinimumHeight(30)
        self.top_bar.setMaximumHeight(30)
        self.top_bar.setStyleSheet("background-color: #44475a")
        
        """
        #Botão para fechar o aplicativo
        #Layout menu superior
        self.top_bar_layout = QVBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(0,0,0,0)
        self.top_bar_layout.setSpacing(0)
        
        #Botões do menu superior
        self.close_button = QPushButton()
        
        #Adicionando widgets ao menu superior
        self.top_bar_layout.addWidget(self.close_button)
        """
        #Menu inferior da área principal
        self.bottom_bar = QFrame()
        self.bottom_bar.setMinimumHeight(30)
        self.bottom_bar.setMaximumHeight(30)
        self.bottom_bar.setStyleSheet("background-color: #44475a")
        
        #Páginas 
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("background-color: white")
        
        self.ui_pages = Ui_StackedWidget()
        self.ui_pages.setupUi(self.pages)
        self.pages.setCurrentWidget(self.ui_pages.os_page)
        
        #Janela ItemOS
        self.itemOS = QMainWindow()
        self.ui_itemOS = Ui_Janela_ItemOS()
        self.ui_itemOS.setupUi(self.itemOS)
        
        #Janela de cadastro de clientes
        self.cliente = QMainWindow()
        self.ui_cliente = Ui_Janela_Cliente() 
        self.ui_cliente.setupUi(self.cliente)
        
        #Janela de edição de clientes
        self.cliente_edicao = QMainWindow()
        self.ui_cliente_edicao = Ui_Janela_Cliente_Edicao() 
        self.ui_cliente_edicao.setupUi(self.cliente_edicao)
        
        #Janela de cadastro de funcionários
        self.funcionario = QMainWindow()
        self.ui_funcionario = Ui_Janela_Funcionario() 
        self.ui_funcionario.setupUi(self.funcionario)
        
        #Janela de edição de funcionários
        self.funcionario_edicao = QMainWindow()
        self.ui_funcionario_edicao = Ui_Janela_Funcionario_Edicao() 
        self.ui_funcionario_edicao.setupUi(self.funcionario_edicao)
        
        #Janela de cadastro de veículos
        self.veiculo = QMainWindow()
        self.ui_veiculo = Ui_Janela_Veiculo()
        self.ui_veiculo.setupUi(self.veiculo)
        
        #Janela de edição de veículos
        self.veiculo_edicao = QMainWindow()
        self.ui_veiculo_edicao = Ui_Janela_Veiculo_Edicao()
        self.ui_veiculo_edicao.setupUi(self.veiculo_edicao)
        
        #Janela de cadastro de produtos
        self.produto = QMainWindow()
        self.ui_produto = Ui_Janela_Produto()
        self.ui_produto.setupUi(self.produto)
        
        #Janela de cadastro de servicos
        self.servico = QMainWindow()
        self.ui_servico = Ui_Janela_Servico()
        self.ui_servico.setupUi(self.servico)
        
        #Janela de edição de serviço
        self.servico_edicao = QMainWindow()
        self.ui_servico_edicao = Ui_Janela_Servico_Edicao()
        self.ui_servico_edicao.setupUi(self.servico_edicao)
        
        #Janela de edição de produto
        self.produto_edicao = QMainWindow()
        self.ui_produto_edicao = Ui_Janela_Produto_Edicao()
        self.ui_produto_edicao.setupUi(self.produto_edicao)
        
        #Janela de vizualização do cliente
        self.cliente_vizualizacao = QMainWindow()
        self.ui_cliente_vizualizacao = Ui_Janela_Cliente_Visualizacao()
        self.ui_cliente_vizualizacao.setupUi(self.cliente_vizualizacao)
        
        #Janela de vizualização do funcionário
        self.funcionario_vizualizacao = QMainWindow()
        self.ui_funcionario_vizualizacao = Ui_Janela_Funcionario_Visualizacao()
        self.ui_funcionario_vizualizacao.setupUi(self.funcionario_vizualizacao)
        
        #Janela de vizualização do veículo
        self.veiculo_vizualizacao = QMainWindow()
        self.ui_veiculo_vizualizacao = Ui_Janela_Veiculo_Visualizacao()
        self.ui_veiculo_vizualizacao.setupUi(self.veiculo_vizualizacao)
        
        #Janela de vizualização do veículo
        self.cliente_selecao = QMainWindow()
        self.ui_cliente_selecao = Ui_Janela_Cliente_Selecao()
        self.ui_cliente_selecao.setupUi(self.cliente_selecao)

        # Janela de receber parcela
        self.receber_p = QMainWindow()
        self.ui_receber_parcela = Ui_janela_receber_parcela()
        self.ui_receber_parcela.setupUi(self.receber_p)

        # Janela de procurar ordem de servico
        self.procurar_os = QMainWindow()
        self.ui_procurar_os = Ui_procurar_os()
        self.ui_procurar_os.setupUi(self.procurar_os)

        # Janela pagar parcela
        self.pagar_parcela = QMainWindow()
        self.ui_pagar_parcela = Ui_pagar_parcela()
        self.ui_pagar_parcela.setupUi(self.pagar_parcela)
        
        
        #Adicionando Widget na área principal
        self.area_layout.addWidget(self.top_bar)
        self.area_layout.addWidget(self.pages)
        self.area_layout.addWidget(self.bottom_bar)
        
        #Adicionando Widgets no aplicativo
        self.main_layout.addWidget(self.menu)
        self.main_layout.addWidget(self.area)
        
        