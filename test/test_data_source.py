from cps.data_source import data_source
from astroquery.skyview import SkyView
from astropy.coordinates import SkyCoord

def test_query():
    position='Eta Carinae'
    survey=['Fermi 5', 'HRI', 'DSS']
    # position = SkyCoord(ra, dec, unit='deg',frame='fk5')
    # survey = 'WISE 3.4'
    ds = data_source(SkyView, position=position, survey=survey)
    ds.query()

    print(ds.headers())
