import nose.tools as n
import special_snowflake
import special_snowflake._snowflake
import special_snowflake._load

def test_multicol_hash():
    row = {'a':8,'b':3,'c':10}
    observed = special_snowflake._snowflake.multicol_hash(row, ('a','b'))
    expected = hash((8,3))
    n.assert_equal(observed, expected)

data = [
    {'a':8, 'b': 3,'c':13,'d': 8},
    {'a':88,'b': 1,'c':10,'d': 8},
    {'a':8, 'b':23,'c':10,'d': 8},
]
headers = ('a','b','c','d')

def test_snowflake_1_adjacent():
    observed = special_snowflake.fromdicts(headers, data, n_columns = 1, only_adjacent = True)
    expected = {('b',)}
    n.assert_set_equal(observed, expected)

def test_snowflake_1_nonadjacent():
    observed = special_snowflake.fromdicts(headers, data, n_columns = 1, only_adjacent = False)
    expected = {('b',)}
    n.assert_set_equal(observed, expected)

def test_snowflake_2_adjacent():
    observed = special_snowflake.fromdicts(headers, data, n_columns = 2, only_adjacent = True)
    expected = {('a','b'),('b','c'),}
    n.assert_set_equal(observed, expected)

def test_snowflake_2_nonadjacent():
    observed = special_snowflake.fromdicts(headers, data, n_columns = 2, only_adjacent = False)
    expected = {('a','b'),('b','c'),('b','d'),('a','c')}
    n.assert_set_equal(observed, expected)
