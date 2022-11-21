# -*- coding: utf-8 -*-
"""QT_Pilha.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Zg8skl7Qa8NMz69kQyv4qJJypY_AAX12
"""

##QT_Pilha
class TPilha:
    
    def __init__(self,capacidade):
        self.capacidade = capacidade

    def empilhar(self,vetor):
        tamanho_vetor = len(vetor)
        tamanho_array = len(vetor)
        contador = 0
        self.pilha = []
        if (tamanho_vetor > self.capacidade):
            return "vetor maior que a capacidade, retire um elemento."
        else:
            for i in vetor:
                valor_temporario = i
                contador += 1
                tamanho_pilha = len(self.pilha)
                if (contador <= tamanho_array):
                    if(valor_temporario % 2 == 1 and tamanho_pilha > 0):
                        self.pilha.pop()
                    else:
                        self.pilha.append(valor_temporario)
    def ver_topo(self):
        return self.pilha


array = TPilha(15)
array.empilhar([1,2,7,9,6,6,1,8,11,98,16,23,54,27,81])
print(array.ver_topo())