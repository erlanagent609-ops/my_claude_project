# Project Overview

This document provides an overview of the project structure and its components, including the multi-agent autonomous architecture.

- `src/`: Contains the main source code for the project.
- `tests/`: Contains unit tests and integration tests.
- `docs/`: Contains project documentation.
- `skills/`: Contains specialized agent guidelines and protocols.
- `scripts/`: Contains executable automation scripts.

## Multi-Agent Roles
1. **Translator Agent**: Responsible for translating English text/responses into clear Indonesian following workspace rules (`skills/translator_agent.md`).
2. **Debugger Agent**: Handles syntax errors, traceback analysis, and code repair across scripts.
3. **Supervisor Agent**: Oversees weekly upgrade protocols (`scripts/weekly_upgrade_protocol.py`) and repository synchronization (`scripts/git_sync.py`).

**Data Source:** Multi-agent architecture configuration and project workspace definitions.
