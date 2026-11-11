# Contribution and change controls

Use [Engineering Operating Model](engineering/OPERATING-MODEL.md) and the Issue and Pull Request templates.

## Before opening a Pull Request
1. Create or link a scoped GitHub Issue with explicit acceptance criteria.
2. State whether the target is a legacy, experimental, protected, or active repository.
3. Make changes on a dedicated feature branch, not by force-pushing main.
4. Keep dependencies pinned, avoid unverified archives and never commit secrets.
5. Run repository-specific lint, build and tests and note any checks not executed.
6. Include screenshots and accessibility checks for UI changes.
7. Document migration, data privacy and rollback considerations for DB or API changes.
8. Obtain an explicit review before merging. A successful AI review is not human approval.

Do not modify active client/local projects solely because a shared template was updated.
