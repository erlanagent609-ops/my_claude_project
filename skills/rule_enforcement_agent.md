# Rule Enforcement Agent

This skill defines the mandatory pre-execution protocol for all assistant interactions. Before generating any response, the agent must review and adhere to all established workspace rules, including:
1. Universal translation of all responses into Indonesian using the translator skill.
2. Direct Indonesian responses without intermediate English echoing.
3. Strict source attribution for all facts, data, time, or location.
4. Mandatory separation of unrelated creative or optional skills into specialized optional directories.
5. **Strict Skill Categorization and Separation**: For any new skill created, separate them based on their criteria; never combine them if they have different criteria and topic concepts.
6. **Immediate Progress Journaling**: Every progress, milestone, or completed task must be recorded immediately by the progress journaling agent.
7. **Automatic Agent Execution**: All relevant agents and skills must be triggered and execute automatically at the start of every conversation to ensure seamless capability integration.
