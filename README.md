# Corpo em Movimento | Gestão de Treinos

Este é um sistema simples de linha de comando (CLI) para gerenciamento de fichas de treino de academia, desenvolvido em Python. Ele permite cadastrar, consultar e listar as fichas de treino dos alunos.

## 📜 Descrição

O projeto foi criado para facilitar a organização de rotinas de exercícios para personal trainers ou pequenas academias. Em vez de usar papel ou planilhas complexas, este sistema oferece uma interface de texto rápida e direta para gerenciar as informações essenciais dos treinos.

Os dados são armazenados em memória durante a execução do programa.

## ✨ Funcionalidades

- **Cadastrar Nova Ficha**: Permite adicionar uma nova ficha de treino para um aluno, incluindo seu nome, objetivo, data de início e uma lista de exercícios com séries e repetições.
- **Consultar Ficha por Nome**: Busca e exibe os detalhes completos de uma ficha de treino a partir do nome do aluno.
- **Listar Todos os Treinos**: Apresenta uma visão resumida de todas as fichas cadastradas, mostrando as informações principais de cada uma.
- **Interface Limpa**: O sistema limpa a tela a cada ação para manter a interface organizada e fácil de ler.

## 🚀 Como Executar

Para rodar o projeto, você precisa ter o Python 3 instalado em sua máquina.

1.  Navegue até o diretório onde o arquivo `academia.py` está localizado.
2.  Execute o seguinte comando no seu terminal:

    ```bash
    python academia.py
    ```

3.  O menu principal será exibido, e você poderá interagir com o sistema digitando as opções desejadas.

## 🔧 Estrutura do Código

- **`FICHAS`**: Uma lista global que atua como um banco de dados em memória para armazenar as fichas (que são dicionários).
- **`main()`**: A função principal que controla o loop do menu e direciona o usuário para as outras funções com base na sua escolha.
- **`cadastrar()`**: Responsável por coletar os dados do aluno e dos exercícios e adicioná-los à lista `FICHAS`.
- **`consultar()`**: Busca por um aluno na lista `FICHAS` e exibe seus dados.
- **`listar()`**: Percorre a lista `FICHAS` e imprime um resumo de cada uma.
- **`limpar()`** e **`aguardar_enter()`**: Funções utilitárias para melhorar a experiência do usuário no console.

## 🔮 Próximos Passos

O projeto pode ser expandido com as seguintes funcionalidades:

- [ ] **Persistência de Dados**: Salvar as fichas em um arquivo (como JSON, CSV) ou em um banco de dados (SQLite) para que os dados não sejam perdidos ao fechar o programa.
- [ ] **Editar Ficha**: Adicionar uma opção para modificar informações de uma ficha já existente.
- [ ] **Excluir Ficha**: Implementar a funcionalidade para remover uma ficha do sistema.
- [ ] **Validação de Entradas**: Melhorar a validação dos dados inseridos pelo usuário (ex: garantir que a data está no formato correto).
