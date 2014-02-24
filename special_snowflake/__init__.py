import csv

def snowflake(i, columns = 3, only_adjacent = True):
    '''
    Given an iterable of dicts, find the keys that are primary keys across the dicts.

    Args:
        i: Iterable of dicts
        columns: How many columns wide is the primary key allowed to be?
        only_adjacent: If this is true, I'll assume that columns in a primary key must be adjacent.

    Returns:
        dict with boolean values
    '''
    if columns != 1 or only_adjacent != False:
        raise NotImplementedError

    for row in i:
        if

def potential_keys(column_names, width):
    '''
    Args:
        column_names: list of key
        width: an integer
    '''

def main():
    with open('open-data-index.csv') as fp:
        print(snowflake(csv.DictReader(fp), columns = 1, only_adjacent = False))
