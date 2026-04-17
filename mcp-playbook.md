# MCP Playbook

Guide pratique pour exploiter des serveurs MCP dans ce projet.
Practical guide to operate MCP servers in this project.

## 1) Why MCP Here / Pourquoi MCP ici

MCP is useful when your coding workflow needs controlled access to external systems such as:
MCP est utile quand votre workflow de dev a besoin d un acces controle a des systemes externes comme:

- issue trackers
- artifact stores
- model registries
- data catalogs
- internal APIs

Goal:
Objectif:

- keep agent workflows deterministic and auditable
- avoid ad hoc scripts and manual copy paste
- centralize integration contracts per server

## 2) Recommended Server Categories / Categories recommandees

- Planning and tracking: tickets, issues, milestones
- Data operations: dataset metadata, schema checks, lineage
- Experiment operations: run metadata, model registry, artifact lookup
- Platform operations: logs, deployment status, incidents

Start small:
Commencez petit:

1. one MCP server per high-value workflow,
2. read-only first,
3. then progressive write access with approval gates.

## 3) Security and Governance Baseline / Securite et gouvernance

- principle of least privilege for every MCP server
- separate read and write capabilities when possible
- no secrets in prompts, docs, or source files
- centralize credentials in secure secret stores only
- keep an allowlist of approved servers and operations
- log who triggered what through which MCP tool

## 4) Server Onboarding Checklist / Checklist onboarding serveur

Use this checklist before enabling a new MCP server:
Utilisez cette checklist avant d activer un nouveau serveur MCP:

- Business purpose is explicit and scoped.
- Owner team and escalation path are defined.
- Data sensitivity is classified.
- Allowed operations are documented (read/write/delete).
- Required auth method is documented.
- Failure modes and fallback workflow are documented.
- Test scenario exists (happy path + failure path).
- Rollback/disable procedure exists.

## 5) Boilerplate: Server Card Template / Template fiche serveur

Copy this block for each MCP server:
Copiez ce bloc pour chaque serveur MCP:

```text
Server name:
Business owner:
Technical owner:
Purpose:
Data classification: public | internal | restricted
Allowed operations: read | write | admin
Primary workflows:
Authentication:
Rate limits / quotas:
Failure fallback:
Monitoring signals:
Rollback procedure:
Last validation date:
```

## 6) Boilerplate: Agent Prompt Pattern / Pattern de prompt agent

Use this pattern when asking an agent to use MCP tools:
Utilisez ce pattern quand vous demandez a un agent d utiliser des outils MCP:

```text
Context:
- Goal:
- Environment:
- Constraints:

MCP scope:
- Allowed server(s):
- Allowed operations:
- Forbidden operations:

Execution plan:
1) Read-only discovery
2) Validate assumptions
3) Apply minimal change if needed
4) Return structured report

Output expected:
- Summary
- Actions performed
- Evidence
- Risks
- Next steps
```

## 7) Boilerplate: Incident Triage Workflow / Workflow triage incident

```text
1. Detect: capture symptom and timestamp.
2. Scope: identify affected services, datasets, users.
3. Contain: switch to read-only fallback if needed.
4. Diagnose: query MCP telemetry and recent changes.
5. Recover: apply minimal corrective action.
6. Verify: confirm service health and data integrity.
7. Document: root cause, impact, and prevention actions.
```

## 8) Integration Tips for This Repo / Conseils integration pour ce repo

- Keep MCP-related docs in this file and in cookbook references.
- Reuse existing specialized agents for triage and documentation.
- If MCP introduces mandatory checks, reflect them in CI and Makefile commands.
- Keep examples bilingual and operational, not theoretical.

## 9) Suggested Next Steps / Prochaines etapes suggerees

1. Add one concrete server card for your first MCP integration.
2. Add a dedicated MCP triage agent if incident volume grows.
3. Add a CI validation step for MCP configuration format if needed.

## 10) Concrete Example: Context7 / Exemple concret: Context7

- See practical server card and boilerplate: `mcp-examples/context7.md`
- Voir la fiche serveur et le boilerplate pratique: `mcp-examples/context7.md`
