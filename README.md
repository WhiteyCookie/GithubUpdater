# README for GitHub Repository Update Script

# Introduction

This script is designed to streamline and automate the process of updating multiple repositories. It primarily focuses on activating virtual environments, 
generating requirements.txt files, and pulling the latest changes from GitHub.

# Features

  Virtual Environment Management: Automatically checks for and sets up virtual environments in each repository.
  
  Requirements File Generation: Creates requirements.txt files for each repository, listing all dependencies.
  
  Git Pull Automation: Performs git pull to update repositories to the latest version.
  
  Error Logging: Logs errors encountered during the update process in a dedicated log file.

# Installation

  Clone this repository to your local machine.

    git clone https://github.com/WhiteyCookie/GithubUpdater.git

# Usage

  Set the base_path = '' variable in the script to the directory containing your GitHub repositories.
  
  Run the script using the command: 
  
    python3 github_updater.py
  
  The script will iterate over each repository in the specified base directory, set up a virtual environment if not present, create a requirements.txt file, and perform a git pull.

# Error Handling

  In case of any errors during the execution, the script logs them into an update_log.txt file in the respective repository directory.
  
  The script outputs error messages in red for clear visibility.

# Contributing

Your contributions are what make the open-source community such an amazing place to learn, inspire, and create. 

Any contributions you make are greatly appreciated. Fork the repository, make your changes, and submit a pull request.

# Acknowledgments

Special thanks to OpenAI's ChatGPT for its invaluable assistance during the development of this project. 
The guidance and support provided by ChatGPT were instrumental in addressing various coding challenges and enhancing the script's functionality.

# License

This project is released under the GNU General Public License (GPL), which provides copyleft for the distribution of free software. For more details, see the LICENSE file.

# Support

If you encounter any issues or have any questions, please file an issue in the GitHub issue tracker.
