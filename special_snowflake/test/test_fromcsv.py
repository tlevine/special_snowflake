import os
import nose.tools as n

from special_snowflake.fromcsv import _separate_fp

def test_separate_fp():
    with open(os.path.join('special_snowflake','test','fixtures','carte-des-licencies-sportifs-dans-les-hauts-de-seine.csv')) as fp:
        header, data = _separate_fp(fp, delimiter = ';')
        assert False, (header, next(data))
#   observed = _None, {})
    assert False, observed
