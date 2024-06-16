.PHONY: setup install lint format docs clean

# Setup Python environment
setup:
    pyenv install 3.9.5 -s
    pyenv virtualenv 3.9.5 myenv
    pyenv local myenv

# Install dependencies
install: setup
    pyenv activate myenv && pip install -r requirements.txt

# Lint code
lint:
    pyenv activate myenv && ruff . && black --check .

# Format code
format:
    pyenv activate myenv && black .

# Build documentation
docs:
    pyenv activate myenv && sphinx-build -b html docs/ docs/_build/html

# Clean up
clean:
    rm -rf venv
    rm -rf docs/_build

