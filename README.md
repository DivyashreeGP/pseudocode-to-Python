# 🔍 Pseudocode to Python Translator (Using SDT)

This project is a **web-based tool** that takes algorithms written in simple **English-like pseudocode** and converts them into **Python code** using **Syntax Directed Translation (SDT)** techniques. It is designed to bridge the gap between natural language logic and programming, especially for beginners.

---

## 💡 Key Features

* ✅ **Natural Language Input:** Accepts step-by-step pseudocode in English.
* 🐍 **Python Code Generation:** Outputs clean, executable Python code.
* 🌐 **Web Interface:** Built using Flask, allowing real-time translation through a browser.
* 🧠 **SDT-Based Logic:** Core translation engine is based on SDT principles — associating grammar rules with Python code templates.

---

## 🔧 How It Works

1. The user inputs an algorithm in plain English (e.g., "Set x to 10", "While x is greater than 0 do...").
2. The input is split into individual lines.
3. Each line is parsed and matched to grammar rules.
4. Using SDT rules, each recognized pattern is converted into its Python equivalent.
5. The final translated code is displayed to the user.

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS (with dark mode UI)
* **Backend:** Python, Flask
* **Translation Engine:** Custom SDT-based parser implemented in Python

---

## ⚡ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/pseudocode-to-python.git
cd pseudocode-to-python
```

### 2. Set Up Virtual Environment (Optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
python app.py
```

Open your browser and go to `http://127.0.0.1:8084/`

---

## 📊 Example

**Input:**

```
Set x to 5
While x is greater than 0 do
    Print x
    Set x to x - 1
```

**Output (Python):**

```python
x = 5
while x > 0:
    print(x)
    x = x - 1
```

---

## 🎓 Learning Goal

This project demonstrates how **Syntax Directed Translation (SDT)** can be used to interpret structured English instructions and generate actual code. It's ideal for teaching how compilers or interpreters work in simplified scenarios.

--
