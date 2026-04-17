# Context7 MCP Example

Exemple concret pour utiliser Context7 comme serveur MCP de documentation.
Concrete example for using Context7 as a documentation MCP server.

## 1) Why Context7 in This Repo

Use Context7 to fetch up-to-date documentation during coding tasks:
Utilisez Context7 pour recuperer de la documentation a jour pendant le developpement:

- PyTorch / Lightning API behavior
- uv command usage and dependency workflows
- CI-related syntax references
- troubleshooting references before applying fixes

## 2) Server Card (Filled Example)

```text
Server name: Context7
Business owner: ML platform / developer experience
Technical owner: Repo maintainers
Purpose: Retrieve authoritative documentation snippets during coding workflows
Data classification: internal
Allowed operations: read
Primary workflows: documentation lookup, API clarification, migration guidance
Authentication: none or token-based (depends on deployed server)
Rate limits / quotas: depends on provider plan
Failure fallback: use official docs URLs directly and continue with read-only exploration
Monitoring signals: MCP server availability, request latency, error rate
Rollback procedure: disable server from MCP client config and use direct web lookup
Last validation date: 2026-04-18
```

## 3) Client Configuration Template

The exact MCP configuration key varies by client.
La cle de configuration MCP exacte varie selon le client.

Use this generic pattern as a starting point:
Utilisez ce pattern generique comme point de depart:

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp"],
      "env": {}
    }
  }
}
```

Notes:

- Validate the package/command with the official Context7 documentation.
- Keep server access read-only in this repo by default.
- Add credentials only through secure secret storage.

## 4) Recommended Workflow

1. Start with a read-only question to Context7.
2. Cross-check key points with project conventions in the repo.
3. Apply minimal code/doc change.
4. Validate with project commands (`make lint`, `make test`).

## 5) Prompt Boilerplate (Copy/Paste)

```text
Use Context7 MCP to retrieve the latest official guidance for <topic>.
Then reconcile the result with this repository constraints:
- uv-based dependency management
- configs/default.yaml as config source of truth
- keep tests green via make test
Return:
1) short summary
2) exact recommendation
3) minimal patch plan
4) risks
```

## 6) Safety Checklist

- Do not execute write/admin actions through MCP for this server.
- Do not trust a single snippet without context validation.
- Prefer official docs for final tie-breakers.
- Record assumptions in PR description when guidance is ambiguous.
