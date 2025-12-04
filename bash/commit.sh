#!/bin/bash

echo $HOME
whoami

if [ $# -eq 0 ]; then
    echo "Please provide a commit message"
    exit 1
fi

# Get local username, fallback to global
git_user=$(git config --global user.name)
git_email=$(git config --global user.email)

echo "Git username: $git_user"
echo "Git email: $git_email"



git add .
git commit -m "$*"
git push