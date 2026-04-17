UV := uv

.PHONY: sync train test lint format

sync:
	$(UV) sync --group dev

train:
	$(UV) run python train.py --config configs/default.yaml

test:
	$(UV) run pytest

lint:
	$(UV) run python -m compileall src tests

format:
	@echo "No formatter configured yet"
