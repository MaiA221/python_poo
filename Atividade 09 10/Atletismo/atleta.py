from abc import ABC

class Atleta(ABC):
    nome : str
    idade : int
    peso : float


    def __init__(self, n : str, i : int, p : float):
        self.nome = n
        self.idade = i
        self.peso = p

    def aquecer(self):
        return "Aquecendo ..."

#STR É UM MÉTODO QUE SERA USADO DE FORMA PADRÃO PELO PROGRAMA
    def __str__(self):
        return f'Nome: {self.nome}, {self.idade} anos, {self.peso} Kg'