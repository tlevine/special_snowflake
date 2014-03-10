from io import StringIO

import nose.tools as n

from special_snowflake.api import fromdicts, fromcsv
import special_snowflake.test.fixtures as f

def test_fromdicts():
    observed = fromdicts(f.headers, f.data, only_adjacent = True)
    assert False, observed

@n.nottest
def test_fromcsv_comma():
    fp = StringIO('''color,shape,meows\r
pink,square,no\r
green,square,no\r
yellow,cat,yes\r
''')
    fp.seek(0)
    observed = fromcsv(fp)
    expected = {('color',)}
    n.assert_set_equal(observed, expected)

@n.nottest
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
