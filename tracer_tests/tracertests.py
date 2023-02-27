import numpy as np
from logging_parameters.checker import *

#authored by Mohammed Fadul
class Tracer:
    def __init__(self):
        self.d1 = .2     # drilling diameter m
        self.d2 = .125     # well's  diameter m
        self.hd = 1.42    # well's head m above ground level
        self.tgp1 = 4.8   # top of gravel pack m below ground level
        self.tfs1 = 5.8   # top of filter screen m below ground level
        self.bow = 8.3    # bottom of well m below ground level
        self.dof = 7.22    # depth of filter m below well's head
        self.wt = 6.85     # water table  m below well's head
        self.c = 900      # initial concentration of the tracer in the well
        self.k1 = .01     # permeability of the gravel pack
        self.k2 = .018     # permeability of the aquifer formation
        self.acc = 10      # accuracy of the fluorescence sensor
        self.top_gravel_pack()
        self.water_head()
        self.calculate_alpha()
        self.area_of_flow()
        self.volume_in_well()

    def top_gravel_pack(self,):
        """
        :return: (EXTRA, usable for other borehole Tests); distance from the wellhead to the top of the gravel pack
        """
        try:
            self.ba = self.tgp1+self.hd
            return self.ba
        except TypeError:
            logging.warning("non numeric data ; returning TGP = np.NaN")
            self.ba = np.nan
            return self.ba

    def top_filter_screen(self):
        """
        :return:(EXTRA, usable for other borehole Tests); distance from the wellhead to the top of the filter screen (tfs2)
        """
        try:
            return self.tfs1+self.hd
        except TypeError:
            logging.warning("non numeric data ; returning TFS = np.NaN")
            return np.nan

    def water_head(self):
        """
        :return: profile of the water in the well measured from the bottom of the well (wh)
        """
        try:
            return self.bow+self.hd-self.wt
        except TypeError:
            logging.warning("non numeric data ; returning WH = np.NaN")
            return np.nan

    def volume_in_well(self):
        """
        :return: the volume of the water in the well
        """
        w_h = self.water_head()
        try:
            self.viw = np.pi * .25 * (self.d2 ** 2) * w_h
            return self.viw
        except TypeError:
            logging.warning("non numeric data ; returning VIW = np.NaN")
            self.viw = np.nan
            return self.viw

    def area_of_flow(self):
        """
        :return: area perpendicular to the flow direction
        """
        w_h = self.water_head()
        try:
            self.f = self.d2*w_h
            return self.f
        except TypeError:
            logging.warning("non numeric data ; returning AoS = np.NaN")
            self.f = np.nan
            return self.f

    def calculate_alpha(self):
        """"
        :return: correction factor borehole horizontal flow rate Qb and aquifer horizontal flow rate Qf
        """
        try:
            self.alpha = 4/(1+((self.d2/self.d1)**2)+self.k2/self.k1*(1-((self.d2/self.d1)**2)))
            return self.alpha
        except TypeError:
            logging.warning("non numeric data ; returning alpha = np.NaN")
            self.alpha = np.nan
            return self.alpha

    def calculate_vf(self, lnc_c0, t):
        """"
        :return: area of the screen filter
        """
        try:
            if t == 0:
                # As the first time step is always zero a small noise is added to avoid division by zero
                return -1 * self.viw*lnc_c0 / self.alpha / self.f / 0.000001
            else:
                return -1 * self.viw * lnc_c0 / self.alpha / self.f / t
        except TypeError:
            logging.warning("non numeric data ; returning Vf = np.NaN")
            return np.nan
