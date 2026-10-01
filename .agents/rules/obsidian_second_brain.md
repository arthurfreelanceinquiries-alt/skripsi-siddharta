# Rule: Obsidian Second Brain & Session Synchronization Protocol

This workspace is integrated with Obsidian as a **Second Brain** for thesis research (skripsi). The assistant MUST adhere to the following protocol on every session and during work execution:

## 1. Session Start (Pre-Flight Hook)
Whenever the user starts a session, says "mulai sesi", "jalankan skill second brain", or begins work:
1. **Multi-Device Git Sync (Pre-Flight Pull):**
   - Run `git pull origin main` to ensure the local repository is 100% synchronized with the latest commits pushed from other devices/laptops before beginning any work.
2. **Inspect Graphify Knowledge:**
   - Check `graphify-out/` (`manifest.json` / `GRAPH_REPORT.md`) to maintain persistent awareness of codebase dependencies, entity communities, and file relationships.
3. **Inspect Second Brain Dashboard:**
   - Read `00_DASHBOARD_SECOND_BRAIN.md` to load active research status, research constructs, recent supervisor feedback, and open tasks.
4. **Session Alignment:**
   - Acknowledge the current research context, report Git sync status, and state readiness to execute.

## 2. In-Flight Documentation (Purpose-Driven Notes)
Whenever creating or editing markdown notes in this vault:
1. **Mandatory Top Summary:**
   Every documentation, concept note, PRD, or bimbingan record must start with an Obsidian callout:
   ```markdown
   > [!SUMMARY] Tujuan & Solusi Catatan Ini
   > - **Untuk Apa:** [Purpose]
   > - **Masalah yang Diselesaikan:** [Problem Solved]
   > - **Keputusan/Output:** [Core Decision / Artifacts]
   ```
2. **Bidirectional Linking:**
   Connect concepts, theories, supervisors, and variables using `[[Wikilinks]]`.

## 3. Auto-Capture & Session End (Mandatory Update Rules)
Whenever a key milestone, decision, revision, or insight occurs:
1. **Source of Truth Synchronization (MANDATORY):**
   - Whenever a new methodological decision, parameter change, hypothesis refinement, or supervisor directive (from Dr. Fredella Colline / examiners) occurs, the assistant MUST record a new canonical decision entry (`D31`, `D32`, etc.) in `04_Riset_&_Metodologi/SOURCE_OF_TRUTH.md` with date, rationale, and academic justification. Never let `SOURCE_OF_TRUTH.md` go stale!
2. **Universal PRD Synchronization:**
   - Whenever workflow architecture, agent roles, quality gates, or file organization subsystems change, the assistant MUST update `04_Riset_&_Metodologi/PRD_UNIVERSAL_SKRIPSI_FRAMEWORK_GRAPH_OF_AGENTS.md`.
3. **Session Logging:**
   - Auto-append an entry to `04_Riset_&_Metodologi/LOG_SESI_SECOND_BRAIN.md` with timestamp, focus, solution achieved, and touched files (starting with `> [!SUMMARY]`, using `[[wikilinks]]`).
4. **Dashboard & Graphify Refresh:**
   - Keep `00_DASHBOARD_SECOND_BRAIN.md` up-to-date (active pages, 54 verified references, gate status).
   - Run incremental graphify update to keep `graphify-out/` synchronized.
