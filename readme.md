# **Sistema de Gerenciamento de Biblioteca**

Um sistema desenvolvido com princípios de **Orientação a Objetos (OO)**, permitindo gerenciar livros, usuários e empréstimos. Ideal para o aprendizado e aplicação de conceitos de programação orientada a objetos, mas como foi o meu primeiro projeto, o codigo não ficou tão refinado e pode haver alguns problemas que não percebi.

Nome: Davi Rodrigues Nunes

Matrícula: 232014413

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
## **Tecnologias Utilizadas**
- **Python**: Linguagem de programação para implementação do sistema.
- **JSON**: Formato utilizado para armazenar os dados de maneira estruturada.

---

## **Conceitos de Orientação a Objetos**

### **Abstração**
Representação dos principais elementos de uma biblioteca, como livros, usuários e empréstimos.

### **Encapsulamento**
Proteção dos atributos e métodos privados para evitar alterações indevidas de dados.

### **Herança**
Uso de uma classe base `Item` para representar itens gerais da biblioteca, podendo ser especializada em classes concretas, como `LivroConcreto`.

### **Polimorfismo**
Implementação de métodos abstratos de forma específica em subclasses, como a definição e verificação de disponibilidade de itens.

---

## Como usar
Esse projeto foi testado utilizando o Vscode

Para iniciarmos iremos clonar o repositório para o sistema local:
```
git clone https://github.com/Nassa1981/Trabalho-Livre-de-OO.git
```
Agora que já temos o repositório na maquina, iremos acessar o mesmo com o seguinte comando:
```
cd Trabalho-Livre-de-OO
```
Diante disso, iremos baixar as bibliotecas utilizadas no programa usando o pip, com o seguinte comando:
```
pip install -r requirements.txt
```
Agora que você instalou as dependências, pode executar o projeto. Para isso, utilize o seguinte comando:
```
python main.py```
---
```
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
```
