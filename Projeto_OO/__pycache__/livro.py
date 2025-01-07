from abc import ABC, abstractmethod
class Livro(ABC):
    def __init__(self, titulo, autor, disponivel=True):
        self._titulo = titulo
        self._autor = autor
        self._disponivel = disponivel

    @property
    def obter_titulo(self):
        return self._titulo

    @property
    def obter_autor(self):
        return self._autor

    @property
    def esta_disponivel(self):
        return self._disponivel

    @esta_disponivel.setter
    def esta_disponivel(self, valor):
        self._disponivel = valor

    @abstractmethod
    def definir_disponivel(self, disponivel):
        pass
    
class LivroConcreto:
    def __init__(self, titulo, autor):
        self._titulo = titulo
        self._autor = autor
        self._disponivel = True

    def obter_titulo(self):
        return self._titulo

    def obter_autor(self):
        return self._autor

    def esta_disponivel(self):
        return self._disponivel

    def definir_disponivel(self, disponivel):
        self._disponivel = disponivel
        
    def esta_emprestado(self):
        return self._emprestado  
