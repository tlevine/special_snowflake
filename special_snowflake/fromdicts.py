from itertools import combinations, chain
from sliding_window import window

def _factorial(f, iterable, n_columns):
    repeatable = list(iterable)
    for i in range(1, 1 + n_columns):
        yield from f(repeatable, i)

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
    return _dedupe(_fromdicts_duplicates(header, data, n_columns, only_adjacent))

def _fromdicts_duplicates(header, data, n_columns, only_adjacent):
    if len(header) < n_columns:
        n_columns = len(header)

    if only_adjacent:
        f = window
    else:
        f = combinations

    hashes = {columns:set() for columns in _factorial(f, header, n_columns)}
    nrow = 0
    for row in data:
        for columns in hashes:
            hashes[columns].add(multicol_hash(row, columns))
        nrow += 1
    return set(k for k,v in hashes.items() if len(v) == nrow)

def _dedupe(indices:set) -> set:
    '''
    Remove complex indices when simpler equivalents exist.
    '''
    result = set()
    top = 1 if indices == set() else max(map(len, indices)) 
    for ncol in range(1, top + 1):
        for columns in indices:
            if len(columns) == ncol:
                for subcolumns in _factorial(combinations, columns, ncol):
                    if subcolumns in result:
                        break
                else:
                    result.add(columns)
    return result

def multicol_hash(row, columns):
    return hash(tuple(row[column] for column in columns if column != None))
