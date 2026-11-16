# Skill Creator Protocol

This document defines the self-learning protocol for worker agents in this project.

## Rules for New Tasks and Skills

1. **Check Existing Skills**:
   Every time the user gives a new task that requires specialized expertise (such as a new API integration, specific data analysis, or unique automation), the agent must first inspect the `skills/` folder to check if a relevant skill guideline already exists.

2. **Create New Skill / Script**:
   If the required skill does not exist, the agent is obligated to design and write a new skill guide or script file inside the appropriate `skills/` or `scripts/` directory.

3. **Test and Document**:
   The agent must test the newly created skill or script using appropriate test or run commands to ensure it functions correctly. Finally, the agent must document the new skill in the `README.md` so it can be reliably reused in future tasks.
