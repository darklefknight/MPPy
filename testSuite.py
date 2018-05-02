from BCO.Instruments import Radar
from BCO.Instruments import Windlidar
from BCO.Instruments import Radiation
from BCO.Instruments import SfcWeather
from BCO.Instruments import Ceilometer
import BCO

from BCO.tools import tools
# from BCO.Quicklooks import plot_RadarLidarVelcities

import numpy as np
from datetime import datetime as dt
import matplotlib.pyplot as plt
from netCDF4 import Dataset


# def testRadar():
#     # coral  = Radar(start="20140813092350",end="20140913000050", device="KATRIN")
#     coral = Radar(start="20180212",end="20180212", device="CORAL")
#     ref = coral.getReflectivity(postprocessing="Ze")
#     vel = coral.getVelocity()
#     time = coral.getTime()
#     range = coral.getRange()
#     coral.quickplot2D(ref,ylim=(100,2000))


if __name__ == "__main__":
    # FTP-settings:

    # BCO.settings.set_ftp(True)
    # BCO.settings.path_to_ftp_file("/home/tobias/Documents/ftp_access.txt")
    # BCO.settings.path_to_ftp_file("/home/mpim/m300517/ftp_access.txt",verbose=True)
    # BCO.settings.path_to_ftp_file("C:/Users/darkl/PycharmProjects/BCO/BCO/ftp_access.txt")


    # working devices:
    #
    # Rad = Radiation("20180101","20180101")
    # Wx = SfcWeather("20180101","20180101")
    # coral = Radar("20180101","20180101",device="CORAL")
    # lidar = Windlidar("20180401","20180401") #seems to work with data version 1.01!


    #not working devices:

    for i in tools.daterange(dt(2017,3,1),dt(2018,7,1),step="month"):
        print(i)


    ceilo = Ceilometer("20180102","20180201") # can not work yet as the data is not there.
