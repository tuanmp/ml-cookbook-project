# ML Cookbook Guide

This file is the practical guide for using the current project layout.
It is aligned with the code that exists today (uv + PyTorch Lightning).

Ce document est le guide pratique du projet.
Il est aligne sur l implementation actuelle (uv + PyTorch Lightning).

## 1) Start Here / Demarrage (2 minutes)

From the project root:

Depuis la racine du projet:

```bash
uv sync --group dev
uv run python train.py --config configs/default.yaml
uv run pytest
```

What this gives you:

Ce que vous obtenez:

- working training pipeline with dummy data / pipeline d entrainement operationnel avec donnees factices
- reproducible setup via a YAML config / setup reproductible via config YAML
- smoke tests for shape and training loop safety / tests smoke pour securiser shapes et boucle train

## 2) Current Project Structure

```text
ml-cookbook-project/
├── cookbook.md
├── README.md
├── Makefile
├── pyproject.toml
├── uv.lock
├── train.py
├── configs/
│   └── default.yaml
├── src/
│   └── ml_cookbook/
│       ├── __init__.py
│       ├── train.py
│       ├── data/
│       │   ├── __init__.py
│       │   └── dummy_datamodule.py
│       ├── models/
│       │   ├── __init__.py
│       │   └── prototype_model.py
│       └── utils/
│           ├── __init__.py
│           └── repro.py
└── tests/
    ├── test_shapes.py
    └── test_train_smoke.py
```

Generated at runtime (not core source code):

- `.venv/`
- `logs/`
- `.pytest_cache/`

## 3) File-by-File Quick Map / Carte Rapide des Fichiers

- `pyproject.toml`: project metadata and dependencies managed by uv.
- `uv.lock`: locked dependency graph for reproducible installs.
- `configs/default.yaml`: experiment config (data, model, trainer, seed).
- `train.py`: root entrypoint that calls package training logic.
- `src/ml_cookbook/train.py`: main Lightning training orchestration.
- `src/ml_cookbook/data/dummy_datamodule.py`: random data module for fast prototyping.
- `src/ml_cookbook/models/prototype_model.py`: baseline Lightning classifier model.
- `src/ml_cookbook/utils/repro.py`: seed and deterministic behavior setup.
- `tests/test_shapes.py`: shape sanity checks.
- `tests/test_train_smoke.py`: 1-epoch smoke train test.
- `Makefile`: simple shortcuts for sync/train/test/lint.

## 4) Daily Workflow / Workflow Quotidien

### Step A: Sync dependencies / Synchroniser les dependances

```bash
make sync
```

### Step B: Run tests before changes / Lancer les tests avant modifs

```bash
make test
```

### Step C: Edit what you need / Modifier ce dont vous avez besoin

Common edits:

- change input shape or class count in `configs/default.yaml`
- evolve model architecture in `src/ml_cookbook/models/prototype_model.py`
- swap dummy data with real data module under `src/ml_cookbook/data/`

### Step D: Train and validate / Entrainer et valider

```bash
make train
```

## 5) How to Move from Dummy Data to Real Data / Passer du dummy au reel

1. Create a new data module file in `src/ml_cookbook/data/`.
2. Keep the same output contract: `(x, y)` where:
   - `x` shape is `[batch, channels, height, width]` for the current model
   - `y` is class indices (dtype long)
3. Update instantiation logic in `src/ml_cookbook/train.py`.
4. Adjust `configs/default.yaml` to your dataset settings.
5. Run `make test` then `make train`.

## 6) Troubleshooting / Depannage

- Import errors in editor:
  - ensure workspace interpreter is `.venv/bin/python`
  - run `make sync`
- Slow dataloading warnings:
  - increase `num_workers` in `configs/default.yaml`
- Non-deterministic behavior:
  - keep `seed` fixed and `trainer.deterministic: true` in config

## 7) Copilot Agent Index / Index des Agents Copilot

