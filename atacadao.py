from abc import ABC, abstractmethod
import math

# 1. Criando a Classe Abstrata
class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
    # Este método não tem implementação na classe base
    # Ele serve apenas como uma "regra" para as filhas.

    def descricao(self):
        return "Eu sou uma forma geométrica."
    
class Quadrado(Forma):
    def calcular_area(self):
        return self.lado * self.lado
    
    class Circulo(Forma):
        def __init__(self, raio):
            self.raio = raio
        def calcular_area(self):
            return math.pi * (self.raio ** 2)