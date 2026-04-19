# Claude Code Context — AI Foundry

## Purpose
This file gives Claude Code the context it needs to work inside ai-foundry.
Read this before doing anything in this repo.

## Scope
You are operating inside ai-foundry ONLY.
Do not touch files in ai-operator-toolkit or ai-infra-patterns unless explicitly told to.
Scope discipline is critical to keeping the Hub clean.

## Your Job In This Repo
- Receive problem statements from /problems
- Create a new branch for each problem
- Write tests first following TDD workflow
- Implement the solution to pass the tests
- Commit cleanly following git workflow
- Open a PR with a clear description

## Active Skills
Load these from ai-operator-toolkit before starting any task:
- skills/explain-like-im-five.md — how to explain things
- skills/tdd-workflow.md — how to write and verify code
- skills/git-workflow.md — how to commit and branch

## Workflow Per Problem
1. Read the problem statement in /problems
2. Create a new branch — feature/problem-name
3. Create a new solution file in /solutions
4. Write tests first
5. Implement solution to pass tests
6. Run tests and confirm passing
7. Commit with clear message
8. Push branch and open PR

## Communication Style
- Start with a brief plan before writing any code
- Explain every step in ELI5 style
- Flag any blockers immediately
- End with a summary of what was done and what tests pass

## Rules
- Never skip writing tests first
- Never commit directly to main
- Never touch files outside ai-foundry
- Always confirm the problem is fully understood before starting
- Keep solutions simple and readable

## Goal
Solve technical interview style problems using a real engineering workflow.
Show that AI assisted development can be disciplined, tested, and production ready.