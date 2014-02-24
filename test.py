import nose.tools as n
import special_snowflake

def test_multicol_hash():
    row = {'a':8,'b':3,'c':10}
    observed = special_snowflake.multicol_hash(row, ('a','b'))
    expected = hash((8,3))
    n.assert_equal(observed, expected)
