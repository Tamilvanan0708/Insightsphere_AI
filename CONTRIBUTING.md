# Git Branch & Contribution Workflow

## Branch Naming Rules

- Features: `feat/<story-id>-<short-description>` (e.g., `feat/ex-01-schema`, `feat/task-2.7-extraction-libs`)
- Bug fixes: `fix/<issue-description>`
- Chores / Setup: `chore/<description>`

## Commit Message Format

Follow Conventional Commits:
- `feat:` for new features or capabilities
- `fix:` for bug fixes
- `test:` for test suites
- `docs:` for documentation updates
- `chore:` for dependencies, config, or maintenance

## Development Workflow

1. Always pull latest `main` before creating a new branch.
2. Create your feature branch from `main`.
3. Test changes locally before committing.
4. Push branch and open a Pull Request for review.
5. All code must pass review before merging to `main`.
