# 🤖 Ollama Local Chatbot (DeepSeek-R1)

A lightweight **command-line chatbot** built using **Python and Ollama** that runs the **DeepSeek-R1:1.5B large language model locally**.

The chatbot maintains **conversation history**, allowing the model to generate **context-aware responses** during interaction.

This project demonstrates how to build a **simple local LLM chatbot using Ollama in Python**.

---

# 📌 Overview

Running **large language models locally** is becoming increasingly popular for:

- Privacy-focused AI applications
- Offline assistants
- Edge AI systems
- Research and experimentation

This project provides a **minimal implementation of a conversational chatbot** using the **Ollama Python API**.

The chatbot works **entirely offline after downloading the model**, with **no cloud API dependencies**.

---

# ✨ Features

- 🧠 **Local LLM inference** using Ollama  
- 💬 **Conversation memory** using message history  
- ⚡ **Simple and lightweight implementation**  
- 🖥️ **Command-line interface**  
- 🔒 **No external API keys required**

---

# 🛠️ Technologies Used

- Python
- Ollama
- DeepSeek-R1 1.5B Model

---

# 📦 Installation

## 1️⃣ Install Ollama

Download and install Ollama from:

https://ollama.com

Verify installation:

```
ollama --version
```

---

## 2️⃣ Download the Model

```
ollama pull deepseek-r1:1.5b
```

---

## 3️⃣ Install Python Dependency

```
pip install ollama
```

---

# 🚀 Usage

Run the chatbot script:

```
python chatbot.py
```

---

### Example Interaction

```
You: Hello
Bot: Hello! How can I assist you today?

You: Explain machine learning
Bot: Machine learning is a field of artificial intelligence that allows systems to learn from data...
```

Press **Enter without typing anything** to exit the chatbot.

---

# 📂 Project Structure

```
ollama-chatbot/
│
├── chatbot.py        # Chatbot implementation
└── README.md         # Project documentation
```

---

# 🧠 Implementation

The chatbot uses the **Ollama chat API** to communicate with the **DeepSeek model**.

Conversation messages are stored in a list to maintain **dialogue context**.

```python
import ollama

model_name = "deepseek-r1:1.5b"

messages = [
    {"role": "system", "content": "Hello,What can I do for you"}
]

while True:
    user = input("You:")

    if not user:
        break

    messages.append({"role": "user", "content": user})

    response = ollama.chat(
        model=model_name,
        messages=messages
    )

    answer = response["message"]["content"]

    print(f"Bot:{answer}")

    messages.append({"role": "assistant", "content": answer})
```

---

# 🔧 Possible Enhancements

Future improvements could include:

- Streaming responses for better UX
- Web interface using **Flask** or **FastAPI**
- Voice input and speech output
- Multi-model support
- Document-based **Retrieval-Augmented Generation (RAG)**

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

**Sinthanaiselvan G**

GitHub  
https://github.com/GS946GS

---

⭐ If you found this project useful, consider giving it a star.
