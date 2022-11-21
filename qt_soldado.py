# -*- coding: utf-8 -*-
"""QT_Soldado.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Jn4_xyeYuNbkLs_sFaNHwqj6anzRad3L
"""

##QT_Soldado
import random
class Soldado:
    def __init__(self, capacidade):
        self.capacidade=capacidade
        self.numero_elementos=0
        self.soldados=[]

    def fila_vazia(self):
        return self.numero_elementos==0

    def fila_cheia (self):
        return self.numero_elementos==self.capacidade

    def enfileirar (self, soldado):
        if self.fila_cheia():
            return "fila chei."
        else:
            self.soldados.append(soldado)

    def sortear_soldado(self):
        tamanho_fila=len(self.soldados)
        continuar=True
        while(continuar):
            if(tamanho_fila>0and tamanho_fila>1):
                tamanho_fila-=1
                sorteio=random.randint(0, tamanho_fila)
                self.soldados.pop(sorteio)

            else:
                continuar=False
                print("O soldado escolhido para a tarefa foi:")
        return self.soldados


soldados=Soldado(3)
soldados.enfileirar("antonio")
soldados.enfileirar("arthur")
soldados.enfileirar("rodrigo")
print(soldados.sortear_soldado())