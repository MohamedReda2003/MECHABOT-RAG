# 🤖 MechaBot RAG — Intelligent Q&A for ENSA Tétouan Mechatronics Club

<p align="center">
  <img src="https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white" alt="Ollama">
  <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" alt="LangChain">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/ChromaDB-FF6B6B?style=for-the-badge&logo=database&logoColor=white" alt="ChromaDB">
</p>

<p align="center">
  <b>A lightweight, privacy-first conversational AI assistant powered by local LLMs</b><br>
  <i>Answering questions about the Mechatronics Club at ENSA Tétouan — in French & English</i>
</p>

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🧠 **Local LLM Inference** | Runs entirely on-device using Ollama — no API keys, no data leaving your machine |
| 📚 **RAG Architecture** | Retrieval-Augmented Generation with ChromaDB vector store for accurate, context-aware responses |
| 🔤 **Bilingual Support** | Seamlessly handles both French and English queries |
| ⚡ **Fast Embeddings** | Uses `mxbai-embed-large` for high-quality semantic search |
| 🎯 **Precision-First** | Designed to only answer when confident — no hallucinations, no guesses |
| 🛠️ **Modular Design** | Clean separation between vector storage (`vector.py`) and chat logic (`main.py`) |

---

## 🏗️ Architecture

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  User Question  │────▶│  ChromaDB Vector │────▶│  Relevant Docs  │
│  (FR / EN)      │     │  Search (k=3)    │     │  Retrieved      │
└─────────────────┘     └──────────────────┘     └────────┬────────┘
                                                          │
┌─────────────────┐     ┌──────────────────┐              │
│  Final Answer   │◀────│  Llama 3.2 (Ollama)│◀─────────────┘
│  (Concise)      │     │  Response Gen    │
└─────────────────┘     └──────────────────┘
```

---

## 🚀 Quick Start

### Prerequisites

- [Ollama](https://ollama.com/download) installed on your system
- Python 3.8+

### 1. Clone & Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/mechabot-rag.git
cd mechabot-rag

# Install dependencies
pip install -r requirements.txt
```

### 2. Pull Required Models

```bash
# Pull the LLM for generation
ollama pull llama3.2

# Pull the embedding model
ollama pull mxbai-embed-large
```

### 3. Prepare Your Knowledge Base

Convert your Excel knowledge base to CSV format:

```bash
# Save your Excel file as: Base_Connaissances_RAG_Club_Mecatronique.csv
```

> 📁 The CSV should contain two columns: `Questions` and `Answers`

### 4. Run the Chatbot

```bash
python main.py
```

Type your questions and press **Enter**. Type `#` to exit.

---

## 📂 Project Structure

```
mechabot-rag/
├── 📄 main.py                                    # Main chat interface & LLM orchestration
├── 📄 vector.py                                  # Vector store setup & document embedding
├── 📄 requirements.txt                           # Python dependencies
├── 📄 Base_Connaissances_RAG_Club_Mecatronique.xlsx   # Knowledge base (source)
└── 📄 Base_Connaissances_RAG_Club_Mecatronique.csv    # Knowledge base (processed)
```

---

## 🛠️ Tech Stack

<div align="center">

| Technology | Purpose |
|------------|---------|
| [Ollama](https://ollama.com) | Local LLM inference (Llama 3.2) |
| [LangChain](https://langchain.com) | LLM orchestration & chaining |
| [ChromaDB](https://chromadb.dev) | Vector database for semantic search |
| [LangChain-Ollama](https://python.langchain.com/docs/integrations/chat/ollama/) | Ollama integration for LangChain |
| [mxbai-embed-large](https://ollama.com/library/mxbai-embed-large) | State-of-the-art embeddings |
| [Pandas](https://pandas.pydata.org) | Data processing |

</div>

---

## 💡 Example Usage

```
------------------------------------------
Donnez votre question: Quand le club a-t-il été fondé ?


2009

------------------------------------------
Donnez votre question: What programming languages are taught?


C/C++ and Python

------------------------------------------
Donnez votre question: #
```

---

## 🎯 Design Philosophy

> **"Absolute Mode"** — This assistant follows a strict cognitive-directive approach:
> 
> - ✅ Direct, information-dense responses
> - ✅ No emojis, no fluff, no engagement bait
> - ✅ Ends immediately after delivering information
> - ✅ Prioritizes accuracy over friendliness
> - ✅ Builds user self-sufficiency

---

## 🔧 Customization

### Change the LLM Model

Edit `main.py`:
```python
model = OllamaLLM(model="your-preferred-model")
```

### Adjust Retrieved Documents

Edit `vector.py`:
```python
retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}  # Retrieve more context
)
```

### Modify System Prompt

Edit the `template` in `main.py` to customize the assistant's behavior.

---

## 📊 Knowledge Base Coverage

The chatbot can answer questions about:

- 🏛️ **ENSA Tétouan** — History, programs, structure
- 🤖 **Mechatronics Club** — Mission, values, organization
- 🎓 **Formations** — Arduino, CATIA, SolidWorks, PCB design, Python
- 🏆 **Competitions** — CNR (Coupe Nationale de Robotique), international events
- 📅 **Events** — Let's Mechatronics, National Mechatronics Day
- 📞 **Contact** — Social media, emails, phone numbers

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

- 🐛 Report bugs
- 💡 Suggest features
- 🔀 Submit pull requests

---


## 🙏 Acknowledgments

- **ENSA Tétouan** — For fostering innovation and technical excellence
- **Mechatronics Club** — For the comprehensive knowledge base
- **Ollama Team** — For making local LLMs accessible
- **LangChain Community** — For the powerful orchestration framework

---

<p align="center">
  <b>Made with ❤️ by the Mechatronics Club at ENSA Tétouan</b><br>
  <i>Promoting innovation, creativity, and technical excellence since 2009</i>
</p>

<p align="center">
  <a href="mailto:clubmecatroniqueensate@gmail.com">📧 Email</a> •
  <a href="https://www.linkedin.com/company/club-m%C3%A9catronique-ensat%C3%A9/">💼 LinkedIn</a> •
  <a href="https://www.instagram.com/clubmecatronique_ensate/">📸 Instagram</a>
</p>
