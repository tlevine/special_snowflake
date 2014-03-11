import csv
import json

def _separate_fp(fp, *args, **kwargs):
    '''
    Return a tuple of
        list of field names
        csv.DictReader
    '''
    position = fp.tell()
    header = next(csv.reader(fp, *args, **kwargs))
    fp.seek(position)
    data = csv.DictReader(fp, *args, **kwargs)
    return header, data
