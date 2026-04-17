# ML Cookbook Project

[![CI](https://github.com/<OWNER>/<REPO>/actions/workflows/ci.yml/badge.svg)](https://github.com/<OWNER>/<REPO>/actions/workflows/ci.yml)

Replace `<OWNER>/<REPO>` with your GitHub repository path.
Remplacez `<OWNER>/<REPO>` par le chemin de votre depot GitHub.

Template de prototypage ML avec PyTorch + Lightning, base sur `uv`.
ML prototyping template with PyTorch + Lightning, powered by `uv`.

## Objectif / Goal

Ce projet sert de socle pour:
This project is a starter kit to:

1. valider rapidement une boucle d entrainement avec donnees factices,
1. quickly validate a training loop with dummy data,
1. iterer sur l architecture du modele,
1. iterate on model architecture,
1. basculer vers des donnees reelles sans casser la plomberie.
1. switch to real data without breaking the training plumbing.

## Quick Start

```bash
make sync
make test
make train
```

Equivalent sans Makefile:
Equivalent without Makefile:

```bash
uv sync --group dev
uv run pytest
uv run python train.py --config configs/default.yaml
```

## Structure Essentielle / Core Structure

```text
.
├── pyproject.toml
├── uv.lock
├── train.py
├── configs/default.yaml
├── src/ml_cookbook/
│   ├── train.py
│   ├── data/dummy_datamodule.py
│   ├── models/prototype_model.py
│   └── utils/repro.py
└── tests/
    ├── test_shapes.py
    └── test_train_smoke.py
```

## Documentation

- Guide utilisateur complet: `cookbook.md`
- User guide: `cookbook.md`
- Config experiment: `configs/default.yaml`
- Experiment config: `configs/default.yaml`
- MCP guide and boilerplate: `mcp-playbook.md`
- Guide MCP et boilerplate: `mcp-playbook.md`
- MCP Context7 example: `mcp-examples/context7.md`
- Exemple MCP Context7: `mcp-examples/context7.md`

## Copilot Behavior / Comportement Copilot

- Repository instructions file: `.github/copilot-instructions.md`
- Fichier d instructions du repository: `.github/copilot-instructions.md`
- Keep this file updated when project workflow, quality gates, or conventions change.
- Mettez ce fichier a jour lorsque le workflow, les controles qualite, ou les conventions changent.

## Copilot Agents / Agents Copilot

- Agent files folder: `.github/agents/`
- Dossier des agents: `.github/agents/`
- `Code Review`: PR review, bug/regression and risk analysis.
- `Docs Writer`: README/cookbook updates in French + English.
- `Test Triage`: diagnose failing tests and CI failures quickly.
- `Experiment Setup`: prepare reproducible experiment configs.
- `Dependency Upgrade Planner`: safe dependency upgrades with `uv`.
- `Performance Profiler`: bottleneck analysis and measurable speedups.

## Commandes Utiles / Useful Commands

- `make sync`: installe et verrouille l environnement via uv
- `make sync`: install and lock the environment via uv
- `make test`: lance la suite de tests
- `make test`: run the test suite
- `make train`: execute un entrainement complet avec la config par defaut
- `make train`: run full training with the default config
- `make lint`: verification syntaxique rapide
- `make lint`: quick syntax check
