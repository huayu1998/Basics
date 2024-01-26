# CS6704 SE Basics Workshop - APIs Requirements
# Author: Huayu Liang

# The script "get_repo_info.sh" is used to retrieve information about a specific GitHub repository (huayu1998/Basics) and saves it as a JSON file named "repo_info_huayu1998_Basics.json".

# The script "get_repo_issues.sh" is used to retrieves a list of issues from a GitHub repository (huayu1998/Basics) and saves it as a JSON file named "repo_issues_huayu1998_Basics.json".

#!/bin/bash

# GitHub API endpoint to get information about a repository
repo_url="https://api.github.com/repos/huayu1998/Basics"

# Make API request and save the output as a JSON file
curl -s "$repo_url" -o "repo_info_huayu1998_Basics.json"

# GitHub API endpoint to list issues in a repository
issues_url="https://api.github.com/repos/huayu1998/Basics/issues"

# Make API request and save the output as a JSON file
curl -s "$issues_url" -o "repo_issues_huayu1998_Basics.json"