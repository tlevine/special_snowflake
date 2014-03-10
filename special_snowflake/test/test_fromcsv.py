import nose.tools as n

from special_snowflake.fromcsv import _fromcsv

def test_fromcsv():

    def fake_separator(*args, **kwargs):
        return ['a','b'],[{'a':3,'b':9}]

    def fake_fromdicts(header, data, n_columns, only_adjacent):
        return {('a',), ('b',), ('a','b')}

    observed = _fromcsv(fake_separator, fake_fromdicts, None, None, None, [], {})
    n.assert_set_equal(observed, {('a',), ('b',), ('a','b')})
