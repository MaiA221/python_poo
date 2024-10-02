import pickle
from typing import List
from common import *
from Interface_Eleicao import Transparencia
import csv

class Urna(Transparencia):
    mesario : Pessoa
    __secao : int
    __zona : int
    __eleitores_presentes : List[Eleitor] = []
    __votos = {} #dicionario chave = numero do candidato, valor é a quantidade de votos

    def __init__(self, mesario : Pessoa, secao : int, zona : int,
                 candidatos : List[Candidato], eleitores : List[Eleitor]):
        self.mesario = mesario
        self.__secao = secao
        self.__zona = zona
        self.__nome_arquivo = f'{self.__zona}_{self.__secao}.pkl'
        self.__candidatos = candidatos
        self.__eleitores = []
        for eleitor in eleitores:
            if eleitor.zona == zona and eleitor.secao == secao:
                self.__eleitores.append(eleitor)

        for candidato in self.__candidatos:
            self.__votos[candidato.get_numero()] = 0
        self.__votos['BRANCO'] = 0
        self.__votos['NULO'] = 0

        with open(self.__nome_arquivo, 'wb') as arquivo:
            pickle.dump(self.__votos, arquivo)

    def get_eleitor(self, titulo : int):
        for eleitor in self.__eleitores:
            if eleitor.get_titulo() == titulo:
                return eleitor
        return False

    def registrar_voto(self, eleitor : Eleitor, n_cand : int):
        self.__eleitores_presentes.append(eleitor)
        if n_cand in self.__votos:
            self.__votos[n_cand] += 1
        else:
            self.__votos['NULO'] += 1

        with open(self.__nome_arquivo, 'wb') as arquivo:
            pickle.dump(self.__votos, arquivo)

    def to_csv(self):
        with open(f'{self.__secao}, {self.__zona}.csv', mode = 'w', newline = '') as file:
            writer = csv.writer(file)
            writer.writerow(['Seção', 'Zona', 'Titulo de Eleitor Presente'])

            for eleitor in self.__eleitores:
                writer.writerow([self.__secao, self.__zona, eleitor.get_titulo()])
    def to_txt(self):
        with open(f'{self.__secao}, {self.__zona}.csv', mode = 'w') as file:
            for eleitor in self.__eleitores:
                file.write(eleitor.__str__())

    def __str__(self):
        info =  f'Urna da seção {self.__secao}, zona {self.__zona}\n'
        info += f'Mesario {self.mesario}\n'
        return info


if __name__ == "__main__":
    c1 = Candidato("Rafael Maia", "2631748299", "454289019-08", 22)
    c2 = Candidato("João Alfredo", "182749273", "234129482-02", 35)

    e1 = Eleitor("Gabriel Viana", "2717382478", "349302823-04", 123, 252, 54)
    e2 = Eleitor("Ricardo NUcci", "3719378123", "123325443-05", 456, 252, 54)

    mesario = Eleitor("Thiago Ferrauchi", "45729729", "958403895-02", 234, 252, 54)

    Urna = Urna(mesario, 252, 54, [c1, c2], [e1, e2])
    Urna.to_csv()
    Urna.to_txt()