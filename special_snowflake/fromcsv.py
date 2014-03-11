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

    _kwargs = dict(kwargs)
    _kwargs['fieldnames'] = _kwargs.get('fieldnames', header)
    _kwargs['restval'] = _kwargs.get('restval', '')
    data = csv.DictReader(fp, *args, **_kwargs)
    next(data) # skip the header
    return header, data
