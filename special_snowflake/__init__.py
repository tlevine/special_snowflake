import csv
import json
import itertools
from sliding_window import window

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
    if only_adjacent:
        f = window
    else:
        f = itertools.combinations

    hashes = {columns:set() for columns in f(header, n_columns)}
    nrow = 0
    for row in data:
        for columns in hashes:
            hashes[columns].add(_multicol_hash(row, columns))
        nrow += 1
    return set(k for k,v in hashes.items() if len(v) == nrow)

def separate_fp(fp):
    header = next(csv.reader(fp))
    data = csv.DictReader(fp)
    return header, data

def fromcsv(fp, *args, **kwargs):
    header, data = separate_fp(fp)
    return fromdicts(header, data)

def _multicol_hash(row, columns):
    return hash(tuple((row[column] for column in columns)))
