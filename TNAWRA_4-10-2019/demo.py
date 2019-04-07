import sys
sys.path.insert(0, 'C:\\Users\\rsjon_000\\Documents\\pyfluv')
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

import time
##########

import pyfluv

survey = pyfluv.StreamSurvey(r'C:\Users\rsjon_000\Documents\pyfluv\pyfluv\Data\myr5_survey_adjusted.csv')
crosses = survey.get_cross_objects()
pros = survey.get_profile_objects()

plt.figure()
crosses[5].qplot()
plt.figure()
crosses[5].planplot()

plt.figure()
pros[2].qplot(showFeatures=True)
plt.figure()
pros[2].planplot(showFeatures=True)