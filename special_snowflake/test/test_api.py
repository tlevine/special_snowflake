import os
from io import StringIO
import pickle

import nose.tools as n

from special_snowflake import fromdicts, fromcsv, fromresponse
import special_snowflake.test.fixtures as f

def test_fromdicts_defaults():
    observed = fromdicts(f.headers, f.data)
    expected = {('b',),('a','c')}
    n.assert_equal(observed, expected)

    observed = fromdicts(f.headers, f.data, n_columns = 3, only_adjacent = False)
    expected = {('b',),('a','c')}
    n.assert_equal(observed, expected)

def test_fromcsv_stringio():
    fp = StringIO('''color;shape;meows
pink;square;no
green;square;no
yellow;square;yes
''')
    observed = fromcsv(fp, delimiter = ';', n_columns = 1)
    expected = {('color',)}
    n.assert_set_equal(observed, expected)

def test_fromcsv_file():
    path = os.path.join('special_snowflake','test','fixtures','carte-des-licencies-sportifs-dans-les-hauts-de-seine.csv')
    with open(path, 'r') as fp:
        observed = fromcsv(fp, delimiter = ';', n_columns = 1)
    expected = {('color',)}
    n.assert_set_equal(observed, expected)

def test_fromresponse():
    path = os.path.join('special_snowflake','test','fixtures','carte-des-licencies-sportifs-dans-les-hauts-de-seine.p')
    with open(path, 'rb') as fp:
        response = pickle.load(fp)
    observed = fromresponse(response, delimiter = ';', n_columns = 1)
    n.assert_set_equal(observed, set())

    observed = fromresponse(response, delimiter = ';', n_columns = 3)
    expected = {3}
    n.assert_set_equal(observed, expected)

def test_fromresponse():
    path = os.path.join('special_snowflake','test','fixtures','carte-des-licencies-sportifs-dans-les-hauts-de-seine.p')
    with open(path, 'rb') as fp:
        response = pickle.load(fp)
    observed = fromresponse(response, delimiter = ';', n_columns = 1)
    n.assert_set_equal(observed, set())

    observed = fromresponse(response, delimiter = ';', n_columns = 3)
    expected = {3}
    n.assert_set_equal(observed, expected)
