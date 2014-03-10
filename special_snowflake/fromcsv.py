import csv
import json

def _separate_fp(fp, *args, **kwargs):
    '''
    Return a tuple of
        list of field names
        csv.DictReader
    '''
    header = next(csv.reader(fp, *args, **kwargs))
    data = csv.DictReader(fp, *args, **kwargs)
    return header, data

def _fromcsv(separate_fp, fp, csv_kwargs):
    return separate_fp(fp, **csv_kwargs)
