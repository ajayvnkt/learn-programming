# 🐍 Learn Programming: A Beginner's Journey into Python

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Poetry](https://img.shields.io/badge/poetry-1.5%2B-blueviolet)
![Status](https://img.shields.io/badge/status-active-success)

**A comprehensive, beginner-friendly Python learning program with hands-on examples, real-world projects, and test-driven learning**

[Getting Started](#-getting-started) • [Features](#-features) • [Curriculum](#-curriculum) • [Examples](#-examples) • [Contributing](#-contributing)

</div>

---

## 📖 About

**Learn Programming** is a carefully structured 10-day Python learning journey designed for absolute beginners. This repository provides:

- ✅ **Day-by-day curriculum** covering Python fundamentals
- ✅ **Hands-on examples** with clear explanations and expected outputs
- ✅ **Comprehensive projects** that tie all concepts together
- ✅ **Practice problems** with step-by-step guidance
- ✅ **Test suite** to verify your understanding
- ✅ **Modern tooling** with Poetry for dependency management

Whether you're a complete beginner or looking to refresh your Python fundamentals, this program will give you a solid foundation to build upon.

---

## ✨ Features

### 🎯 **Structured Learning Path**
- **10 focused days** of Python fundamentals
- Progressive difficulty from basics to functions
- Each day builds upon previous concepts

### 💻 **Hands-On Examples**
- Every concept demonstrated with working code
- Clear comments explaining what each line does
- Expected outputs shown for verification

### 🏗️ **Real-World Projects**
- **Student Grade Manager**: Complete system using all concepts
- **Library Book Management**: Another comprehensive example
- **Inventory Management**: Practice problem with guidance

### 🧪 **Test-Driven Learning**
- Test classes for each day's concepts
- Verify your understanding with automated tests
- Learn best practices from the start

### 🔧 **Modern Development Setup**
- Poetry for dependency management
- Consistent environment across all systems
- Latest Python best practices

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.9+** ([Download here](https://www.python.org/downloads/))
- **Poetry** ([Installation guide](https://python-poetry.org/docs/#installation))

> 💡 **Why Poetry?** Poetry ensures everyone has the same environment regardless of their operating system. No more "it works on my machine" issues!

> 📖 **For detailed setup instructions**, see [SETUP.md](SETUP.md)

### Quick Install

#### 1. **Install Poetry** (if not already installed)

**On macOS/Linux:**
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

**On Windows:**
```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

**Verify installation:**
```bash
poetry --version
```

#### 2. **Clone the Repository**
```bash
git clone https://github.com/ajayvnkt/learn-programming.git
cd learn-programming
```

#### 3. **Set Up Environment**

```bash
# Create virtual environment and install dependencies
poetry install

# Activate the environment
poetry shell
```

> 💡 **What's happening?** Poetry creates an isolated virtual environment and installs all necessary dependencies. This keeps your system Python clean!

#### 4. **Run the Program**

```bash
# Run all days (1-10) using Poetry (Recommended)
poetry run python -m src.learn_python

# Or without Poetry (if environment is activated)
python -m src.learn_python
```

---

## 📚 Curriculum

### Days 1-10: Python Fundamentals

| Day | Topic | Key Concepts |
|-----|-------|--------------|
| **Day 1** | Python Basics | Variables, Data Types, Print Statements |
| **Day 2** | Numbers & Math | Arithmetic Operations, Math Functions |
| **Day 3** | Strings | String Methods, Formatting, Slicing |
| **Day 4** | Lists | List Methods, Slicing, Comprehensions |
| **Day 5** | Tuples & Sets | Immutability, Set Operations |
| **Day 6** | Dictionaries | Key-Value Pairs, Dictionary Methods |
| **Day 7** | Conditionals | If/Elif/Else, Logical Operators |
| **Day 8** | For Loops | Iteration, Enumerate, Nested Loops |
| **Day 9** | While Loops | Conditional Loops, Break/Continue |
| **Day 10** | Functions | Function Definition, Parameters, Lambda |

---

## 💡 Examples

### Example 1: Day 1 - Variables and Data Types

```python
# Day 1: Variables and data types
name = "Python Learner"  # String
age = 25                 # Integer
height = 5.9            # Float
is_student = True       # Boolean

print(f"Hello, {name}!")
print(f"Age: {age}, Height: {height}, Student: {is_student}")
```

**Output:**
```
Hello, Python Learner!
Age: 25, Height: 5.9, Student: True
```

### Example 2: Day 6 - Dictionaries

```python
# Creating a dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Accessing values
print(person["name"])           # Alice
print(person.get("age", 0))     # 25

# Dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### Example 3: Comprehensive Project - Student Grade Manager

The program includes a complete Student Grade Management System that uses ALL concepts from Days 1-10:

```python
from src.learn_python.days_1_10 import comprehensive_problem_student_grade_manager

# Run the comprehensive problem
comprehensive_problem_student_grade_manager()
```

This demonstrates:
- ✅ Variables and data types
- ✅ Lists and dictionaries
- ✅ String methods
- ✅ Math operations
- ✅ Conditionals
- ✅ Loops (for and while)
- ✅ Functions
- ✅ Real-world problem solving

---

## 🧪 Running Tests

This project includes comprehensive tests to verify your understanding:

```bash
# Run all tests
poetry run pytest

# Run with coverage report
poetry run pytest --cov=src --cov-report=html

# Run specific test
poetry run pytest tests/test_day1.py -v
```

**Test Output:**
```
tests/test_day1.py::TestDay1::test_variables PASSED
tests/test_day2.py::TestDay2::test_math_operations PASSED
...
✅ All tests passed!
```

---

## 📁 Project Structure

```
learn-programming/
├── src/
│   └── learn_python/
│       ├── __init__.py          # Package initialization
│       ├── __main__.py          # Main entry point
│       └── days_1_10.py         # Main learning content
├── tests/
│   ├── __init__.py
│   ├── test_day1.py             # Day 1 tests
│   ├── test_day2.py             # Day 2 tests
│   └── ...                      # More test files
├── examples/                    # Additional examples
├── docs/                        # Documentation
├── pyproject.toml               # Poetry configuration
├── README.md                    # This file
├── SETUP.md                     # Setup instructions
└── .gitignore                   # Git ignore rules
```

---

## 🎓 Learning Tips

1. **Run Every Example**: Don't just read—execute every code snippet!
2. **Modify and Experiment**: Try changing values and see what happens
3. **Read the Comments**: Every example has detailed comments explaining concepts
4. **Complete the TODO Problem**: Test your knowledge with the Inventory Management problem
5. **Run the Tests**: Verify your understanding with the test suite

---

## 🔧 Development

### Code Quality

This project uses modern Python tooling:

- **Black**: Code formatting
- **Ruff**: Fast linting
- **MyPy**: Type checking
- **Pytest**: Testing framework

```bash
# Format code
poetry run black src tests

# Lint code
poetry run ruff check src tests

# Type check
poetry run mypy src
```

### Adding New Content

1. Add your code to `src/learn_python/days_1_10.py`
2. Write tests in `tests/`
3. Update documentation
4. Submit a pull request!

---

## 🤝 Contributing

Contributions are welcome! Whether it's:
- 📝 Fixing typos
- 💡 Adding examples
- 🐛 Reporting bugs
- 📚 Improving documentation
- ✨ Adding new features

Please feel free to open an issue or submit a pull request.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Ajay V N K T**

- GitHub: [@ajayvnkt](https://github.com/ajayvnkt)
- Repository: [learn-programming](https://github.com/ajayvnkt/learn-programming)

---

## 🙏 Acknowledgments

- Python Software Foundation for creating an amazing language
- The Python community for excellent documentation and resources
- All contributors who help make this project better

---

## 📈 What's Next?

After completing Days 1-10, you'll have a solid foundation in:

- ✅ Python basics and syntax
- ✅ Data structures (lists, dictionaries, sets, tuples)
- ✅ Control flow (conditionals, loops)
- ✅ Functions and code organization
- ✅ Problem-solving with Python

**Ready to continue?** Check out these next steps:

- 🐍 Object-Oriented Programming in Python
- 📊 Data Analysis with Pandas
- 🌐 Web Development with Flask/FastAPI
- 🤖 Machine Learning Basics
- 🧪 Testing and Debugging

---

<div align="center">

**⭐ Star this repo if you found it helpful! ⭐**

*Happy Learning! 🚀*

</div>

---

## 📝 Blog Post & Portfolio

This repository is designed to be:

- 📰 **Blog-ready**: Perfect content for Medium articles
- 💼 **Portfolio-worthy**: Showcases teaching and coding skills
- 🔗 **Shareable**: Easy to share on LinkedIn, Twitter, etc.
- 📚 **Educational**: Real learning value for beginners

**Suggested Blog Titles:**
- "Teaching Python to Beginners: A 10-Day Journey"
- "Building a Comprehensive Python Learning Program"
- "From Zero to Python Hero: A Structured Learning Path"
- "Creating Beginner-Friendly Programming Tutorials"

---

## 🎯 Why This Repository Stands Out

1. **Modern Tooling**: Uses Poetry for professional dependency management
2. **Test-Driven**: Includes comprehensive tests from day one
3. **Real Projects**: Not just examples—actual working systems
4. **Well-Documented**: Every concept explained clearly
5. **Beginner-Focused**: Assumes no prior programming knowledge
6. **Cross-Platform**: Works on Windows, macOS, and Linux

---

<div align="center">

**Made with ❤️ for Python learners everywhere**

[Report Bug](https://github.com/ajayvnkt/learn-programming/issues) • [Request Feature](https://github.com/ajayvnkt/learn-programming/issues) • [Contribute](https://github.com/ajayvnkt/learn-programming/pulls)

</div>

