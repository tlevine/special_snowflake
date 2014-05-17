import os
import io
import csv

from special_snowflake.fromcsv import _separate_fp, _dialect
from special_snowflake.fromdicts import _fromdicts

def fromcsv(fp, n_columns = 3, only_adjacent = False, **csv_kwargs):
    # Check for emptiness
    position = fp.tell()
    if fp.seek(0, os.SEEK_END) == 0:
        return set()
    fp.seek(position, os.SEEK_SET)

    # Detect dialect if no csv stuff is specified
    if csv_kwargs == {}:
        try:
            csv_kwargs['dialect'] = _dialect(fp)
        except csv.Error:
            pass

    # Go
    header, data = _separate_fp(fp, **csv_kwargs)
    return _fromdicts(header, data, n_columns, only_adjacent)

def fromresponse(response, n_columns = 3, only_adjacent = False, **csv_kwargs):
    'Load from an HTTP response object.'
    fp = io.StringIO(response.text)
    return fromcsv(fp, n_columns = n_columns, only_adjacent = only_adjacent, **csv_kwargs)

def fromdicts(header, data, n_columns = 3, only_adjacent = False):
    return _fromdicts(header, data, n_columns, only_adjacent)
