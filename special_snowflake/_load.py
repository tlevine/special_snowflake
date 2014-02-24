import csv
import json

def separate_fp(fp, *args, **kwargs):
    header = next(csv.reader(fp, *args, **kwargs))
    data = csv.DictReader(fp, *args, **kwargs)
    return header, data

def fromcsv(fp, *args, **kwargs):
    header, data = separate_fp(fp)
    return fromdicts(header, data)
