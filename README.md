Eu só pedi pro gpt criar esse único arquivo -_-.

---

#  Sistema de Catálogo de Filmes — Django (Class-Based Views)

##  Descrição

Este projeto é um sistema web desenvolvido com **Django**, utilizando **Class-Based Views (CBV)**, com o objetivo de gerenciar um catálogo de filmes.
O sistema permite **cadastrar**, **listar**, **visualizar detalhes**, **atualizar** e **excluir** filmes.

---

##  Tecnologias Utilizadas

* **Python 3.13**
* **Django 5.2**
* **HTML5 / CSS3 (templates simples)**
* **SQLite3** (banco de dados padrão do Django)

---

##  Estrutura do Projeto

```
atv_class_based_view/
├── core/
│   ├── settings.py
│   ├── urls.py
│   └── views.py
├── filmes/
│   ├── migrations/
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── forms.py
│   └── templates/
│       ├── filmes_list.html
│       ├── filmes_detail.html
│       ├── filmes_form.html
│       └── filmes_confirm_delete.html
└── manage.py
```

---

##  Modelo (Model)

O modelo principal é o **Filme**, com os seguintes campos:

| Campo        | Tipo           | Descrição          |
| ------------ | -------------- | ------------------ |
| `nome`       | `CharField`    | Nome do filme      |
| `duracao`    | `IntegerField` | Duração em minutos |
| `lancamento` | `DateField`    | Data de lançamento |
| `genero`     | `CharField`    | Gênero do filme    |
| `diretor`    | `CharField`    | Nome do diretor    |

---

##  Funcionalidades

| View                  | Classe Django | Descrição                                        |
| --------------------- | ------------- | ------------------------------------------------ |
| **Listar Filmes**     | `ListView`    | Exibe todos os filmes cadastrados                |
| **Detalhes do Filme** | `DetailView`  | Mostra informações detalhadas de um filme        |
| **Criar Filme**       | `CreateView`  | Permite adicionar um novo filme                  |
| **Editar Filme**      | `UpdateView`  | Permite editar informações de um filme existente |
| **Excluir Filme**     | `DeleteView`  | Exibe uma confirmação antes de excluir o filme   |

---

##  Rotas Principais

| Rota                        | View         | Descrição                                |
| --------------------------- | ------------ | ---------------------------------------- |
| `/`                         | `home`       | Página inicial do sistema                |
| `/filmes/list/`             | `FilmList`   | Lista todos os filmes                    |
| `/filmes/create/`           | `FilmCreate` | Formulário para cadastrar novo filme     |
| `/filmes/<int:pk>/details/` | `FilmDetail` | Mostra detalhes de um filme específico   |
| `/filmes/<int:pk>/update/`  | `FilmUpdate` | Formulário para editar filme             |
| `/filmes/<int:pk>/delete/`  | `FilmDelete` | Página de confirmação para excluir filme |

---

## Templates

* **filmes_list.html** → lista de filmes
* **filmes_detail.html** → detalhes do filme
* **filmes_form.html** → formulário usado no *create* e *update*
* **filmes_confirm_delete.html** → confirmação de exclusão

---

## Como Executar o Projeto

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seuusuario/nome-do-repositorio.git
   cd nome-do-repositorio
   ```

2. **Crie e ative um ambiente virtual:**

   ```bash
   python -m venv venv
   venv\Scripts\activate  # (Windows)
   source venv/bin/activate  # (Linux/Mac)
   ```

3. **Instale as dependências:**

   ```bash
   pip install django
   ```

4. **Execute as migrações:**

   ```bash
   python manage.py migrate
   ```

5. **Inicie o servidor:**

   ```bash
   python manage.py runserver
   ```

6. **Acesse o sistema em:**
    [http://localhost:8000/](http://localhost:8000/)

---

**Nome:** *[Pedro Henrique de Lima Silva]*
**Curso:** Desenvolvimento Web com Django
**Professor:** *[Jefferson Queiroga]*

---
