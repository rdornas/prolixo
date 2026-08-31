# Project Guidelines & Rules

## Purpose & Execution Philosophy
Complete the current task with the minimal sufficient solution.
Prohibit over-engineering.
Planning can be aggressive, but execution must be lightweight.
Designs that cannot prove necessity are not done by default.
Development follows **TDD (Test-Driven Development)**: every feature, fix, and behavior must be validated by automated tests without introducing unnecessary abstraction or test complexity.

## Language Conventions
- **Internal Project Language**: All codebase files, source code, comments, docstrings, configuration files, Makefiles, Dockerfiles, compose specs, technical documentation, commit messages, and internal console/system logs MUST be written in **English**.
- **Chat & User Interaction**: Conversational dialogue with the user in chat is conducted in **Portuguese (PT-BR)**.
- **Application & Domain Data**: Application-specific domain assets (e.g., lexical dictionaries, linguistic corpora, target language word lists in Portuguese, Spanish, Latin, etc.) remain in their respective original/intended language.

## Workflow
1. Understand the requirements first, then take action. Do not modify code first and guess the intent afterward.
2. Higher reasoning can be used in the planning phase. In the execution phase, default to medium-low reasoning, or switch to a lighter model for implementation.
3. Do not keep the highest reasoning mode on throughout.
4. Do not default to spinning up multiple Agents in parallel. Complete one task in a single thread first, then decide whether to split it.
5. Only enable skills that are necessary to complete the task. Do not install heavy-process skills.
6. Produce a minimal plan first, then execute. The plan must clearly state:
   - Goals
   - Non-goals
   - Acceptance criteria
   - Scope not to be changed

### Git & Branching Workflow (Passo Curto / Passo Longo)
- **Main Branch is Sacred**: Direct commits or pushes to the `main` branch are strictly prohibited. All changes must go through dedicated feature/fix branches.
- **"Passo Curto" (Short Step)**: Create/switch to a branch and commit the changes locally. (No push, no PR).
- **"Passo Longo" (Long Step)**: Create/switch to a branch, commit the changes, push the branch to the remote repository, and open a Pull Request (PR) targeting `main`.
  - **Pre-Push Documentation Updates**: Before executing the push, review if project documentation files ([`roadmap.md`](roadmap.md), [`INFRASTRUCTURE.md`](INFRASTRUCTURE.md), [`README.md`](README.md)) need updates to reflect the changes. When applicable, update and commit these files before pushing.
  - **PR Content**: The PR description MUST include a clear summary of what was done and the specific automated tests executed.
- **Autonomous Execution Permission**: When the user requests or authorizes a "Passo Curto" or "Passo Longo" in the conversation, the agent is **fully authorized** to execute whatever operations are necessary to complete that workflow end-to-end (e.g. branch creation, local commits, automated test runs, documentation updates, and `git push` to the remote branch) directly and autonomously without asking repetitive conversational permission questions.


## Action Boundaries & Permissions
1. **Pre-action Restatement**:
   - What the user truly wants
   - The scope of this time
   - Things explicitly not to do
   - What counts as completion
2. **Dependency & Package Management (CRITICAL)**:
   - **Never install or update packages/dependencies automatically**: Do not run package manager commands (`pip`, `npm`, `yarn`, `pnpm`, `brew`, `cargo`, etc.) or add new libraries to requirements/lock files without first obtaining explicit permission from the user.
   - **Explain Before Requesting**: Whenever a new package or dependency is needed, explain to the user:
     1. *Package Name*: Exact name and version (if applicable).
     2. *Purpose*: What the package does.
     3. *Justification*: Why it is needed and what problem it solves.
     4. *Alternatives*: If there is a native/built-in way to accomplish the task without adding the third-party dependency.
   - **Wait for Confirmation**: Wait for explicit user confirmation before executing any installation command or modifying dependency files.
3. **Irreversible Operations**:
   - For any irreversible operation, must wait for user reply with confirmation codeword before executing.
   - Confirmation codeword is specified by the user.
   - Without codeword, wrong codeword, or other replies, refuse execution outright.
4. **Safe Operations (Permitted by default)**:
   - Git rollback, revert, branch switch, branch creation
   - Moving files to the backup directory of the current repository
   - Running tests, viewing diffs, generating plans, read-only analysis
   - Local staging, commits, and remote branch push when completing a user-requested "Passo Curto" or "Passo Longo"

