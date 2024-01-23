#!/bin/bash

# GitHub API endpoint to list issues in a repository
issues_url="https://api.github.com/repos/huayu1998/Basics/issues"

# Make API request and save the output as a JSON file
curl -s "$issues_url" -o "repo_issues_huayu1998_Basics.json"
