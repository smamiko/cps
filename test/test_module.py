import cps
from astropy import table

def test_cross_match():
    assert type(cps.cross_match()) != type(table.Table)
