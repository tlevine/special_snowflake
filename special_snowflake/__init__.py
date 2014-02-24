import csv
import json
import itertools

def fromdicts(header, data, n_columns = 3, only_adjacent = True):
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

def fromcsv(fn, *args, **kwargs):
    with open(fn, 'r') as fp:
        header = next(csv.reader(fp))
        data = csv.DictReader(fp)
        out = fromdicts(header, data)
    return out

def _multicol_hash(row, columns):
    return hash(tuple((row[column] for column in columns)))
