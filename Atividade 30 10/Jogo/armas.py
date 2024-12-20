from abc import ABC, abstractmethod, ABCMeta
from golpe import *

class Arma(ABC):
    destruicao : float

    def __init__(self, d : float):
        self.destruicao = d

    def agredir(self, j):
        j.energia -= 5

    def __str__(self):
        return f'Poder de Destruicao: {self.destruicao}'

class Disparavel(metaclass=ABCMeta):
    @abstractmethod
    def disparar(self, j):
        pass

    @abstractmethod
    def recarregar(self):
        pass

class Faca(Arma):
    lamina : int

    def __init__(self):
        self.destruicao = 15
        self.lamina = 10

    def agredir(self, j):
        self.lamina -= 1
        if self.lamina > 0 :
            j.energia -= self.destruicao
        else:
            super().agredir(j)

class Revolver(Arma, Disparavel):
    cartuchos : int

    def __init__(self):
        self.destruicao = 20
        self.cartuchos = 6

    def disparar(self, j):
        if self.cartuchos > 0:
            self.cartuchos -= 1
            j.energia -= self.destruicao

    def recarregar(self):
        self.cartuchos = 6

class Lanca_chamas(Arma, Disparavel):
    gas : float

    def __init__(self):
        self.destruicao = 30
        self.gas = 100

    def disparar(self, j):
        if self.gas > 0:
            self.gas -= 5.5
            j.energia -= self.destruicao

    def recarregar(self):
        self.gas = 100

class Soco_ingles(Faca, Soco):
    def agredir(self, j):
        super().agredir(j)
        self.golpear(j)