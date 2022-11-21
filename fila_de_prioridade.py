# -*- coding: utf-8 -*-
"""Fila_de_Prioridade.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EZKXhh38Dn1hSopoF5H1gpTcczS3Nz6g
"""

import numpy as np

##Fila_de_Prioridade


class FilaPrioridade:
    def __init__(self,capacidade):
        self.capacidade = capacidade
        self.qtd_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def __fila_vazia(self):
        return self.qtd_elementos == 0

    def __fila_cheia(self):
        return self.qtd_elementos == self.capacidade

    def enfileirar(self, valor):
        if self.__fila_cheia():
            print('Fila cheia')
            return

        if self.qtd_elementos == 0:
            self.valores[self.qtd_elementos] = valor
            self.qtd_elementos += 1

        else:
            num = self.qtd_elementos -1
            while num >= 0:
                if valor > self.valores[num]:
                    self.valores[num+1] = self.valores[num]
                else:
                    break
                num-=1
            self.valores[num+1]=valor
            self.qtd_elementos += 1

    def desenfileirar(self):
        if self.__fila_vazia():
            print('Fila vazia')
            return
        valor=self.valores[self.qtd_elementos -1]
        self.qtd_elementos -1
        return valor

    def primeiro(self):
        if self.__fila_vazia():
            return -1
        return self.valores[self.qtd_elementos -1]

fila = FilaPrioridade(4)
fila.enfileirar(14)
fila.primeiro()
fila.enfileirar(8)
fila.primeiro()
fila.enfileirar(50)
fila.primeiro()
print(fila.desenfileirar())
print(fila.primeiro())