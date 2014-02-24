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
            hashes[columns].add(_multicol_hash(row, columns))

        nrow += 1

    return set(k for k,v in hashes.items() if len(v) == nrow)

def _multicol_hash(row, columns):
    return hash(tuple((row[column] for column in columns)))
