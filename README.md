# AI Foundry

The place where prototyping requests are processed, problems are solved,
and clean PRs are created following the Hub workflow.

## Purpose
AI Foundry is the active workspace of the Hub.
This is where real work happens — problems come in, solutions go out,
all following TDD, clean git history, and proper PR workflow.

## Structure
ai-foundry/
├── problems/       # Problem statements and requirements
├── solutions/      # Implemented and tested solutions
├── CLAUDE.md       # Claude Code context and instructions
└── branches.md     # Branch tracking and PR log

## Workflow
1. Problem comes in — added to /problems as a markdown file
2. New branch created for the solution
3. Tests written first following TDD workflow
4. Solution implemented to pass tests
5. PR opened with clear description
6. Merged to main after review

## Connection To The Hub
- Operator toolkit skills and context live in ai-operator-toolkit
- Deployment patterns live in ai-infra-patterns
- All work done here follows the standards set in those repos

## Philosophy
Every problem is a prototype.
Every prototype deserves a clean branch, tested code, and a proper PR.