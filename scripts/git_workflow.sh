#!/usr/bin/env bash
set -e

MODE="$1"
BRANCH="$2"
MSG="$3"
PR_TITLE="${4:-$MSG}"
PR_BODY="${5:-Automated Pull Request created by Prolixo workflow.}"

if [ -z "$MODE" ] || [ -z "$BRANCH" ] || [ -z "$MSG" ]; then
    echo "Usage: $0 <curto|longo> <branch_name> <commit_message> [pr_title] [pr_body]"
    exit 1
fi

CURRENT_BRANCH=$(git branch --show-current 2>/dev/null || echo "")
if [ "$CURRENT_BRANCH" != "$BRANCH" ]; then
    if git show-ref --verify --quiet "refs/heads/$BRANCH"; then
        git checkout "$BRANCH"
    else
        git checkout -b "$BRANCH"
    fi
fi

git add -A

if ! git diff --cached --quiet; then
    git commit -m "$MSG"
else
    echo "No new changes to commit."
fi

if [ "$MODE" = "longo" ]; then
    echo "Pushing branch $BRANCH to origin..."
    git push -u origin "$BRANCH"

    echo "Creating Pull Request targeting main..."
    if command -v gh >/dev/null 2>&1; then
        gh pr create --title "$PR_TITLE" --body "$PR_BODY" || echo "PR may already exist."
    else
        echo "GitHub CLI (gh) not found. Branch pushed successfully."
    fi
fi

echo "Git workflow ($MODE) completed successfully."
