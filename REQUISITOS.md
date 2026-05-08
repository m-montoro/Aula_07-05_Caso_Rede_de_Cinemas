# 📋 Requisitos e Regras de Negócio

## Sistema de Rede de Cinemas

---

## 1. Requisitos Funcionais

| ID | Descrição | Ator |
|---|---|---|
| RF01 | O sistema deve permitir o cadastro de filmes informando título, diretor, gênero e duração em minutos. | Funcionário |
| RF02 | O sistema deve listar todos os filmes cadastrados com suas informações completas. | Funcionário / Espectador |
| RF03 | O sistema deve permitir o cadastro de sessões, vinculando um filme a um cinema com horário e sala definidos. | Funcionário |
| RF04 | O sistema deve listar todas as sessões cadastradas, podendo filtrar por cinema. | Funcionário / Espectador |
| RF05 | O sistema deve permitir o registro da quantidade de público presente em uma sessão. | Funcionário |
| RF06 | O sistema deve calcular e exibir o total acumulado de público de todas as sessões de um determinado filme. | Funcionário |

---

## 2. Requisitos Não Funcionais

| ID | Descrição |
|---|---|
| RNF01 | O sistema deve persistir todos os dados em banco de dados SQLite local. |
| RNF02 | O sistema deve ser desenvolvido em Python 3.8 ou superior. |
| RNF03 | O sistema deve utilizar arquitetura em camadas: MVC + Service + Repository. |
| RNF04 | O sistema não deve depender de bibliotecas externas além da biblioteca padrão do Python. |
| RNF05 | O sistema deve apresentar mensagens claras de erro para entradas inválidas. |
| RNF06 | A integridade referencial entre tabelas deve ser garantida via chaves estrangeiras. |

---

## 3. Regras de Negócio

| ID | Descrição |
|---|---|
| RN01 | Título e diretor são campos obrigatórios no cadastro de filmes. |
| RN02 | A duração do filme deve ser um número inteiro maior que zero. |
| RN03 | Horário e sala são campos obrigatórios no cadastro de sessão. |
| RN04 | Uma sessão só pode ser criada se o filme informado existir no sistema. |
| RN05 | A quantidade de público registrada em uma sessão não pode ser negativa. |
| RN06 | O público de uma sessão é acumulativo: novos registros somam ao valor existente. |
| RN07 | Cada sessão pertence a exatamente um cinema e exibe exatamente um filme. |
| RN08 | O total de público por filme é a soma do público de todas as suas sessões. |

---

## 4. Casos de Uso

### UC01 — Cadastrar Filme
- **Ator:** Funcionário
- **Pré-condição:** Nenhuma
- **Fluxo principal:**
  1. Funcionário acessa o menu de filmes
  2. Informa título, diretor, gênero e duração
  3. Sistema valida os dados (RN01, RN02)
  4. Sistema persiste o filme no banco
  5. Sistema exibe mensagem de sucesso
- **Fluxo alternativo:** Dados inválidos → sistema exibe mensagem de erro

### UC02 — Listar Filmes
- **Ator:** Funcionário / Espectador
- **Pré-condição:** Nenhuma
- **Fluxo principal:**
  1. Ator acessa o menu de filmes
  2. Sistema consulta todos os filmes no banco
  3. Sistema exibe a lista com id, título, diretor, gênero e duração

### UC03 — Cadastrar Sessão
- **Ator:** Funcionário
- **Pré-condição:** Filme cadastrado no sistema (RF01)
- **Fluxo principal:**
  1. Funcionário acessa o menu de sessões
  2. Informa ID do filme, ID do cinema, horário e sala
  3. Sistema valida os dados (RN03, RN04)
  4. Sistema persiste a sessão no banco
  5. Sistema exibe mensagem de sucesso
- **Fluxo alternativo:** Filme não encontrado → sistema exibe mensagem de erro

### UC04 — Listar Sessões
- **Ator:** Funcionário / Espectador
- **Pré-condição:** Nenhuma
- **Fluxo principal:**
  1. Ator acessa o menu de sessões
  2. Sistema consulta todas as sessões
  3. Sistema exibe a lista com id, filme, cinema, horário, sala e público atual

### UC05 — Registrar Público
- **Ator:** Funcionário
- **Pré-condição:** Sessão cadastrada no sistema (RF03)
- **Fluxo principal:**
  1. Funcionário acessa o menu de sessões
  2. Informa ID da sessão e quantidade de público
  3. Sistema valida a quantidade (RN05)
  4. Sistema acumula o valor ao público da sessão (RN06)
  5. Sistema exibe mensagem de sucesso
- **Fluxo alternativo:** Quantidade negativa → sistema exibe mensagem de erro

### UC06 — Consultar Total de Público por Filme
- **Ator:** Funcionário
- **Pré-condição:** Filme e sessões cadastradas
- **Fluxo principal:**
  1. Funcionário acessa o menu de sessões
  2. Informa o ID do filme
  3. Sistema soma o público de todas as sessões do filme (RN08)
  4. Sistema exibe o total

---

## 5. Modelo de Dados

```
cinemas
  id          INTEGER PK
  nome        TEXT NOT NULL
  cidade      TEXT NOT NULL
  estado      TEXT NOT NULL
  capacidade  INTEGER NOT NULL

filmes
  id          INTEGER PK
  titulo      TEXT NOT NULL
  diretor     TEXT NOT NULL
  genero      TEXT NOT NULL
  duracao_min INTEGER NOT NULL

sessoes
  id          INTEGER PK
  filme_id    INTEGER FK → filmes.id
  cinema_id   INTEGER FK → cinemas.id
  horario     TEXT NOT NULL
  sala        TEXT NOT NULL
  publico     INTEGER DEFAULT 0
```
