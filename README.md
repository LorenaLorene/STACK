# 🧮 FifthStackLanguage

A simple stack-based interpreter in Python that supports basic commands like  
`PUSH`, `POP`, `DUP`, `SWAP`, and arithmetic operations: `+`, `-`, `*`, `/`.

---

## 📦 Features

- Stack operations: `PUSH x`, `POP`, `DUP`, `SWAP`
- Arithmetic: `+`, `-`, `*`, `/` (integer division, using floor division)
- Graceful error handling for invalid or malformed commands

---

## ▶️ How to Run FifthStackLanguage

1. Open `main.py` and initialize the `FifthStackLanguage` class like this:

```python
from main import FifthStackLanguage

f = FifthStackLanguage()

print(f.execute("PUSH 5"))    
print(f.execute("PUSH 3")) 
print(f.execute("+"))
```

2.run the file
```commandline
python main.py
```

## ▶️ Run Tests

1. Install requirements.txt
```commandline
pip install -r requirements.txt
```
2. Run tests
```commandline
pytest tests/fifth_stack.py
```
