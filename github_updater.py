#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 18:05:05 2023

@author: WhiteyCookie
"""

import os
import subprocess

GREEN = '\033[92m'  # Green text
RED = '\033[91m'    # Red text
RESET = '\033[0m'   # Reset text formatting

base_path = ''

def create_requirements_file(repo_path):
    venv_dir = os.path.join(repo_path, 'venv')
    venv_activate = os.path.join(venv_dir, 'bin', 'activate')

    try:
        # Activate the virtual environment
        subprocess.check_output(['bash', '-c', f'source {venv_activate} && pip freeze > requirements.txt'], stderr=subprocess.STDOUT, cwd=repo_path, universal_newlines=True)
    except subprocess.CalledProcessError as e:
        # Handle any errors and log them
        with open(os.path.join(repo_path, 'update_log.txt'), 'a') as log_file:
            log_file.write(f"Error creating 'requirements.txt' in '{repo_path}':\n{e.output}\n")
        print(f"{RED}Error creating 'requirements.txt' in '{repo_path}':{RESET}")
        print(e.output)

def update_repositories():
    for repo_dir in os.listdir(base_path):
        repo_path = os.path.join(base_path, repo_dir)

        if os.path.isdir(repo_path):
            try:
                # Check if a virtual environment exists or create one if not
                venv_dir = os.path.join(repo_path, 'venv')
                venv_activate = os.path.join(venv_dir, 'bin', 'activate')
                if not os.path.exists(venv_activate):
                    subprocess.check_output(['python3', '-m', 'venv', venv_dir])

                # Activate the virtual environment and create 'requirements.txt'
                create_requirements_file(repo_path)

                # Now, check if requirements.txt exists before running 'git pull'
                req_file = os.path.join(repo_path, 'requirements.txt')
                if os.path.exists(req_file):
                    pull_output = subprocess.check_output(['git', 'pull'], cwd=repo_path, stderr=subprocess.STDOUT, universal_newlines=True)

                    print(f"{GREEN}Updating '{repo_dir}':{RESET}")
                    print(pull_output)
                else:
                    print(f"{RED}Error: 'requirements.txt' not found in '{repo_dir}'{RESET}")
            except subprocess.CalledProcessError as e:
                # Handle any errors and log them
                with open(os.path.join(repo_path, 'update_log.txt'), 'a') as log_file:
                    log_file.write(f"Error updating '{repo_dir}':\n{e.output}\n")
                print(f"{RED}Error updating '{repo_dir}':{RESET}")
                print(e.output)
            except Exception as ex:
                print(f"{RED}Error in '{repo_dir}': {str(ex)}{RESET}")

if __name__ == '__main__':
    update_repositories()
    
