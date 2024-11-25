from exercicio import *

if __name__ == "__main__":

    c1 = Corredor("Bolt", 35, 58.5)
    n1 = Nadador("Cesar Cielo", 42, 85.5)
    cicli1 = Ciclista("Henrique Avamcine", 37, 74.3)
    tri = Triatleta("Fernanda Keller", 42, 65.3)
#QUANDO É CHAMADO APENAS O c1 ELE INVOCA O MÉTODO __STR__ QUE FOI ERDADO DE ATLETA PELO
#MÉTODO CORREDOR, O MESMO OCORRE PARA AS OUTRAS DUAS CLASSES
    print(c1)
#O MÉTODO aquecer FOI HERDADO DE Atleta PELO O Corredor
    print(c1.aquecer())
    print(c1.correr())

    print(n1)
    print(n1.aquecer())
    print(n1.nadar())

    print(cicli1)
    print(cicli1.aquecer())
    print(cicli1.pedalar())

    print(tri)
    print(tri.realizar_maratona())