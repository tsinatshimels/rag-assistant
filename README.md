My RAG Assistant for Agentic AI Certification
A simple, locally-run RAG (Retrieval-Augmented Generation) assistant built with LangChain and Ollama. This project answers questions based on a provided text file about Python.
How It Works
This assistant uses a RAG pipeline to provide answers. The process is:
Load Documents: A text file (data/sample.txt) is loaded.
Split Text: The document is split into smaller, manageable chunks.
Create Embeddings: The text chunks are converted into numerical vectors using a local HuggingFace model (all-MiniLM-L6-v2).
Vector Store: These embeddings are stored in a ChromaDB vector store.
Retrieve & Generate: When a user asks a question, the system retrieves the most relevant text chunks from the vector store and passes them, along with the question, to a local Large Language Model (Ollama with llama3) to generate a final answer.
Setup and Installation
1. Clone the Repository:
code
Bash
git clone https://github.com/your-username/agentic-ai-rag-assistant.git
cd agentic-ai-rag-assistant
2. Install Ollama:
Download and install Ollama from the official website: https://ollama.com.
3. Download the Local LLM:
Run the following command in your terminal to download the llama3 model:
code
Bash
ollama run llama3
4. Set Up a Python Virtual Environment:
code
Bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
5. Install Dependencies:
code
Bash
pip install -r requirements.txt
How to Run the Assistant
With Ollama running in the background and your virtual environment active, run the main script:
code
Bash
python main.py
Sample Interaction
code
Code
RAG Assistant is ready! Ask your questions. Type 'quit' to exit.

You: what is python?
Assistant: Python is a high-level, interpreted programming language known for its readability and simplicity. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming.

You: what is python used for?
Assistant: Python is widely used in web development, data science, artificial intelligence, scientific computing, and automation.
