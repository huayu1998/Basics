#!/bin/bash

# GitHub API endpoint to get information about a repository
repo_url="https://api.github.com/repos/huayu1998/Basics"

# Make API request and save the output as a JSON file
curl -s "$repo_url" -o "repo_info_huayu1998_Basics.json"
