import sys
sys.path.insert(0, 'C:\\Users\\rsjon_000\\Documents\\pyfluv')
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

import time
##########

import pyfluv


eco = pyfluv.eco71()
eco.qplot('Bankfull width')
eco.trend('Bankfull width')