import matplotlib.pyplot as plt
from cps.data_source import data_source
from astroquery.skyview import SkyView
from astropy.coordinates import SkyCoord

def test_query():
    position='Eta Carinae'
    survey=['Fermi 5', 'HRI', 'DSS']
    # ds = data_source(SkyView)
    # position = SkyCoord(ra, dec, unit='deg',frame='fk5')
    # survey = 'WISE 3.4'
    ds = data_source(SkyView, position=position, survey=survey)
    ds.query()

def test_images_and_headers():
    ds = data_source(SkyView, position='Eta Carinae', survey='DSS')
    ds.query()
    print(ds.headers())

    data = ds.images()
    plt.imshow(data[0])
    plt.show()

def test_masks_and_background():
    ds = data_source(SkyView, position='Eta Carinae', survey='DSS')
    ds.query()
    ds.set_masks()
    mean, median, std = ds.background()
    print(mean, median, std)

