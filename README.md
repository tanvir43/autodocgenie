# 🚀 AutoDocGenie

**AutoDocGenie** is a GenAI-powered platform designed to automatically generate high-quality documentation from raw technical specifications (e.g., `.txt`, `.md`, `.docx`). It leverages LLMs like GPT and open-source models to produce user guides, API references, configuration docs, and more — all through a secure, scalable backend.

---

## 🔧 Key Features

- 📄 Upload raw spec files (Markdown, Docx, etc.)
- 🧠 Use LLMs (local or cloud) to auto-generate:
  - User guides
  - API references
  - Tutorials & configuration docs
- 🗂️ Multi-tenant support (organizations and users)
- 🧩 RAG-enabled document Q&A
- 🐳 Dockerized with CI/CD, monitored via MLflow + Grafana
- ☁️ Kubernetes- and Terraform-ready for production

---

## 🏗️ Stack

- **Backend**: FastAPI + Python
- **AI Layer**: HuggingFace / OpenAI / Ollama
- **Preprocessing**: Pandas, Python-docx
- **Vector DB**: FAISS / ChromaDB
- **MLOps**: MLflow, Prometheus, Grafana
- **CI/CD**: GitHub Actions
- **Infra**: Docker, Kubernetes, Terraform

---

## 🛠️ Setup Instructions

```bash
git clone https://github.com/yourusername/autodocgenie.git
cd autodocgenie
pip install -r requirements.txt
uvicorn app.main:app --reload
