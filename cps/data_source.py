import astropy.units as u
from astropy.wcs import WCS
from astropy.coordinates import SkyCoord

class data_source:
    def __init__(self, database: object, *args, **kwargs) -> None:
        """
        Astronomical data source

        Args:
            database (object): one of database provide by astroquery
        """
        self.database = database
        self.args = args
        self.kwargs = kwargs
        self.imgs = None

    def query(self):
        self.imgs = self.database.get_images(*self.args, **self.kwargs)

    def headers(self):
        """
        Get general information of images

        Returns:
            header (str): the header of images
        """
        return [WCS(x[0].header) for x in self.imgs]