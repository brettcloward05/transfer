#!/usr/bin/env python3
"""
@author      : wsu001 (wsu001@cs3030_85)
@file        : data_analysis
@created     : Monday Nov 19, 2018 15:24:58 UTC

Module Documentation Here
"""
from __future__ import print_function
import sqlite3
import os
import csv
import mock_sqlite


def get_files(mock):
    """
    Change to data directory, open each file,
    do your bookkeeping,
    Go back to your working directory
    :param mock: Mock Dictionary from mock_sqlite
    """
    file_list = os.listdir(mock['file']) # get dir content
    # print(file_list)
    saved_path = os.getcwd()            # get pwd
    os.chdir(mock['file'])              # go to the data
    # loop over data directory
    for file in file_list:
        # Select only CSV files
        if file.endswith(".csv"):
            print("Processing: ", file)
        else:
            continue
        with open(file, mode='rt', encoding='utf-8') as fin:
            # Get a csv object
            transactions = csv.reader(fin, delimiter=',')
            # loop over this object
            for rec in transactions:
                # Strip header records
                if rec[0] == "id":
                    continue
                # Record map
                # 0    1      2      3      4        5
                # id, fName, lName, email, Gender, Nationality
                # fix email, set default: waldo@weber.edu
                if rec[3] == "":
                    rec[3] = "waldo@weber.edu"
                # Add record to mock dictionary
                # print(rec)
                mock['rec'] = rec
                mock_sqlite.data_entry(mock)
                # TODO: you probably want to bring your
                # db commit here, and do it every 1000
                # records.

    os.chdir(saved_path)                # return to pwd


def select_data(mock):
    """
    Select Female Canadian records
    and print the total
    :param mock Dictionary
    """
    # Read data
    mock_sqlite.read_data(mock)
    # Fetch the data
    data = mock['cur'].fetchall()
    # iterate over data
    count = 0
    for row in data:
        if row[4] == 'Female' and row[5] == 'Canada':
            count += 1
            #print(row)

    # Print total
    print("Total number of Female Canadians is: ", count)



def main():
    """
    Test your module
    """
    # Create your mock object with DB information
    mock = mock_sqlite.mock
    # data directory
    data_dir = "data"
    mock['file'] = data_dir
    # Connect to Database
    conn = sqlite3.connect("tutorial.db")
    mock['conn'] = conn
    # Create a cursor
    cur = conn.cursor()
    mock['cur'] = cur

    # Create a table
    mock_sqlite.create_table(mock)
    # Insert data (Do this once)
    # get_files(mock)

    # Select data
    select_data(mock)

    # Close cursor
    cur.close()
    # Close database connection
    conn.close()


if __name__ == "__main__":
    main()
    exit(0)
