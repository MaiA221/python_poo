from atleta import Atleta

class Corredor(Atleta):
    def correr(self):
        return "Correndo..."

class Nadador(Atleta):
    def nadar(self):
        return "Nadando..."

class Ciclista(Atleta):
    def pedalar(self):
        return "Pedalando..."

class Triatleta(Corredor, Nadador, Ciclista):
    def realizar_maratona(self):
        info = self.aquecer()
        info += self.nadar()
        info += self.pedalar()
        info += self.correr()
        return info