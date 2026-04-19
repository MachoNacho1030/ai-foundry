# Branch Tracker

## Purpose
Track all branches, problems, and PRs in ai-foundry.
Every problem gets a branch. Every branch gets a PR. Every PR gets logged here.

## Active Branches
| Branch | Problem | Status | PR |
|--------|---------|--------|----|

## Merged Branches
| Branch | Problem | PR | Merged |
|--------|---------|-----|--------|
| prep/initial-scaffold | Initial setup | #1 | Yes |
| feature/two-sum | Two Sum | #3 | Yes |

## Branch Naming Convention
feature/problem-name
fix/problem-name
prep/description

## PR Log
### PR #1 — prep: initial scaffold of ai-foundry
- Branch: prep/initial-scaffold
- Status: Merged
- Description: Initial scaffold of ai-foundry including problems, solutions, and claude context

### PR #3 — feat: two sum — hashmap solution with full TDD test suite
- Branch: feature/two-sum
- Status: Merged
- Description: LeetCode #1. O(n) hashmap approach, 8 tests covering standard cases, negatives, duplicates, and large input.

## How To Add A New Problem
1. Add problem statement to /problems/problem-name.md
2. Create branch — git checkout -b feature/problem-name
3. Solve following TDD workflow
4. Push and open PR
5. Log it here after merge