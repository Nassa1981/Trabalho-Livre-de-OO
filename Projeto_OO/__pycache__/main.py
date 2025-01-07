from livro import Livro
from emprestimo_devolução import Emprestimo
from usuario import Usuario
from biblioteca import Biblioteca
from documentation import Documentation
from item import Item
from tchau_biblioteca import TchauBiblioteca


def exibir_menu():
    print("\n========== SISTEMA BIBLIOTECÁRIO ===========")
    print("\nMENU:")
    print("1. Cadastrar Cliente")
    print("2. Remover Cliente")
    print("3. Alterar Dados do Cliente")
    print("4. Cadastrar Livro")
    print("5. Emprestar Livro")
    print("6. Devolver Livro")
    print("7. Mostrar Clientes Cadastrados")
    print("8. Mostrar Livros Cadastrados")
    print("9. Remover Livro da Biblioteca")
    print("10. Mostrar Documentação")
    print("11. Sair")


if __name__ == "__main__":
    biblioteca = Biblioteca()
    tchauBiblioteca = TchauBiblioteca()

    while True:
        exibir_menu()
        try:
            opcao = input("Escolha uma opção: ").strip()
        except Exception as e:
            print(f"Erro ao selecionar opção: {e}")
            continue

        if opcao == "1":
            nome_cliente = input("Digite o nome do cliente: ").strip()
            id_cliente = input("Digite o ID do cliente: ").strip()
            biblioteca.cadastrar_usuario(nome_cliente, id_cliente)

        elif opcao == "2":
            id_cliente = input("Digite o ID do cliente a ser removido: ").strip()
            tchauBiblioteca.remover_cliente(id_cliente)

        elif opcao == "3":
            id_cliente = input("Digite o ID do cliente a ser alterado: ").strip()
            if id_cliente in biblioteca._usuarios:
                novo_nome = input("Digite o novo nome: ").strip()
                biblioteca._usuarios[id_cliente]["nome"] = novo_nome
                print("Nome do cliente alterado.")
                biblioteca.salvar_usuarios()
            else:
                print("Usuário não encontrado.")

        elif opcao == "4":
            titulo_livro = input("Digite o título do livro: ").strip()
            autor_livro = input("Digite o autor do livro: ").strip()
            biblioteca.adicionar_livros(titulo_livro, autor_livro)

        elif opcao == "5":
            id_cliente = input("Digite o ID do cliente: ").strip()
            titulo_livro = input("Digite o título do livro: ").strip()
            autor_livro = input("Digite o autor do livro: ").strip()
            biblioteca.emprestar_livro(id_cliente, titulo_livro, autor_livro)


        elif opcao == "6":
            id_cliente = input("Digite o ID do cliente: ").strip()
            titulo_livro = input("Digite o título do livro: ").strip()
            tchauBiblioteca.devolver_livro(id_cliente, titulo_livro)

        elif opcao == "7":
            biblioteca.mostrar_clientes()

        elif opcao == "8":
            biblioteca.mostrar_livros_cadastrados()

        elif opcao == "9":
            livro_id = input("Digite o ID do livro a ser removido: ").strip()
            tchauBiblioteca.remover_livro_biblioteca(livro_id)

        elif opcao == "10":
            Documentation.register(Livro)
            Documentation.register(Emprestimo)
            Documentation.register(Usuario)
            Documentation.register(Biblioteca)
            Documentation.register(Item)

            def exibir_documentacao(classe):
                if issubclass(classe, Documentation):
                    if not hasattr(classe, "documentation"):
                        raise Exception(f"A classe {classe.__name__} não implementou o método 'documentation'.")
                    else:
                        print(classe.documentation())
                else:
                    print(f"A classe {classe.__name__} não é uma subclasse de 'Documentation'.")

            while True:
                print("\nEscolha uma classe para ver a documentação: ")
                print("1. Livro")
                print("2. Empréstimo")
                print("3. Usuário")
                print("4. Biblioteca")
                print("5. Item")
                print("6. Voltar Para o Menu Principal")

                escolha = input("Informe a opção desejada: ").strip()

                if escolha == "1":
                    exibir_documentacao(Livro)
                elif escolha == "2":
                    exibir_documentacao(Emprestimo)
                elif escolha == "3":
                    exibir_documentacao(Usuario)
                elif escolha == "4":
                    exibir_documentacao(Biblioteca)
                elif escolha == "5":
                    exibir_documentacao(Item)
                elif escolha == "6":
                    print("Voltando para o menu principal...")
                    break
                else:
                    print("Opção incorreta, tente novamente!")

        elif opcao == "11":
            print("Encerrando o sistema da biblioteca...")
            print("Sistema encerrado!")
            break

        else:
            print("Opção inválida. Tente novamente!")
