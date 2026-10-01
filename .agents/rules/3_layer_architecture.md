# Mandatory Rule: 3-Layer Architecture Execution

This rule governs all work conducted within this workspace. The assistant must operate strictly within the 3-layer architecture.

## The 3-Layer Architecture

1. **Layer 1: Directive (What to do)**
   - All standard operating procedures (SOPs), requirements, and guidelines reside in `directives/*.md`.
   - Before taking action, read or establish the relevant directive in `directives/`.

2. **Layer 2: Orchestration (Decision making & Intelligent Routing)**
   - The AI agent orchestrates the workflow, plans steps, handles edge cases, calls execution scripts, and updates directives with learnings (*self-annealing*).

3. **Layer 3: Execution (Doing the work deterministically)**
   - All deterministic tasks (file operations, API calls, data scraping, data analysis, PDF validation, catalog generation) must be written as modular, reusable Python scripts in `execution/`.
   - Never perform complex multi-step data manipulation or scraping manually if a deterministic script can execute it reliably.

## Operating Principles
- **Check tools first:** Before writing new code, check if an existing script in `execution/` already fulfills the task.
- **Self-anneal:** When a script or command fails, inspect the error, fix the script in `execution/`, test it, and update the directive in `directives/`.
- **File Organization:**
  - `directives/`: Living SOPs and instructions.
  - `execution/`: Deterministic Python tools.
  - `.tmp/`: Intermediate / temporary scratch files (never committed).
  - `.env`: Environment variables and secrets (never committed).
