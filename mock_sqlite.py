#!/usr/bin/env python3
"""
@author      : wsu001 (wsu001@cs3030_85)
@file        : mock_sqlite
@created     : Monday Nov 19, 2018 16:01:22 UTC

Module Documentation Here
"""
from __future__ import print_function
import sqlite3


# Mock dictionary to connect to DB and
# retrieve data
mock = dict(conn = None,
        cur = None,
        file = None,
        rec = None,
        rval = None)


def create_table(mock):
    """
    Create table for our db
    :param mock: Mock dictionary object with db info
    """
    mock['cur'].execute("""CREATE TABLE IF NOT EXISTS mock_data(
        id          INT,
        f_name      TEXT,
        l_name      TEXT,
        email       TEXT,
        gender      TEXT,
        nation      TEXT)""")

    print("Done creating table")


def data_entry(mock):
    """
    Dynamic data entry
    :param mock: Mock Dictionary
    """
    mock['cur'].execute("""INSERT INTO mock_data
    (id, f_name, l_name, email, gender, nation)
    VALUES (?, ?, ?, ?, ?, ?)""",
    mock['rec'])
    # Note: if you are inserting many records
    # you may want to have this commit outside
    # and do not commit after each record,
    # instead do a commit every 1000 records.
    mock['conn'].commit()


def read_data(mock):
    """
    Read data from DB
    :param mock: Mock Dictionary
    """
    sel = """SELECT * from mock_data"""
    mock['cur'].execute(sel)

    # test print data
    # data = mock['cur'].fetchall()
    # [print(row) for row in data]


def update_data(mock):
    """
    Update data entry
    :param mock: Mock Dictionary
    """
    pass


def delete_data(mock):
    """
    Delete data entry
    :param mock: Mock Dictionary
    """
    pass


def main():
    """
    Test your module
    """
    pass


if __name__ == "__main__":
    main()
    exit(0)
