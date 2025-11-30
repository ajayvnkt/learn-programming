# 🚀 Setup Guide

## Quick Start with Poetry

### 1. Install Poetry (if not already installed)

**macOS/Linux:**
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

**Windows:**
```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

**Verify installation:**
```bash
poetry --version
```

### 2. Install Dependencies

```bash
cd learn-programming
poetry install
```

This will:
- Create a virtual environment
- Install all dependencies (including pytest for testing)
- Set up the project for development

### 3. Activate the Environment

```bash
poetry shell
```

### 4. Run the Program

```bash
# Option 1: Using Python module (Recommended)
poetry run python -m src.learn_python

# Option 2: Using the module directly
poetry run python -m src.learn_python.days_1_10

# Option 3: Direct import
poetry run python -c "from src.learn_python.days_1_10 import run_days_1_10; run_days_1_10()"
```

### 5. Run Tests

```bash
# Run all tests
poetry run pytest

# Run with verbose output
poetry run pytest -v

# Run with coverage
poetry run pytest --cov=src --cov-report=html
```

## Without Poetry (Alternative Setup)

If you prefer not to use Poetry:

### 1. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install pytest pytest-cov
```

### 3. Run the Program

```bash
# Using Python module (Recommended)
python -m src.learn_python

# Or using the module directly
python -m src.learn_python.days_1_10
```

### 4. Run Tests

```bash
pytest tests/ -v
```

## Verification Checklist

- [ ] Poetry installed (`poetry --version`)
- [ ] Dependencies installed (`poetry install`)
- [ ] Environment activated (`poetry shell`)
- [ ] Code runs (`poetry run python -m src.learn_python`)
- [ ] Tests pass (`poetry run pytest`)
- [ ] All imports work correctly

## Troubleshooting

### Issue: "poetry: command not found"
**Solution:** Add Poetry to your PATH. After installation, add:
```bash
export PATH="$HOME/.local/bin:$PATH"
```
to your `~/.bashrc` or `~/.zshrc`, then reload: `source ~/.zshrc`

### Issue: "No module named pytest"
**Solution:** Make sure you've run `poetry install` to install dev dependencies

### Issue: Import errors
**Solution:** Ensure you're running from the project root directory and using `poetry run` or have activated the virtual environment

