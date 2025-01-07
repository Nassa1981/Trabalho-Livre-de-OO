import json
from datetime import datetime, timedelta
from livro import LivroConcreto
from emprestimo_devolução import Emprestimo
from usuario import Usuario


class Biblioteca:
    def __init__(self):
        self._emprestimos = []
        self._livros = []  
        self._usuarios = {} 
        self._emprestimos = []
        self._livros = []  
        self._usuarios = {} 
        
        

    def adicionar_livros(self, titulo, autor):
        for livro in self._livros:
            if livro.obter_titulo() == titulo and livro.obter_autor() == autor:
                print(f"O livro '{titulo}' de '{autor}' já está cadastrado na biblioteca.")
                return
        novo_livro = LivroConcreto(titulo, autor)
        self._livros.append(novo_livro)
        self.salvar_livros()
        print(f"Livro '{titulo}' de {autor} adicionado à biblioteca.")

    def salvar_livros(self):
        livros_data = [
            {
                "titulo": livro.obter_titulo(),
                "autor": livro.obter_autor(),
                "disponibilidade": livro.esta_disponivel()
            }
            for livro in self._livros
        ]
        with open("livros.json", "w", encoding="utf-8") as file:
            json.dump(livros_data, file, ensure_ascii=False, indent=4)
        print("Dados dos livros salvos em 'livros.json'.")

    def buscar_livro(self, titulo, autor):
        for livro in self._livros:
            if livro.obter_titulo() == titulo and livro.obter_autor() == autor:
                print(f"Livro encontrado: '{titulo}' de {autor}.")
                return livro
        print(f"O livro '{titulo}' de '{autor}' não foi encontrado na biblioteca.")
        return None

    def cadastrar_usuario(self, nome, usuario_id):
        if usuario_id in self._usuarios:
            print("Já existe um usuário com esse ID.")
            return
        usuario = Usuario(nome, usuario_id)
        self._usuarios[usuario_id] = usuario
        self.salvar_usuarios()
        print(f"Usuário '{nome}' cadastrado com ID '{usuario_id}'.")

    def salvar_usuarios(self):
        usuarios_data = {
            usuario_id: {
                "nome": usuario.obter_nome(),
                "usuario_id": usuario.obter_usuario_id(),
                "livros_emprestados": [
                    {"titulo": livro.obter_titulo(), "autor": livro.obter_autor()}
                    for livro in usuario.obter_livros_emprestados()
                ],
            }
            for usuario_id, usuario in self._usuarios.items()
        }
        with open("usuarios.json", "w", encoding="utf-8") as file:
            json.dump(usuarios_data, file, ensure_ascii=False, indent=4)
        print("Dados dos usuários salvos em 'usuarios.json'.")

    def emprestar_livro(self, usuario_id, livro_titulo, livro_autor):
        """Realiza o empréstimo de um livro para um usuário."""
        usuario = self._usuarios.get(usuario_id)
        if not usuario:
            print("Usuário não encontrado.")
            return

        livro = self.buscar_livro(livro_titulo, livro_autor)
        if not livro or not livro.esta_disponivel():
            print(f"O livro '{livro_titulo}' de '{livro_autor}' não está disponível.")
            return

        data_emprestimo = datetime.now()
        data_devolucao = data_emprestimo + timedelta(days=7)

        livro.definir_disponivel(False)
        usuario.emprestar_livro(livro)
        self._emprestimos.append(Emprestimo(livro, data_emprestimo, data_devolucao))

        self.salvar_livros()
        self.salvar_usuarios()
        print(f"Livro '{livro_titulo}' emprestado para {usuario.obter_nome()}. Prazo: {data_devolucao.strftime('%Y-%m-%d')}")

    def mostrar_clientes(self):
        if not self._usuarios:
            print("Não há clientes cadastrados.")
            return

        print("\nCLIENTES CADASTRADOS:")
        for usuario_id, usuario in self._usuarios.items():
            print(f"ID: {usuario_id}, Nome: {usuario.obter_nome()}")

    def mostrar_livros_cadastrados(self):
        if not self._livros:
            print("Não há livros cadastrados na biblioteca.")
            return

        print("\nLIVROS CADASTRADOS:")
        for livro in self._livros:
            disponibilidade = "Disponível" if livro.esta_disponivel() else "Emprestado"
            print(f"Título: {livro.obter_titulo()}, Autor: {livro.obter_autor()}, Disponibilidade: {disponibilidade}")

    @classmethod
    def documentation(cls):
        return "Classe responsável pela gestão da biblioteca."
