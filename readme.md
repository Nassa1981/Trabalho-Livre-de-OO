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
Tecnologias Utilizadas
Python: Linguagem de programação para implementação do sistema.
JSON: Formato utilizado para armazenar os dados de maneira estruturada.
Conceitos de Orientação a Objetos
Abstração
Representação dos principais elementos de uma biblioteca, como livros, usuários e empréstimos.

Encapsulamento
Proteção dos atributos e métodos privados para evitar alterações indevidas de dados.

Herança
Uso de uma classe base Item para representar itens gerais da biblioteca, podendo ser especializada em classes concretas, como LivroConcreto.

Polimorfismo
Implementação de métodos abstratos de forma específica em subclasses, como a definição e verificação de disponibilidade de itens.

Como Usar
Passo 1: Clonar o Repositório
Abra o terminal ou o Git Bash e execute os comandos abaixo:

bash
Copiar código
git clone https://github.com/Nassa1981/Trabalho-Livre-de-OO.git
cd Trabalho-Livre-de-OO
Passo 2: Instalar Dependências
Se necessário, instale os pacotes necessários:

bash
Copiar código
pip install -r requirements.txt
Passo 3: Executar o Sistema
Inicie o sistema com o comando:

bash
Copiar código
python main.py











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
