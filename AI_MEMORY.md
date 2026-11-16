# AI Memory & Workspace Context

This document serves as the persistent memory for the autonomous agent workspace. At the start of every session, the AI must read this file first to maintain full context of the project architecture, scripts, skills, and progress.

## 1. Project Overview & Environment
- **Environment**: Ubuntu, directory `~/my_agent_home`.
- **Core Architecture**: Autonomous multi-agent workspace utilizing Python and Git.
- **Security**: Sensitive credentials (`config/git_credentials.json`) are secured via `.gitignore` to prevent secret scanning blocks. Git database is maintained and cleaned regularly.

## 2. Folder Structure
- `src/`: Main source code.
- `scripts/`: Executable automation scripts.
- `tests/`: Unit and integration tests.
- `docs/`: Project documentation and guides.
- `skills/`: Specialized agent guidelines and protocols.

## 3. Available Scripts
- `scripts/git_pusher_agent.py`: Autonomous Python agent for checking git status, committing changes with timestamps, pushing to GitHub (`origin main`), and sending Telegram/local activity notifications.
- `scripts/weather_fetcher.py`: Real-time weather fetcher using the public Open-Meteo API (supports location queries like Manado or Berlin).
- `scripts/text_analyzer.py`: Text processing utility for word count, sentence count, and word frequencies.
- `scripts/translator_wrapper.py`: Translation utility following agent translation guidelines.
- `scripts/create_zip.py`: Archives the entire workspace.
- `scripts/git_sync.py`: Handles repository synchronization.
- `scripts/weekly_upgrade_protocol.py`: Executes weekly upgrade protocols.

## 4. Skills & Guidelines
- `skills/data_parser.md`: CSV data processing and cleaning guidelines.
- `skills/text_analyzer.md`: Text analysis rules and steps.
- `skills/translator_agent.md`: Translation guidelines for English to Indonesian.
- `skills/executor_agent.md`: Autonomous executor agent guidelines.
- `skills/general_assistant.md`: General assistant protocols.
- `skills/skill_creator_protocol.md`: Protocol for creating new skills.

## 5. Operational Rules
- **Context Retention**: Whenever a new session starts, the AI must read `AI_MEMORY.md` first before performing tasks.
- **Autonomous Execution**: Act as an Autonomous Executor Agent, leveraging existing scripts whenever possible rather than asking users for manual terminal commands unnecessarily.
