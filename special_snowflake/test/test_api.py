import os
from io import StringIO

import nose.tools as n

from special_snowflake import fromdicts, fromcsv
import special_snowflake.test.fixtures as f

def test_fromdicts_defaults():
    observed = fromdicts(f.headers, f.data)
    expected = {('b',),('b', 'c', 'd'), ('a', 'b', 'c')}
    n.assert_equal(observed, expected)

    observed = fromdicts(f.headers, f.data, n_columns = 3, only_adjacent = True)
    expected = {('b',),('b', 'c', 'd'), ('a', 'b', 'c')}
    n.assert_equal(observed, expected)

def test_fromcsv_semicolon():
    fp = StringIO('''color;shape;meows
pink;square;no
green;square;no
yellow;square;yes
''')
    fp.seek(0)
    observed = fromcsv(fp, delimiter = ';', n_columns = 1)
    expected = {('color',)}
    n.assert_set_equal(observed, expected)
