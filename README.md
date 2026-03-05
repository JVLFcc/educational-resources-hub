# 📚 Hub Inteligente de Recursos Educacionais

Sistema fullstack para gerenciamento de recursos educacionais com integração a LLM (Gemini) para geração automática de descrições e tags.

---

## 🚀 Visão Geral

O **Hub Inteligente de Recursos Educacionais** é uma aplicação web SPA (Single Page Application) que permite:

- 📌 Cadastro de recursos educacionais
- 📋 Listagem paginada
- ✏️ Edição
- 🗑 Exclusão
- 🤖 Geração automática de descrição e tags usando IA (Google Gemini)

O sistema foi desenvolvido seguindo os requisitos técnicos do desafio, com foco em:

- Arquitetura limpa
- Validação estruturada
- Integração segura com LLM
- Experiência do usuário com feedback visual

---

# 🏗 Arquitetura

## Backend
- **FastAPI**
- **SQLite**
- **SQLAlchemy**
- **Pydantic**
- **Integração com Gemini 2.5 Flash**
- Logging de Token Usage e Latência

## Frontend
- **React (Vite)**
- SPA
- Consumo de API REST
- Loading state
- Tratamento de erros

---

# 🧠 Funcionalidade Smart Assist (IA)

Ao clicar em **"Gerar Descrição com IA"**:

1. O frontend envia:
   - Título
   - Tipo do recurso

2. O backend:
   - Envia requisição para o modelo `gemini-2.5-flash`
   - Utiliza um **System Prompt estruturado**
   - Força resposta em JSON estrito
   - Retorna:
     - Descrição pedagógica
     - 3 tags específicas

3. O frontend:
   - Preenche automaticamente os campos
   - Exibe estado de loading
   - Trata erros de requisição

---

# 📦 Estrutura do Projeto
# 📚 Hub Inteligente de Recursos Educacionais

Sistema fullstack para gerenciamento de recursos educacionais com integração a LLM (Gemini) para geração automática de descrições e tags.

---

## 🚀 Visão Geral

O **Hub Inteligente de Recursos Educacionais** é uma aplicação web SPA (Single Page Application) que permite:

- 📌 Cadastro de recursos educacionais
- 📋 Listagem paginada
- ✏️ Edição
- 🗑 Exclusão
- 🤖 Geração automática de descrição e tags usando IA (Google Gemini)

O sistema foi desenvolvido seguindo os requisitos técnicos do desafio, com foco em:

- Arquitetura limpa
- Validação estruturada
- Integração segura com LLM
- Experiência do usuário com feedback visual

---

# 🏗 Arquitetura

## Backend
- **FastAPI**
- **SQLite**
- **SQLAlchemy**
- **Pydantic**
- **Integração com Gemini 2.5 Flash**
- Logging de Token Usage e Latência

## Frontend
- **React (Vite)**
- SPA
- Consumo de API REST
- Loading state
- Tratamento de erros

---

# 🧠 Funcionalidade Smart Assist (IA)

Ao clicar em **"Gerar Descrição com IA"**:

1. O frontend envia:
   - Título
   - Tipo do recurso

2. O backend:
   - Envia requisição para o modelo `gemini-2.5-flash`
   - Utiliza um **System Prompt estruturado**
   - Força resposta em JSON estrito
   - Retorna:
     - Descrição pedagógica
     - 3 tags específicas

3. O frontend:
   - Preenche automaticamente os campos
   - Exibe estado de loading
   - Trata erros de requisição

---

# 📦 Estrutura do Projeto
# 📚 Hub Inteligente de Recursos Educacionais

Sistema fullstack para gerenciamento de recursos educacionais com integração a LLM (Gemini) para geração automática de descrições e tags.

---

## 🚀 Visão Geral

O **Hub Inteligente de Recursos Educacionais** é uma aplicação web SPA (Single Page Application) que permite:

- 📌 Cadastro de recursos educacionais
- 📋 Listagem paginada
- ✏️ Edição
- 🗑 Exclusão
- 🤖 Geração automática de descrição e tags usando IA (Google Gemini)

O sistema foi desenvolvido seguindo os requisitos técnicos do desafio, com foco em:

- Arquitetura limpa
- Validação estruturada
- Integração segura com LLM
- Experiência do usuário com feedback visual

---

# 🏗 Arquitetura

## Backend
- **FastAPI**
- **SQLite**
- **SQLAlchemy**
- **Pydantic**
- **Integração com Gemini 2.5 Flash**
- Logging de Token Usage e Latência

## Frontend
- **React (Vite)**
- SPA
- Consumo de API REST
- Loading state
- Tratamento de erros

---

# 🧠 Funcionalidade Smart Assist (IA)

Ao clicar em **"Gerar Descrição com IA"**:

1. O frontend envia:
   - Título
   - Tipo do recurso

2. O backend:
   - Envia requisição para o modelo `gemini-2.5-flash`
   - Utiliza um **System Prompt estruturado**
   - Força resposta em JSON estrito
   - Retorna:
     - Descrição pedagógica
     - 3 tags específicas

3. O frontend:
   - Preenche automaticamente os campos
   - Exibe estado de loading
   - Trata erros de requisição

---

# 📦 Estrutura do Projeto

├── backend/
│ ├── app/
│ │ ├── models.py
│ │ ├── schemas.py
│ │ ├── resources.py
│ │ ├── ia_services.py
│ │ ├── health.py
│ │ └── main.py
│ ├── requirements.txt
│
├── frontend/
│ ├── src/
│ │ └── App.jsx
│ ├── package.json
│ ├── package.json
│ └── vite.config.js
│
└── README.md