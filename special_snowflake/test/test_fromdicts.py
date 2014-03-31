from io import StringIO

import nose.tools as n

from special_snowflake.fromdicts import _fromdicts, multicol_hash
from special_snowflake.test.fixtures import data, data2, headers

def test_multicol_hash():
    row = {'a':8,'b':3,'c':10}
    observed = multicol_hash(row, ('a','b'))
    expected = hash((8,3))
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

def test_intelligence():
    '''
    Multi-column keys should not be returned
    if there are simpler keys within the same columns.
    '''
    observed = _fromdicts(headers, data2, 2, False)
    expected = {('a',),('c','d',)}
    n.assert_set_equal(observed, expected)
