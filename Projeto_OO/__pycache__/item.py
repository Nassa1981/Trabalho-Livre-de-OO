from abc import ABC, abstractmethod

class Item(ABC): 
    def __init__(self, titulo, autor, disponivel):
        self._titulo = titulo
        self._autor = autor
        self._disponivel = disponivel

    @abstractmethod
    def obter_titulo(self):
        pass

    @abstractmethod
    def obter_autor(self):
        pass

    @abstractmethod
    def estar_disponivel(self):
        pass

    @abstractmethod
    def definir_disponivel(self, disponivel):
        pass

    @classmethod
    def documentation(cls):
        return