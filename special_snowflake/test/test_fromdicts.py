from io import StringIO

import nose.tools as n

from special_snowflake.fromdicts import _fromdicts, multicol_hash

data = [
    {'a':8, 'b': 3,'c':13,'d': 8},
    {'a':88,'b': 1,'c':10,'d': 8},
    {'a':8, 'b':23,'c':10,'d': 8},
]
headers = ('a','b','c','d')

def test_multicol_hash():
    row = {'a':8,'b':3,'c':10}
    observed = multicol_hash(row, ('a','b'))
    expected = hash((8,3))
    n.assert_equal(observed, expected)

def test_multicol_hash_on_missing_key():
    row = {'a':8,'b':3,'c':10}
    observed = multicol_hash(row, ('a','d'))
    expected = hash((8,None))
    n.assert_equal(observed, expected)

def test_snowflake_1_adjacent():
    observed = _fromdicts(headers, data, 1, True)
    expected = {('b',)}
    n.assert_set_equal(observed, expected)

def test_snowflake_1_nonadjacent():
    observed = _fromdicts(headers, data, 1, False)
    expected = {('b',)}
    n.assert_set_equal(observed, expected)

def test_snowflake_2_adjacent():
    observed = _fromdicts(headers, data, 2, True)
    expected = {('a','b'),('b','c'),}
    n.assert_set_equal(observed, expected)

def test_snowflake_2_nonadjacent():
    observed = _fromdicts(headers, data, 2, False)
    expected = {('a','b'),('b','c'),('b','d'),('a','c')}
    n.assert_set_equal(observed, expected)
