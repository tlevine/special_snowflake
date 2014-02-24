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


r = csv.DictReader(open('open-data-index.csv'))
for a in r:
    print(a)
    break
