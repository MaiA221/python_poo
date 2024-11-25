from lutadores import *

if __name__ == "__main__":
    popo = Boxeador("Popó")
    bambam = Boxeador("Bambam")

    print(popo)
    print(bambam)
    popo.cruzado(bambam)
    popo.gancho(bambam)
    bambam.soco(popo)
    bambam.soco(popo)
    print(popo)
    print(bambam)

    print("<------------------------------>")
    
    gabriel = Muay_Thai("Gabriel")
    ricardo = Jujitsu("Ricardo")

    print(gabriel)
    print(ricardo)
    gabriel.soco(ricardo)
    gabriel.gancho(ricardo)
    gabriel.chute_alto(ricardo)
    ricardo.chave_braco(gabriel)
    print(gabriel)
    print(ricardo)

    print("<------------------------------>")
    
    rafael = MMA("Rafael")
    nattan = MMA("Nattan")

    print(rafael)
    print(nattan)
    rafael.superman_punch(nattan)
    nattan.cadeirada(rafael)
    nattan.chute_alto(rafael)
    nattan.soco(rafael)
    print(rafael)
    print(nattan)

    print("<------------------------------>")

    datena = MMA("Datena")
    marcal = MMA("Pablo Marçal")

    print(datena)
    print(marcal)
    datena.cadeirada(marcal)
    print(datena)
    print(marcal)