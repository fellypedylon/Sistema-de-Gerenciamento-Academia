# 🏋️ Corpo em Movimento | Gestão de Treinos

Sistema de linha de comando (CLI) para gerenciamento de fichas de treino de academia, desenvolvido em Python.

---

## 📜 Descrição

O projeto foi criado para facilitar a organização de rotinas de exercícios para personal trainers ou pequenas academias. Em vez de usar papel ou planilhas complexas, este sistema oferece uma interface de texto rápida e direta para gerenciar as informações essenciais dos treinos.

Os dados são armazenados em um arquivo **JSON**, garantindo que as informações persistam entre as execuções do programa.

---

## ✨ Funcionalidades

* **Cadastrar Nova Ficha** — Adiciona uma nova ficha de treino para um aluno, incluindo nome, objetivo, data de início e uma lista de exercícios com séries e repetições.
* **Consultar Ficha por Nome** — Busca e exibe os detalhes completos de uma ficha a partir do nome do aluno.
* **Listar Todos os Treinos** — Apresenta uma visão resumida de todas as fichas cadastradas.
* **Editar Ficha** — Permite modificar as informações de uma ficha já existente.
* **Excluir Ficha** — Remove uma ficha do sistema.
* **Validação de Entradas** — Garante que os dados inseridos pelo usuário estão no formato correto antes de salvar.
* **Interface Limpa** — O sistema limpa a tela a cada ação para manter a interface organizada e fácil de ler.

---

## 🚀 Como Executar

Para rodar o projeto, você precisa ter o **Python 3** instalado em sua máquina.

1. Navegue até o diretório onde o arquivo `academia.py` está localizado.
2. Execute o seguinte comando no seu terminal:

```bash
python academia.py
```

3. O menu principal será exibido e você poderá interagir com o sistema digitando as opções desejadas.

---

## 🔧 Estrutura do Código

* `academia.py` — Arquivo principal com toda a lógica do sistema.
* `fichas.json` — Arquivo gerado automaticamente para persistência dos dados.

**Funções principais:**

* `main()` — Controla o loop do menu e direciona o usuário para as outras funções.
* `cadastrar()` — Coleta os dados do aluno e dos exercícios e salva no arquivo JSON.
* `consultar()` — Busca por um aluno e exibe seus dados.
* `listar()` — Percorre as fichas e imprime um resumo de cada uma.
* `editar()` — Permite modificar uma ficha já cadastrada.
* `excluir()` — Remove uma ficha do sistema.
* `salvar_dados()` / `carregar_dados()` — Gerenciam a leitura e escrita no arquivo JSON.
* `limpar()` e `aguardar_enter()` — Funções utilitárias para melhorar a experiência no console.

---

## ✅ Melhorias Implementadas

* [x] Persistência de dados em arquivo JSON
* [x] Editar ficha existente
* [x] Excluir ficha
* [x] Validação de entradas

---

## 🔮 Próximos Passos

* [ ] Migrar para banco de dados SQLite
* [ ] Adicionar busca por objetivo ou data
* [ ] Criar relatório de treinos por período
* [ ] Desenvolver interface gráfica (GUI)

---

## 👨‍💻 Autor

Desenvolvido por **Fellype Dylon Souza Arrais**.