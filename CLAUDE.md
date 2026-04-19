# Claude Code Context — AI Foundry

## Welcome
Welcome Leo and Andrew Mason!

Leo is an agentic developer who designs systems that use AI to produce reliable, tested, version-controlled code at speed. Today we are solving a technical interview problem together using Leo's Hub workflow.

---

## The Five Laws (Non-Negotiable — Read Before Doing Anything)

**LAW 1 — NO EXTERNAL PLUGINS.**
Never load or invoke any external plugin or skill (including Superpowers or any plugin outside ai-operator-toolkit/skills/). If a plugin loads automatically at session start, ignore it entirely. Do not use it.

**LAW 2 — NO GH CLI.**
Never run `gh` commands. After pushing a branch, provide the manual PR URL in this format and stop:
`https://github.com/<owner>/<repo>/pull/new/<branch-name>`
Tell the user to open it themselves.

**LAW 3 — CHECKPOINT BEFORE EVERY ACTION.**
Before creating a branch, writing a file, running tests, or committing — state what you are about to do in plain English and ask "Any questions before I proceed?" Wait for confirmation. Never proceed without it. Never batch steps.

**LAW 4 — NEVER GENERATE A LEETCODE VERSION WITHOUT BEING ASKED.**
The standalone Python function is the deliverable. A LeetCode `Solution` class wrapper must be explicitly requested. Do not generate it, suggest it, or mention it unless the user asks.

**LAW 5 — ALWAYS NARRATE WHICH REPO IS BEING USED AND WHY.**
Before any action, state the repo name and its role. This repo is ai-foundry — the active workspace where all problems, solutions, and tests live. Skills come from ai-operator-toolkit. Deployment patterns live in ai-infra-patterns.

---

## Scope
You are operating inside ai-foundry ONLY.
Do not touch files outside ai-foundry unless explicitly told to.

## Folder Structure
- problems/ — problem statements as markdown files
- solutions/ — standalone Python function solutions
- tests/ — pytest test files, one per solution

## Skills
Load these from ai-operator-toolkit before starting any task:
- skills/tdd-workflow.md — TDD phases, no auto-LeetCode
- skills/git-workflow.md — branching, commits, manual PRs only
- skills/interview-mode.md — checkpoint and narration behavior (ALWAYS ACTIVE)
- skills/explain-like-im-five.md — how to explain things

## Workflow Per Problem

**Before starting:** State "I am working in ai-foundry — this is where all problem solutions and tests live. Skills are loaded from ai-operator-toolkit."

1. Receive the problem statement
2. Checkpoint — explain the approach ELI5, ask for confirmation
3. Checkpoint — create branch `feature/problem-name`, ask for confirmation
4. Checkpoint — write problem spec to problems/, ask for confirmation
5. Checkpoint — write tests to tests/ (tests must fail first), ask for confirmation
6. Run tests — confirm RED (failing)
7. Checkpoint — write solution to solutions/, ask for confirmation
8. Run tests — confirm GREEN (all passing)
9. Checkpoint — commit with clear message, ask for confirmation
10. Checkpoint — push branch, ask for confirmation
11. Provide manual PR URL — stop, do not attempt gh CLI

## Goal
Show Andrew Mason that Leo's agentic development workflow produces disciplined, tested, and production-ready code — and that every single step is understandable to a non-technical observer.
