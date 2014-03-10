def test_fromcsv_comma():
    fp = StringIO('''color,shape,meows\r
pink,square,no\r
green,square,no\r
yellow,cat,yes\r
''')
    fp.seek(0)
    observed = special_snowflake._load.fromcsv(fp)
    expected = {('color',)}
    n.assert_set_equal(observed, expected)

def test_fromcsv_semicolon():
    fp = StringIO('''color;shape;meows
pink;square;no
green;square;no
yellow;square;yes
''')
    fp.seek(0)
    observed = special_snowflake._load.fromcsv(fp, delimiter = ';', n_columns = 1)
    expected = {('color',)}
    n.assert_set_equal(observed, expected)
