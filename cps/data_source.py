# from cps import annulus_class
import astropy.units as u
from astropy.wcs import WCS
from astropy.coordinates import SkyCoord
from astropy.stats import SigmaClip, sigma_clipped_stats
from photutils import *

class data_source:
    def __init__(self, database: object, list_survey=False, *args, **kwargs) -> None:
        """
        Astronomical data source

        Args:
            database (object): one of database provide by astroquery
        """
        self.database = database
        self.args = args
        self.kwargs = kwargs
        self.imgs = None
        self.masks = None

        if list_survey:
            database.list_surveys()

    def query(self, *args, **kwargs):
        if args or kwargs:
            self.args = args
            self.kwargs = kwargs
        self.imgs = self.database.get_images(*self.args, **self.kwargs)

    def headers(self):
        """
        Get general information of images

        Returns:
            header (str): the header of images
        """
        return [WCS(x[0].header) for x in self.imgs]

    def images(self):
        return [x[0].data for x in self.imgs]

    def set_masks(self, method='source_mask', images='all'):
        data_list = []
        if images == 'all':
            data_list = self.images()

        if method == 'source_mask':
            self.masks = [
                make_source_mask(data, nsigma=2, npixels=5, dilate_size=11)
                for data in data_list
            ]

    # def center_flux():

    def background(self, images='all'):
        mean_list = median_list = std_list = []
        for data, mask in zip(self.images(), self.masks):
            mean, median, std = sigma_clipped_stats(data, sigma=3.0, mask=mask)
            mean_list.append(mean)
            median_list.append(median)
            std_list.append(std)
        return mean_list, median_list, std_list
        