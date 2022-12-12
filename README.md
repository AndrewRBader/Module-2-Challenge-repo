# Module-2-Challenge-repo
Columbia Fintech Bootcamp Module 2 Challenge
Due: 7/14/2022
By: Andrew Ryan Bader

# Project Title

Loan Qualifier App: The purpose of this app is for a user to have the ability to save a set of qualifying loans to a CSV file in order to share the results as a spreadsheet.

---

## Technologies

This project uses the Python. This project uses sys, fire, questionary, pathlib and csv libraries

---

## Installation Guide

To clone and use:
1) make a local directory for this github repository
2) clone down this repo with git clone command
3) cd into cloned repo
4) run the program with python command in cli
5) follow loan-qualifier-tool prompts

---

## Usage

Functionality:
When the qualifier is ran, the tool prompts the user to save the results as a CSV file (or not if user opts out). If no loans exist, the program should notify the user and exit. The tool will prompt for a file path to save the file. The tool saves the results as a CSV file

Modules and Directories:
app.py: the primary application file
data directory: includes the CSV file
qualifier folder: contains functions imported into the main app
filters: directory that contains .py files for filter functions
utils: includes financial calculator module and fileio module

1) Go through prompts and answer questions about income, debt, etc.
![loan tool prompts](assets/image-1.png "Loan Qualifier Prompts")
2) Chose yes/no for the save CSV prompt
![save CSV prompt](assets/image-2.png "Save loan CSV Prompt")
3a) If chose yes, find CSV in directory root
![new CSV file](assets/image-3.png "New CSV File")
3b) If chose no, program exits
![don't save CSV](assets/image-4.png "don't save CSV")
3c) If client doesn't qualify for loan
![don't qualify](assets/image-5.png "don't qualify")

---

## Contributors

Andrew Ryan Bader

---

## License

N/A
