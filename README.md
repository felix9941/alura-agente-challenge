# 🤖 CloudFlow AI Agent

Un agente inteligente basado en RAG (Retrieval-Augmented Generation) capaz de responder preguntas sobre la documentación interna de una plataforma SaaS.

El proyecto fue desarrollado como solución al **Challenge Alura Agente**, utilizando LangChain, Google Gemini, ChromaDB y FastAPI.

---

# 📌 Características

- Procesamiento automático de documentos PDF.
- Generación de embeddings mediante Google Gemini.
- Almacenamiento vectorial con ChromaDB.
- Recuperación inteligente de contexto (RAG).
- API REST desarrollada con FastAPI.
- Frontend desarrollado con React + Vite.
- Preparado para despliegue en Oracle Cloud Infrastructure (OCI).

---

# 🏗 Arquitectura

```
                    +-----------------------+
                    |      React Frontend   |
                    +-----------+-----------+
                                |
                                | HTTP
                                |
                    +-----------v-----------+
                    |      FastAPI API      |
                    +-----------+-----------+
                                |
                                |
                         RAG Pipeline
                                |
                +---------------+---------------+
                |                               |
        Retriever                        Gemini LLM
                |                               |
                +---------------+---------------+
                                |
                         Chroma Vector DB
                                |
                     Document Embeddings
                                |
                      PDF Document Loader
                                |
                    FAQ - Pricing - Privacy
                          Terms of Use
```

---

# 📁 Estructura del Proyecto

```
alura-agent/

│
├── backend/
│   │
│   ├── app/
│   │   ├── ingestion/
│   │   ├── models/
│   │   ├── services/
│   │   ├── config.py
│   │   ├── rag.py
│   │   ├── prompts.py
│   │   └── main.py
│   │
│   ├── data/
│   │   ├── faq.pdf
│   │   ├── pricing.pdf
│   │   ├── privacy.pdf
│   │   └── terms.pdf
│   │
│   ├── scripts/
│   │   └── ingest.py
│   │
│   ├── vectorstore/
│   │
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│
├── Dockerfile
│
└── README.md
```

---

# 🛠 Tecnologías

## Backend

- Python
- FastAPI
- LangChain
- Google Gemini
- ChromaDB
- PyPDF
- Uvicorn

## Frontend

- React
- Vite
- Axios

## Infraestructura

- Docker
- Oracle Cloud Infrastructure (OCI)

---

# ⚙ Instalación

## Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/alura-agent.git

cd alura-agent
```

---

## Backend

```bash
cd backend

python -m venv venv
```

Activar entorno virtual

Windows

```bash
venv\Scripts\activate
```

Instalar dependencias

```bash
pip install -r requirements.txt
```

Crear archivo `.env`

```env
GOOGLE_API_KEY=TU_API_KEY
```

---

## Frontend

```bash
cd ../frontend

npm install
```

---

# ▶ Ejecutar el proyecto

Backend

```bash
uvicorn app.main:app --reload
```

Frontend

```bash
npm run dev
```

---

# 📄 Documentación utilizada

La base de conocimiento del agente está compuesta por los siguientes documentos:

- FAQ
- Planes y Precios
- Política de Privacidad
- Términos de Uso

---

# 💬 Ejemplos de preguntas

- ¿Qué incluye el plan Enterprise?

- ¿Cómo recupero mi contraseña?

- ¿Cuál es el tiempo de respuesta del soporte?

- ¿CloudFlow vende información personal?

- ¿Cómo puedo exportar mis datos?

- ¿Qué navegadores son compatibles?

- ¿Qué descuento tiene el pago anual?

---

# 💡 Ejemplo de respuesta

Pregunta

```
¿Qué incluye el plan Enterprise?
```

Respuesta

```
El plan Enterprise incluye usuarios ilimitados,
SSO, backups horarios, almacenamiento ilimitado,
soporte técnico 24/7 y un gerente de cuenta dedicado.
```

---

# ☁ Deploy

El proyecto fue desplegado utilizando Oracle Cloud Infrastructure (OCI).

URL

```
https://xxxxxxxxxxxx
```

---

# 📸 Evidencias

## Aplicación

_(Agregar captura del frontend.)_

## API

_(Agregar captura de Swagger.)_

## OCI

_(Agregar captura del despliegue.)_

---

# 👨‍💻 Autor

Felix Ignacio Figueroa
Ingeniero en Sistemas de Información
