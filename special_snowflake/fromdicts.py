from itertools import combinations
from sliding_window import window

def _fromdicts(header, data, n_columns, only_adjacent):
    '''
    Given an iterable of dicts, find the keys that are primary keys across the dicts.

    Args:
        data: Iterable of dicts
        n_columns: How many columns wide is the primary key allowed to be?
        only_adjacent: If this is true, I'll assume that columns in a primary key must be adjacent.

    Returns:
        set of primary keys
    '''
    if only_adjacent:
        f = window
    else:
        f = combinations

    hashes = {columns:set() for columns in f(header, n_columns)}
    nrow = 0
    for row in data:
        for columns in hashes:
            hashes[columns].add(multicol_hash(row, columns))
        nrow += 1
    return set(k for k,v in hashes.items() if len(v) == nrow)

def multicol_hash(row, columns):
    return hash(tuple(row[column] for column in columns))
