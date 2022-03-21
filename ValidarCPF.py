#Fonte > https://www.youtube.com/watch?v=pX_eSMo3DQ4
import re

class ValidarCPF:
    def __init__(self,cpf):
        self.cpf = cpf
        print(self.cpf)
    
    #Obtenção do cpf 
    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = self.apenas_numeros(cpf)
    
    @staticmethod
    def apenas_numeros(cpf):
        return re.sub('[^0-9]', '', cpf)
    
    @staticmethod
    def calcular_digitos(fatia_cpf):
        if not fatia_cpf:
            return False
        
        sequencia = fatia_cpf[0] * len(fatia_cpf)
        if sequencia == fatia_cpf:
            return False

        soma = 0
        for chave, multiplicador in enumerate(range(len(fatia_cpf)+1, 1, -1)):
            soma += int(fatia_cpf[chave]) * multiplicador
            
        resto = 11 - (soma%11)
        resto = resto  if resto <= 9 else 0
        return fatia_cpf + str(resto)
    
    
    def validar(self):
        if not self.cpf:
            return False
        
        novo_cpf = self.calcular_digitos(self.cpf[:9]) #Primeiros 9 dígitos
        #print(novo_cpf)
        novo_cpf = self.calcular_digitos(novo_cpf) # 10 dígitos
        #print(novo_cpf)
        
        if novo_cpf == self.cpf:
            return True
        else:
            return False
    