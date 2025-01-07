import json
import os
import uuid


class TchauBiblioteca:
    def __init__(self):
        self._usuarios = {}
        self._livros = []
        self.carregar_usuarios()
        self.carregar_livros()

    def carregar_usuarios(self):
        if os.path.exists("usuarios.json"):
            try:
                with open("usuarios.json", "r", encoding="utf-8") as arquivo:
                    self._usuarios = json.load(arquivo)
            except json.JSONDecodeError:
                print("Erro ao carregar 'usuarios.json'. Criando arquivo vazio.")
                self._usuarios = {}
                self.salvar_usuarios()
        else:
            print("Arquivo 'usuarios.json' não encontrado. Criando arquivo vazio.")
            self._usuarios = {}
            self.salvar_usuarios()

    def salvar_usuarios(self):
        try:
            with open("usuarios.json", "w", encoding="utf-8") as arquivo:
                json.dump(self._usuarios, arquivo, indent=4, ensure_ascii=False)
            print("Usuários salvos com sucesso.")
        except Exception as e:
            print(f"Erro ao salvar 'usuarios.json': {e}")

    def carregar_livros(self):
        if os.path.exists("livros.json"):
            try:
                with open("livros.json", "r", encoding="utf-8") as arquivo:
                    self._livros = json.load(arquivo)
            except json.JSONDecodeError:
                print("Erro ao carregar 'livros.json'. Criando arquivo vazio.")
                self._livros = []
                self.salvar_livros()
        else:
            print("Arquivo 'livros.json' não encontrado. Criando arquivo vazio.")
            self._livros = []
            self.salvar_livros()

    def salvar_livros(self):
        try:
            with open("livros.json", "w", encoding="utf-8") as arquivo:
                json.dump(self._livros, arquivo, indent=4, ensure_ascii=False)
            print("Livros salvos com sucesso.")
        except Exception as e:
            print(f"Erro ao salvar 'livros.json': {e}")

    def cadastrar_usuario(self, nome, id_usuario):
        id_usuario = str(id_usuario)  # Converte o ID para string
        if id_usuario in self._usuarios:
            print(f"Usuário com ID {id_usuario} já está cadastrado.")
            return

        self._usuarios[id_usuario] = {"nome": nome, "livros_emprestados": []}
        self.salvar_usuarios()
        print(f"Usuário '{nome}' cadastrado com sucesso.")

    def remover_cliente(self, usuario_id):
        usuario_id = str(usuario_id)  # Converte o ID para string
        if usuario_id in self._usuarios:
            usuario = self._usuarios[usuario_id]

            for titulo in usuario["livros_emprestados"]:
                for livro in self._livros:
                    if livro["titulo"] == titulo:
                        livro["disponivel"] = True

            del self._usuarios[usuario_id]
            self.salvar_usuarios()
            self.salvar_livros()
            print(f"Usuário com ID {usuario_id} foi removido com sucesso.")
        else:
            print(f"Usuário com ID {usuario_id} não encontrado.")

    def adicionar_livro(self, titulo, autor):
        for livro in self._livros:
            if livro["titulo"] == titulo and livro["autor"] == autor:
                print("Livro já cadastrado.")
                return

        novo_livro = {
            "id": str(uuid.uuid4()),  # Gera um ID único
            "titulo": titulo,
            "autor": autor,
            "disponivel": True
        }
        self._livros.append(novo_livro)
        self.salvar_livros()
        print(f"Livro '{titulo}' cadastrado com sucesso.")

    def emprestar_livro(self, id_usuario, titulo):
        id_usuario = str(id_usuario)  # Converte o ID para string
        print(f"ID fornecido: {id_usuario}")  # Debug
        print(f"Usuários disponíveis: {list(self._usuarios.keys())}")  # Debug

        usuario = self._usuarios.get(id_usuario)
        if not usuario:
            print(f"Usuário com ID {id_usuario} não encontrado.")
            return

        for livro in self._livros:
            if livro["titulo"] == titulo and livro["disponivel"]:
                livro["disponivel"] = False
                usuario["livros_emprestados"].append(titulo)
                self.salvar_usuarios()
                self.salvar_livros()
                print(f"Livro '{titulo}' emprestado para o usuário '{usuario['nome']}'.")
                return

        print(f"Livro '{titulo}' não está disponível para empréstimo.")

    def devolver_livro(self, id_usuario, titulo):
        id_usuario = str(id_usuario)  # Converte o ID para string
        usuario = self._usuarios.get(id_usuario)
        if not usuario:
            print(f"Usuário com ID {id_usuario} não encontrado.")
            return

        if titulo in usuario["livros_emprestados"]:
            usuario["livros_emprestados"].remove(titulo)
            for livro in self._livros:
                if livro["titulo"] == titulo:
                    livro["disponivel"] = True
            self.salvar_usuarios()
            self.salvar_livros()
            print(f"Livro '{titulo}' devolvido com sucesso.")
        else:
            print(f"O usuário '{usuario['nome']}' não possui o livro '{titulo}' emprestado.")

    def mostrar_relatorio_geral(self):
        print("\n--- Relatório de Usuários ---")
        if self._usuarios:
            for usuario_id, usuario in self._usuarios.items():
                print(f"ID: {usuario_id}, Nome: {usuario['nome']}, Livros emprestados: {', '.join(usuario['livros_emprestados']) or 'Nenhum'}")
        else:
            print("Nenhum usuário cadastrado.")

        print("\n--- Relatório de Livros ---")
        if self._livros:
            for livro in self._livros:
                status = "Disponível" if livro.get("disponivel", False) else "Emprestado"
                print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Status: {status}")
        else:
            print("Nenhum livro cadastrado.")

    def remover_livro_biblioteca(self, livro_id):
        livro_encontrado = None
        for livro in self._livros:
            if livro.get("id") == livro_id:
                livro_encontrado = livro
                break

        if not livro_encontrado:
            print(f"Livro com ID '{livro_id}' não encontrado na biblioteca.")
            return

        if not livro_encontrado.get("disponivel", True):
            print(f"Não é possível remover o livro '{livro_encontrado['titulo']}'. O livro está atualmente emprestado.")
            return

        self._livros.remove(livro_encontrado)
        self.salvar_livros()
        print(f"Livro '{livro_encontrado['titulo']}' foi removido da biblioteca com sucesso.")
