from special_snowflake.fromcsv import _separate_fp
from special_snowflake.fromdicts import _fromdicts

def fromcsv(fp, n_columns = 3, only_adjacent = True, **csv_kwargs):
    header, data = _separate_fp(fp, **csv_kwargs)
    return _fromdicts(header, data, n_columns, only_adjacent)

def fromdicts(header, data, n_columns = 3, only_adjacent = True):
    return _fromdicts(header, data, n_columns, only_adjacent)
