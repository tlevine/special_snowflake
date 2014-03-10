from special_snowflake.fromcsv import _fromcsv, _separate_fp
from special_snowflake.fromdicts import _fromdicts

def fromcsv(fp, *csv_args, n_columns = 3, only_adjacent = True, **csv_kwargs):
    return _fromcsv(_separate_fp, fromdicts, fp, n_columns, only_adjacent, csv_args, csv_kwargs)

def fromdicts(header, data, n_columns = 3, only_adjacent = True):
    return _fromdicts(header, data, n_columns, only_adjacent)
