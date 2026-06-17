# Fraction

> A lightweight Python library that implements rational numbers from scratch using Python's magic methods and operator overloading.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 📖 Overview

`Fraction` is a pure Python implementation of rational numbers designed to demonstrate Python's object-oriented programming model, operator overloading, and special (magic) methods.

Unlike Python's built-in `fractions.Fraction`, this project was built from scratch for educational purposes to understand how Python's data model works internally.

---

## ✨ Features

* ✅ Automatic fraction simplification
* ✅ Denominator validation
* ✅ Arithmetic operator overloading
* ✅ Comparison operators
* ✅ Reverse arithmetic operators
* ✅ Integer and float conversion
* ✅ Canonical representation of fractions
* ✅ Clean and Pythonic API

---

## 📦 Installation

Install using pip:

```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ fraction-raj
```

or install from source:

```bash
git clone https://github.com/RajeshPhulwaria06/fraction-package.git

cd fraction-pacakge

pip install .
```

---

## 🚀 Quick Start

```python
from fraction import Fraction

a = Fraction(1, 2)
b = Fraction(3, 4)

print(a)
print(b)

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

Output

```
1/2
3/4
5/4
-1/4
3/8
2/3
```

---

# Arithmetic Operations

```python
from fraction import Fraction

a = Fraction(2,3)
b = Fraction(5,6)

print(a+b)
print(a-b)
print(a*b)
print(a/b)
```

---

# Comparison Operations

```python
from fraction import Fraction

a = Fraction(1,2)
b = Fraction(2,4)
c = Fraction(3,4)

print(a == b)
print(a < c)
print(c > a)
print(a <= b)
print(c >= b)
```

Output

```
True
True
True
True
True
```

---

# Mixed Integer Operations

```python
from fraction import Fraction

a = Fraction(3,4)

print(a + 2)
print(2 + a)

print(a * 3)
print(3 * a)

print(2 - a)
print(2 / a)
```

---

# Automatic Simplification

```python
Fraction(4,8)
```

Output

```
1/2
```

---

# Negative Denominator Handling

```python
Fraction(3,-6)
```

Output

```
-1/2
```

---

# Type Conversion

## Integer

```python
a = Fraction(7,2)

print(int(a))
```

Output

```
3
```

---

## Float

```python
a = Fraction(1,8)

print(float(a))
```

Output

```
0.125
```

---

# Error Handling

Division by zero denominator

```python
Fraction(5,0)
```

Raises

```
ZeroDivisionError:
Denominator cannot be zero.
```

---

# API

## Constructor

```python
Fraction(numerator, denominator)
```

---

## Supported Operators

| Operation | Supported |
| --------- | --------- |
| +         | ✅         |
| -         | ✅         |
| *         | ✅         |
| /         | ✅         |
| ==        | ✅         |
| <         | ✅         |
| >         | ✅         |
| <=        | ✅         |
| >=        | ✅         |
| int()     | ✅         |
| float()   | ✅         |

---

# Project Structure

```
fraction-raj/
│
├── src/
│   └── fraction/
│       ├── __init__.py
│       └── fraction.py
│
├── tests/
│   └── test_fraction.py
│
├── examples.py
├── pyproject.toml
├── README.md
├── LICENSE
└── .gitignore
```

---

# Motivation

This project was built to gain a deeper understanding of:

* Object-Oriented Programming
* Python Data Model
* Special (Magic) Methods
* Operator Overloading
* Package Development
* Python Packaging (PyPI)
* Writing reusable Python libraries

Instead of relying on Python's built-in `fractions` module, every core feature was implemented manually as a learning exercise.

---

# Future Improvements

* [ ] Hash support (`__hash__`)
* [ ] Boolean conversion (`__bool__`)
* [ ] Unary operators (`__neg__`, `__abs__`)
* [ ] Decimal interoperability
* [ ] Rich documentation
* [ ] 100% unit test coverage
* [ ] GitHub Actions CI/CD
* [ ] Benchmark against Python's `fractions.Fraction`

---

# Contributing

Contributions, feature requests, and bug reports are welcome.

1. Fork the repository
2. Create a feature branch

```
git checkout -b feature/new-feature
```

3. Commit your changes

```
git commit -m "Add new feature"
```

4. Push the branch

```
git push origin feature/new-feature
```

5. Open a Pull Request

---

# Running Tests

Install pytest

```bash
pip install pytest
```

Run

```bash
pytest
```

---

# Author

**Rajesh Phulwaria**

Research-oriented Software Engineer passionate about Python, AI, backend systems, and building developer tools from scratch.

GitHub:
https://github.com/RajeshPhulwaria006/

LinkedIn:
https://linkedin.com/in/rajesh-phulwaria-b61093315/

---

# License

This project is licensed under the MIT License.

---

⭐ If you found this project helpful, consider starring the repository to support future development.
