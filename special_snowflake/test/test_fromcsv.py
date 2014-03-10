import nose.tools as n

from special_snowflake.fromcsv import _fromcsv

def fake_separator(*args, **kwargs):
    return ['a','b'],[{'a':3,'b':9}]

def fake_fromdicts(header, data, n_columns, only_adjacent):
    return {('a',), ('b',), ('a','b')}

def test_fromcsv():
    observed = _fromcsv(fake_separator, fake_fromdicts, None, None, None, [], {})
    n.assert_set_equal(observed, {('a',), ('b',), ('a','b')})

@n.nottest
def test_fromcsv_comma():
    fp = StringIO('''color,shape,meows\r
pink,square,no\r
green,square,no\r
yellow,cat,yes\r
''')
    fp.seek(0)
    observed = _fromcsv(fp)
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
    observed = _fromcsv(fp, delimiter = ';', n_columns = 1)
    expected = {('color',)}
    n.assert_set_equal(observed, expected)
