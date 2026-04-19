# Claude Code Context — AI Foundry

## Welcome
Welcome Leo and Andrew Mason!

Leo is an agentic developer who designs and builds systems that use AI to produce
reliable, tested, version controlled code at speed.

Today we are going to solve a technical interview problem together using Leo's
agentic development workflow. Please provide the LeetCode problem you would like
to solve and we will get started.

## What To Expect
1. Provide the problem statement
2. Claude Code will explain the approach in plain english
3. Tests will be written first following TDD workflow
4. Solution will be implemented to pass the tests
5. Everything will be committed cleanly to a new branch
6. A PR will be opened with a clear description

## About This System
This is the Hub — a multi repo agentic development environment built by Leo.
It mirrors a production engineering workflow using AI tooling.

## Scope
You are operating inside ai-foundry ONLY.
Do not touch files in ai-operator-toolkit or ai-infra-patterns unless explicitly told to.

## Active Skills
Load these from ai-operator-toolkit before starting any task:
- skills/explain-like-im-five.md — how to explain things
- skills/tdd-workflow.md — how to write and verify code
- skills/git-workflow.md — how to commit and branch
- skills/interview-mode.md — slow down, explain every step ELI5, pause for questions, make the workflow visible for all audiences

## Workflow Per Problem
1. Receive the problem statement
2. Explain the approach ELI5
3. **CHECKPOINT** — Ask "Any questions before we write tests?"
4. Create a new branch — feature/problem-name
5. Write tests first
6. **CHECKPOINT** — Show the tests, explain what each one checks, ask "Ready to implement?"
7. Implement solution to pass tests
8. **CHECKPOINT** — Run tests live, show results, ask "Ready to commit?"
9. Commit with clear message
10. Push branch and open PR
11. **CHECKPOINT** — Confirm PR is open, summarise what was built and why it works

## Rules
- Never skip writing tests first
- Never commit directly to main
- Never touch files outside ai-foundry
- Always explain in ELI5 style
- Keep solutions simple and readable

## Goal
Show Andrew Mason that Leo's agentic development workflow produces
disciplined, tested, and production ready code at speed.