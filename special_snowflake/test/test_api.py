import os
from io import StringIO

import nose.tools as n

from special_snowflake.api import fromdicts, fromcsv
import special_snowflake.test.fixtures as f

def test_fromdicts_defaults():
    observed = fromdicts(f.headers, f.data)
    expected = {('b', 'c', 'd'), ('a', 'b', 'c')}
    n.assert_equal(observed, expected)

    observed = fromdicts(f.headers, f.data, n_columns = 3, only_adjacent = True)
    expected = {('b', 'c', 'd'), ('a', 'b', 'c')}
    n.assert_equal(observed, expected)

@n.nottest
def test_fromcsv_semicolon():
    with open(os.path.join('special_snowflake','test','fixtures','carte-des-licencies-sportifs-dans-les-hauts-de-seine.csv'), 'r') as fp:
        observed = fromcsv(fp, n_columns = 3, only_adjacent = True, delimiter = ';')
    n.assert_set_equal(observed, expected)
