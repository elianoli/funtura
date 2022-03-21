import os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class PushButton(QPushButton):
    def __init__(
        #Parâmetros para customizar o botão
        self,
        text = "",
        height = 40,
        minimum_width = 50,
        text_padding = 55,
        text_color = "white",#c3ccdf
        icon_path = "",
        icon_color = "#c3ccdf",
        btn_color = "#4B7584",
        btn_hover = "#4f5368", #Cor do botão quando o mouse estiver em cima
        btn_pressed = "#282a36",
        is_active = False
    ):
        super().__init__()
        
        self.setText(text)
        self.setMaximumHeight(height)
        self.setMinimumHeight(height)
        self.setCursor(Qt.PointingHandCursor)
        
        self.minimum_width = minimum_width
        self.text_padding = text_padding
        self.text_color = text_color
        self.icon_path = icon_path
        self.icon_color = icon_color
        self.btn_color = btn_color
        self.btn_hover = btn_hover
        self.btn_pressed = btn_pressed
        self.is_active = is_active
        
        self.set_style(
            text_padding = self.text_padding,
            text_color = self.text_color,
            btn_color = self.btn_color,
            btn_hover = self.btn_hover,
            btn_pressed = self.btn_pressed,
            is_active = self.is_active
        )
        
    #Função para ativar estilo de "selecionado" no botão 
    def set_active(self, is_active_button):
        self.set_style(
            text_padding = self.text_padding,
            text_color = self.text_color,
            btn_color = self.btn_color,
            btn_hover = self.btn_hover,
            btn_pressed = self.btn_pressed,
            is_active = is_active_button
        )
        
        
    #Método para aplicar estilo ao botão   
    def set_style(
        self,
        text_padding = 55,
        text_color = "#c3ccdf",
        btn_color = "#4B7584",#44475a
        btn_hover = "#4f5368", 
        btn_pressed = "#282a36",
        is_active = False
    ):
    
        style = f"""
            QPushButton{{
                color: {text_color};
                background-color: {btn_color};
                padding-left: {text_padding}px;
                font: 87 10pt "Arial Black";
                text-align: left;
                border: none;
            }} 
            QPushButton:hover{{
                background-color: {btn_hover};
            }}
                
            QPushButton:pressed{{
                background-color: {btn_pressed};
            }}
            
        """
        
        active_style = f"""
            QPushButton{{
                background-color: {btn_hover};
                border-top: 2px solid white; 
                border-left: 2px solid white; 
                border-bottom: 2px solid white; 
                border-top-left-radius: 15px; 
                border-bottom-left-radius: 15px;
            }}
        """
        if not is_active:
            self.setStyleSheet(style)
        else:
            self.setStyleSheet(style + active_style)
            
            
    def paintEvent(self, event):
        #Recuperar estilo definido anteriormente
        QPushButton.paintEvent(self, event)
        
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(Qt.NoPen)
        
        rect = QRect(0,0,self.minimum_width,self.height())
        
        self.draw_icon(qp, self.icon_path, rect, self.icon_color)
        
        qp.end()
    
    def draw_icon(self, qp, image, rect, color):
        #Construindo o caminho 
        app_path = os.path.abspath(os.getcwd()) #Caminho até a aplicação 
        folder = "images/icons" #Caminho até os ícones
        path = os.path.join(app_path, folder)
        icon_path = os.path.normpath(os.path.join(path, image))
        
        #Desenhando ícone
        icon = QPixmap(icon_path)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), color)
        
        qp.drawPixmap(
            (rect.width() - icon.width())/2,
            (rect.height() - icon.height())/2,
            icon
        )
        painter.end()