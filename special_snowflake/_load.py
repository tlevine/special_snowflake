import csv
import json

def separate_fp(fp):
    header = next(csv.reader(fp))
    data = csv.DictReader(fp)
    return header, data

def fromcsv(fp, *args, **kwargs):
    header, data = separate_fp(fp)
    return fromdicts(header, data)
