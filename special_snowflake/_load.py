import csv
import json

from special_snowflake._snowflake import fromdicts

def separate_fp(fp, *args, **kwargs):
    header = next(csv.reader(fp, *args, **kwargs))
    data = csv.DictReader(fp, *args, **kwargs)
    return header, data

def fromcsv(fp, *args, **kwargs):
    header, data = separate_fp(fp, *args, **kwargs)
    return fromdicts(header, data)
