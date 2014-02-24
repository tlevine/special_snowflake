import csv
import json
import itertools

def snowflake(data, n_columns = 3, only_adjacent = True):
    '''
    Given an iterable of dicts, find the keys that are primary keys across the dicts.

    Args:
        data: Iterable of dicts
        n_columns: How many columns wide is the primary key allowed to be?
        only_adjacent: If this is true, I'll assume that columns in a primary key must be adjacent.

    Returns:
        dict with boolean values
    '''
    if only_adjacent != False:
        raise NotImplementedError

    hashes = None
    nrow = 0
    for row in data:
        # First row only
        if hashes == None:
            hashes = {columns:set() for columns in itertools.combinations(row.keys(), n_columns)}

        for columns in hashes:
            hashes[columns].add(multicol_hash(row, columns))

        nrow += 1

    print(hashes)
    for columns in hashes:
        if len(hashes[columns]) == nrow:
            yield columns

def multicol_hash(row, columns):
    return hash(tuple((row[column] for column in columns)))

def main():
    with open('open-data-index.csv') as fp:
        print(list(snowflake(csv.DictReader(fp), n_columns = 1, only_adjacent = False)))

if __name__ == '__main__':
    main()
