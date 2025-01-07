class Emprestimo:
    def __init__(self, livro, data_emprestimo, data_devolucao):
        self._livro = livro
        self._data_emprestimo = data_emprestimo
        self._data_devolucao = data_devolucao

    def obter_livro(self):
        return self._livro

    def obter_data_emprestimo(self):
        return self._data_emprestimo

    def obter_data_devolucao(self):
        return self._data_devolucao

    def calcular_periodo_emprestimo(self):
        return (self._data_devolucao - self._data_emprestimo).days

    @classmethod
    def documentation(cls):
        return