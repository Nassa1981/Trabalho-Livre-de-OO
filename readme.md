# **Sistema de Gerenciamento de Biblioteca**

Um sistema desenvolvido com princípios de **Orientação a Objetos (OO)**, permitindo gerenciar livros, usuários e empréstimos. Ideal para o aprendizado e aplicação de conceitos de programação orientada a objetos.

---

## **Funcionalidades**

### **Gerenciamento de Livros**
- Adicionar novos livros ao catálogo da biblioteca.
- Listar todos os livros cadastrados.
- Verificar a disponibilidade de um livro específico.
- Remover livros da biblioteca.

### **Gerenciamento de Usuários**
- Cadastrar novos usuários com nome e ID exclusivo.
- Alterar dados de um cliente cadastrado.
- Listar todos os usuários cadastrados.
- Remover clientes da biblioteca.

### **Empréstimos e Devoluções**
- Realizar empréstimos de livros disponíveis, associando-os a um usuário.
- Devolver livros e atualizar automaticamente o status de disponibilidade.
- Exibir a lista de livros emprestados por cada usuário.

### **Persistência de Dados**
- Armazenamento persistente dos dados em arquivos JSON:
  - **livros.json**: Contém as informações dos livros cadastrados e sua disponibilidade.
  - **usuarios.json**: Contém os dados dos usuários e os livros que estão emprestados.

---

## **Terminal do Menu**

### **Interface Principal**
Ao executar o programa, o sistema exibe o seguinte menu no terminal:

```plaintext
========== SISTEMA BIBLIOTECÁRIO ===========

MENU:
1. Cadastrar Cliente
2. Remover Cliente
3. Alterar Dados do Cliente
4. Cadastrar Livro
5. Emprestar Livro
6. Devolver Livro
7. Mostrar Clientes Cadastrados
8. Mostrar Livros Cadastrados
9. Remover Livro da Biblioteca
10. Mostrar Documentação
11. Sair