All workspace agents are in `.github/agents/`.
Tous les agents du workspace sont dans `.github/agents/`.

- `Code Review`
  - Use when: reviewing PRs, finding regressions, missing tests, architecture risks.
  - Utiliser quand: revue de PR, detection regressions, trous de tests, risques architecture.
- `Docs Writer`
  - Use when: updating README/cookbook/setup docs in FR + EN.
  - Utiliser quand: mise a jour docs README/cookbook/setup en FR + EN.
- `Test Triage`
  - Use when: test or CI failures need fast root-cause and minimal fix.
  - Utiliser quand: echec tests/CI, besoin diagnostic rapide et correctif minimal.
- `Experiment Setup`
  - Use when: creating or adjusting experiment configs and trainer/model/data parameters.
  - Utiliser quand: creation ou ajustement configs experiment et parametres trainer/model/data.
- `Dependency Upgrade Planner`
  - Use when: planning package upgrades, refreshing `uv.lock`, and reducing upgrade risk.
  - Utiliser quand: planifier upgrades dependances, refresh `uv.lock`, reduire le risque.
- `Performance Profiler`
  - Use when: profiling slow runs and proposing measured optimizations.
  - Utiliser quand: profiler lenteurs et proposer optimisations mesurees.

## 8) MCP Suggestions and Boilerplate / Suggestions et boilerplate MCP

- See detailed MCP playbook: `mcp-playbook.md`
- Voir le playbook MCP detaille: `mcp-playbook.md`

Recommended usage order:
Ordre d usage recommande:

1. Define one high-value MCP workflow first.
1. Define server scope, allowed operations, and fallback path.
1. Start with read-only operations before enabling writes.
1. Add observability and rollback notes to the server card.

For day-to-day operations, reuse:
Pour les operations quotidiennes, reutiliser:

- `Test Triage` for incident diagnosis
- `Docs Writer` for keeping MCP docs up to date
- `Code Review` for risk checks before enabling write operations

## 9) Context7 + Agents Prompts / Prompts Context7 + Agents

Use these ready-to-copy prompts in Copilot Chat.
Utilisez ces prompts prets a copier dans Copilot Chat.

### Prompt A: Lightning API Review with Context7 + Code Review

```text
Use Context7 MCP to retrieve the latest official guidance for Lightning callbacks and Trainer options.
Then run a code review focused on regressions and reproducibility for these files:
- src/ml_cookbook/train.py
- configs/default.yaml

Return:
1) key doc updates from Context7
2) concrete risks in current code/config
3) minimal patch plan
4) validation commands
```

### Prompt B: uv Workflow Update with Context7 + Dependency Upgrade Planner

```text
Use Context7 MCP to fetch the latest recommended uv workflow for project sync, lock refresh, and CI usage.
Then propose minimal updates for this repository without changing architecture.

Constraints:
- keep pyproject.toml + uv.lock as source of truth
- keep make sync / make test / make lint commands

Return:
1) proposed dependency workflow changes
2) exact files to edit
3) rollback strategy
4) commands to validate
```

### Prompt C: CI Troubleshooting with Context7 + Test Triage

```text
Use Context7 MCP to retrieve current guidance for GitHub Actions + Python + uv setup.
Then triage a failing CI run for lint/test with minimal safe fixes.

Input:
- failing job logs
- affected workflow file: .github/workflows/ci.yml

Return:
1) probable root cause
2) minimal fix patch
3) re-run plan
4) residual risks
```

Tip:
Astuce:

- Start with read-only discovery through Context7, then apply minimal edits.
- Commencez par une phase read-only via Context7, puis appliquez des edits minimaux.

## 10) Next Improvement Targets / Prochaines Ameliorations

- add dedicated real dataset modules (image, text, tabular recipes)
- add CI workflow for test/lint on pull requests
- add richer metrics and experiment tracking if needed
