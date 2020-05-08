#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 17:01:50 2020

@author: raivat
"""


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

s = pd.read_csv('test2.csv') # reads the .csv file

xmin = 750 # Change these bounds as needed
xmax = 2800 
ymin = 0
ymax = 16

y_axis_columns = s.columns[1:] # Reads column data to plot y values from index 1 onwards

for col_name in y_axis_columns: # Loop to plot all columns until it finds an empty one
   plt.plot(s.energy,s[col_name], label=col_name)
   plt.tight_layout()
   axes = plt.gca()
   axes.set_xlim([xmin,xmax])
   axes.set_ylim(ymin,ymax)
   plt.xlabel('Energy (eV)') # Edit as needed
   plt.ylabel('Intensity (counts/nC)')
   plt.title('Al2O3 5cyc Spot1') 
   plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=10) # Defines legend formatting
   plt.annotate('O', # These define the labels, must be adjusted for each plot
                xy=(1150, 14),
                xytext=(1150, 14))
   plt.annotate('Al',
                xy=(1675, 13),
                xytext=(1675, 13))
   plt.annotate('Mo',
                xy=(2500, 9),
                xytext=(2500, 9))
   plt.savefig("test2.png", dpi = 600) # Edit export file name and DPI here
plt.show()