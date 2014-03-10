import nose.tools as n

from special_snowflake.fromcsv import _fromcsv

def test_fromcsv():

    def fake_separator(*args, **kwargs):
        return ['a','b'],[{'a':3,'b':9}]

    observed = _fromcsv(fake_separator, None, {})
    assert False, observed
