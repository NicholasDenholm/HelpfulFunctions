#!/bin/bash

# Auto-detect Git identity
git_user=$(git config user.name || git config --global user.name)
git_email=$(git config user.email || git config --global user.email)

if [ -z "$git_user" ]; then
    git_user="$USER"
    git_email="$USER@$(hostname)"
fi

echo "$git_user"
echo "$git_email"