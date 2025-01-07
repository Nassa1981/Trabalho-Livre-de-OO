import json

class Usuario:
    def __init__(self, nome, usuario_id):
        self._nome = nome
        self._usuario_id = usuario_id
        self._livros_emprestados = []

    def obter_nome(self):
        return self._nome

    def definir_nome(self, novo_nome):
        self._nome = novo_nome

    def obter_usuario_id(self):
        return self._usuario_id

    def obter_livros_emprestados(self):
        return self._livros_emprestados

    def emprestar_livro(self, livro):
        self._livros_emprestados.append(livro)

    def devolver_livro(self, livro):
        if livro in self._livros_emprestados:
            self._livros_emprestados.remove(livro)
            print(f"Livro '{livro.obter_titulo()}' de {livro.obter_autor()} devolvido com sucesso.")
            return True
        else:
            print(f"Erro: O livro '{livro.obter_titulo()}' não foi emprestado por {self._nome}.")
            return False

    def to_dict(self):
        return {
            "nome": self._nome,
            "usuario_id": self._usuario_id,
            "livros_emprestados": [livro.to_dict() for livro in self._livros_emprestados]
        }

    @classmethod
    def from_dict(cls, dados):
        usuario = cls(dados["nome"], dados["usuario_id"])
        return usuario

    @classmethod
    def documentation(cls):
        return "Classe que representa um usuário da biblioteca."

    def __str__(self):
        return f"Usuário: {self._nome} (ID: {self._usuario_id})"
