# 🎬 Sistema de Rede de Cinemas

Projeto de Engenharia de Software desenvolvido com arquitetura **MVC + Service + Repository**, persistência em **SQLite** e interface de linha de comando (CLI).

---

## 📋 Descrição

Sistema de informação para gerenciamento de uma rede de cinemas distribuída em múltiplas cidades e estados. Permite o controle de filmes em cartaz, sessões diárias e registro de público.

---

## 🏗️ Arquitetura

```
cinema_project/
 ├── controller/
 │   ├── filme_controller.py
 │   └── sessao_controller.py
 ├── service/
 │   ├── filme_service.py
 │   └── sessao_service.py
 ├── repository/
 │   ├── filme_repository.py
 │   └── sessao_repository.py
 ├── model/
 │   ├── filme.py
 │   ├── sessao.py
 │   └── cinema.py
 ├── view/
 │   └── cinema_view.py
 ├── db/
 │   └── database.py
 └── main.py
```

### Responsabilidades das Camadas

| Camada | Responsabilidade |
|---|---|
| **Model** | Entidades do domínio (Filme, Sessao, Cinema) |
| **Repository** | Acesso e persistência no banco SQLite |
| **Service** | Regras de negócio e validações |
| **Controller** | Orquestra View ↔ Service |
| **View** | Interface CLI — menus e entrada de dados |

---

## ⚙️ Requisitos

- Python 3.8+
- Sem dependências externas (usa `sqlite3` da stdlib)

---

## ▶️ Como Executar

```bash
# Acesse a pasta do projeto
cd cinema_project

# Execute o sistema
python main.py
```

O banco de dados `cinema.db` será criado automaticamente na primeira execução.

---

## 🗂️ Funcionalidades

### Filmes
- Cadastrar filme (título, diretor, gênero, duração)
- Listar todos os filmes em cartaz

### Sessões
- Cadastrar sessão (vinculada a filme e cinema, com horário e sala)
- Listar sessões cadastradas
- Registrar público de uma sessão
- Consultar total de público por filme

---

## 🗃️ Banco de Dados

Três tabelas SQLite com chaves estrangeiras:

```sql
filmes      (id, titulo, diretor, genero, duracao_min)
cinemas     (id, nome, cidade, estado, capacidade)
sessoes     (id, filme_id, cinema_id, horario, sala, publico)
```

---

## 📐 Diagramas UML

Os diagramas estão na pasta `/diagramas` no formato `.puml` (PlantUML):

| Arquivo | Conteúdo |
|---|---|
| `diagrama_classes.puml` | Estrutura estática das entidades |
| `diagrama_casos_de_uso.puml` | Atores e casos de uso do sistema |
| `diagrama_atividade_cadastrar_filme.puml` | Fluxo de cadastro de filme |
| `diagrama_atividade_registrar_publico.puml` | Fluxo de registro de público |
| `diagrama_sequencia_cadastrar_filme.puml` | Sequência de cadastro de filme |
| `diagrama_sequencia_registrar_publico.puml` | Sequência de registro de público |

> Visualize os diagramas em [https://www.plantuml.com/plantuml/uml](https://www.plantuml.com/plantuml/uml) ou com a extensão PlantUML no VS Code.

---

## 👥 Atores do Sistema

- **Funcionário / Administrador** — gerencia filmes, sessões e registra público
- **Espectador** — consulta filmes em cartaz e horários de sessões

---

## 📄 Licença

Projeto acadêmico — uso educacional.
