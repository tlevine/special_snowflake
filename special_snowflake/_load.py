import csv
import json

from special_snowflake._snowflake import fromdicts

def separate_fp(fp, *args, **kwargs):
    header = next(csv.reader(fp, *args, **kwargs))
    data = csv.DictReader(fp, *args, **kwargs)
    return header, data

def fromcsv(fp, n_columns = 3, only_adjacent = True, **kwargs):
    header, data = separate_fp(fp, **kwargs)
    return fromdicts(header, data, n_columns = n_columns, only_adjacent = only_adjacent)
