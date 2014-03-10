import csv
import json

from special_snowflake._snowflake import fromdicts as _fromdicts

def _separate_fp(fp, *args, **kwargs):
    '''
    Return a tuple of
        list of field names
        csv.DictReader
    '''
    header = next(csv.reader(fp, *args, **kwargs))
    data = csv.DictReader(fp, *args, **kwargs)
    return header, data

def fromcsv(fp, *args, n_columns = 3, only_adjacent = True, **kwargs, fromdicts = _fromdicts):
    header, data = separate_fp(fp, *args, **kwargs)
    return _fromdicts(header, data, n_columns = n_columns, only_adjacent = only_adjacent)