5. **Stop Signals & Anti-Bloat Triggers**:
   - If you find yourself doing any of the following, must stop and switch to a smaller solution:
     - Adding new abstractions, frameworks, or config layers that the current requirement doesn't need
     - Designing ahead for possible future use
     - Continuing to stack more constraints to satisfy existing ones
     - Modifying many unrelated files at once
     - Creating a second implementation to accommodate old logic
     - Using the opportunity to add a complete test suite
6. **Project Documentation & Tracking Updates**:
   - Any modification affecting infrastructure (Docker, compose, environment) MUST be documented in [`INFRASTRUCTURE.md`](INFRASTRUCTURE.md).
   - Any modification affecting milestones, features, or architectural plans MUST be documented in [`roadmap.md`](roadmap.md).
   - Any change affecting setup instructions, user guides, or project APIs MUST be documented in [`README.md`](README.md).
   - All relevant documentation updates must be committed before pushing.
7. **No Absolute Local Paths**:
   - **NEVER hardcode local machine absolute file paths** (e.g., `/Users/username/...`, `C:\Users\...`, `file:///Users/...`) in any codebase files, source code, comments, documentation, Markdown files, configuration files, Dockerfiles, or scripts. Always use relative repository paths to ensure portability across different developer environments and projects.
8. **Sandbox Bypass & External Permission Requests**:
   - Every time an action or command requires extrapolating or bypassing the sandbox (such as running commands with `BypassSandbox: true` or triggering an external permission prompt), you MUST output a visible explanation in the chat **BEFORE** triggering the tool call/modal. The explanation must detail:
     1. *Action/Command*: The exact command or operation to be run.
     2. *Justification*: Why sandbox extrapolation is strictly required (e.g., remote network connection for Git push, external authentication, etc.).
     3. *Expected Outcome*: What the operation will accomplish once approved.


## Failure Modes
1. Failing to truly understand the intent and only fixing surface issues.
2. When a clean root-cause fix could have been done once, instead piling on historical patches, compatibility layers, dual tracks, duplicates, and branches to bloat the code.
3. Over-designing for rare cases, increasing daily maintenance costs.
4. Wrong judgment basis: even if reasoning is complete, the conclusion is wrong.
5. Instead of directly reading the code to locate the issue, substituting with search or guesswork.
6. Using "add tests" as an excuse to keep adding abstraction, expanding scope, and making things seem complete.

## Testing & TDD Principles
Test-Driven Development (TDD) is the default development methodology for Prolixo.
Tests ensure correctness, prevent regressions, and guide design. However, tests should remain concise, readable, and free of over-engineering or mock bloat.

1. **Test-First & Behavior Coverage**: Write tests before or alongside implementation for each feature, endpoint, generator rule, or bugfix.
2. **Fast Feedback**: Maintain unit and integration test suites that execute quickly (sub-second or few seconds).
3. **No Test Over-Engineering**:
   - Write clean, straightforward assertions.
   - Avoid creating massive nested mock hierarchies when real objects or lightweight fixtures suffice.
   - Do not write overly complicated test utilities that are harder to maintain than the application code itself.
4. **Backend Testing**: Use `pytest` for unit and FastAPI integration tests covering all generator rules, algorithms, and endpoints.
5. **Frontend Validation**: Use TypeScript compile-time type checking and linting to validate UI contracts cleanly without mock bloat or heavy DOM simulation layers.
6. **Continuous Validation**: All tests must pass before code is committed or merged.

## Model Division of Labor
- Requirement clarification and solution review: Use stronger models
- Writing code, modifying code, running tests: Use medium-low spec models, or lighter execution models
- When the execution model starts stacking architecture, adding compatibility, or expanding unnecessary scope: Stop immediately and simplify

## Pre-Completion Checklist
- Intent and acceptance criteria have been restated
- Solution is well-tested following TDD principles
- Tests are fast, clean, and directly verify the intended behavior
- Only modified the minimal set of files needed to complete the task
- All existing and new tests pass successfully
- Relevant documentation (`roadmap.md`, `INFRASTRUCTURE.md`, `README.md`) updated and committed if applicable before push
- No hardcoded absolute local machine paths (e.g., `/Users/...`) in any file

## General Principles
Confirm intent first, then complete acceptance with minimal sufficient changes.
Designs that cannot prove necessity are not done by default.
All features and modifications are backed by automated tests (TDD).
