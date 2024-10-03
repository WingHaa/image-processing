VENV_DIR = venv
REQUIREMENTS_FILE = requirements.txt

.PHONY: venv
venv:
	python3 -m venv $(VENV_DIR)

.PHONY: dev
dev:
	source venv/bin/activate

.PHONY: install
install: venv
	@$(VENV_DIR)/bin/pip install -r $(REQUIREMENTS_FILE)

.PHONY: setup
setup: install

.PHONY: clean
clean:
	rm -rf $(VENV_DIR)

.PHONY: help
help:
	@echo "Makefile commands:"
	@echo "  make setup  - Create venv and install dependencies"
	@echo "  make dev    - Instructions to activate the virtual environment"
	@echo "  make clean  - Remove the virtual environment"
	@echo "  make help   - Show this help message"
