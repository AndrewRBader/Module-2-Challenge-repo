# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
# added pathlib to get .csv for the save_CSV function
from pathlib import Path


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

# function that saves qualifying data as a file
def save_csv(qualifying_loans):
    # Set the output header
    header = ['Lender', 'Max Loan Amount', 'Max LTV', 'Max DTI', 'Min Credit Score', 'Interest Rate']

    # Set the output file path
    output_path = Path("qualifying_loans.csv")

    with open(output_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(header)
        
        for loan in qualifying_loans:
            csvwriter.writerow(loan)