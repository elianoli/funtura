from qt_core import *

class Caixa_Pergunta(QMessageBox):
    def __init__(self, texto):
        super(Caixa_Pergunta, self).__init__()

        msgBox = QMessageBox()
        msgBox.setWindowTitle("Caixa de Pergunta")
        #msgBox.setIcon(QMessageBox.Question)
        msgBox.setText(texto)
        botao_sim = QPushButton()
        botao_nao = QPushButton()
        botao_sim.setText("SIM")
        botao_nao.setText("NÃO")
        msgBox.addButton(botao_sim, QMessageBox.YesRole)
        msgBox.addButton(botao_nao, QMessageBox.NoRole)
        self.ret = self.exec() # 0 = Sim, 1 = Não
        
    def getResposta(self):
        return self.ret
