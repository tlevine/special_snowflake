import nose.tools as n
import special_snowflake

def test_multicol_hash():
    row = {'a':8,'b':3,'c':10}
    observed = special_snowflake._multicol_hash(row, ('a','b'))
    expected = hash((8,3))
    n.assert_equal(observed, expected)

data = [
    {'a':8, 'b': 3,'c':13,'d': 8},
    {'a':88,'b': 1,'c':10,'d': 8},
    {'a':8, 'b':23,'c':10,'d': 8},
]

def test_snowflake_1_adjacent():
    observed = special_snowflake.snowflake(data, n_columns = 1, only_adjacent = True)
    expected = {('b',)}
    n.assert_set_equal(observed, expected)

def test_snowflake_1_nonadjacent():
    observed = special_snowflake.snowflake(data, n_columns = 1, only_adjacent = False)
    expected = {('b',)}
    n.assert_set_equal(observed, expected)
