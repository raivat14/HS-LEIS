#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 17:01:50 2020

@author: raivat
"""


import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
import re

s = pd.read_csv('Edit_This.csv') # reads the .csv file can be found in dropbox > shared manuscripts > Ravi Ben MoOx Nucleation and LEIS > Figures

xmin = 750 # Change these bounds as needed
xmax = 2800 
ymin = 0
ymax = 32

y_axis_columns = s.columns[1:] # Reads column data to plot y values from index 1 onwards

for col_name in y_axis_columns: # Loop to plot all columns until it finds an empty one
   plt.plot(s.energy,s[col_name], label=col_name)
   plt.tight_layout()
   from matplotlib.ticker import MaxNLocator
   axes = plt.gca()
   axes.yaxis.set_major_locator(MaxNLocator(integer=True))
   axes.set_xlim([xmin,xmax])
   axes.set_ylim(ymin,ymax)
   plt.xlabel('Energy (eV)', fontsize=12) # Edit as needed
   plt.ylabel('Intensity (counts/nC)', fontsize=12) 
   plt.legend(loc='upper center', fontsize=10) # Defines legend formatting
   plt.annotate('O', # These define the labels, must be adjusted for each plot
                xy=(1150, 13),
                xytext=(1135, 22))
   plt.annotate('Al',
                xy=(1675, 7),
                xytext=(1700, 10))
   plt.annotate('Mo',
                xy=(2450, 12),
                xytext=(2450, 30))
   plt.savefig("6_Sputter1_5-222cyc_SiOx.png", dpi = 1200) # Edit export file name and DPI here
plt.show()

# This section below saves a copy of your current script so you can edit the figure in the future
# To avoid saving un-needed files, comment everything below out until you are happy with your figure (ctrl +1)

# filename = '6_Sputter1_5-222cyc_SiOx' # Adjust what you want this to be
# timestamp = str(dt.datetime.now())[:19] # No need to mess with anything here or below. These lines add a date and time to the saved text file
# timestamp = re.sub(r'[\:-]','',timestamp)
# timestamp = re.sub(r'[\s]','_',timestamp)
# print('{}_{}'.format(filename,timestamp))
# out_filename = ('{}_{}'.format(filename,timestamp))

# with open(__file__,'r') as f:
#     with open(out_filename,'w') as out:
#         for line in (f.readlines()[:-14]):
#             print(line,end='',file=out)
