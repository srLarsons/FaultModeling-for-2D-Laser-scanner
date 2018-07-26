import numpy as np
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt

# 1. read the data
# -----------------------
# for this purpose I
#   - ignored the headline (skip_header)
#   - changed all "," to "."
# you should define a ";" as delimiter for your csv files, this is
# more clear than a ","

from numpy import genfromtxt
datafile = 'white_wall_avarage.csv'
data = genfromtxt(datafile,
                   delimiter=',',
                   skip_header = 1)

# first question why do we have so many columns. Do to the
# resolution of the scanner I expected to find 60 or 70 but not
# 400
print data.shape

# 2.  Elimiating first column (distance information)
# -----------------------
data = np.delete(data, 0, 1)
print data.shape

# 3. Eliminate disturbances
# -----------------------
# Why do we have to consider outliers at some positions?
print data[data>10]
data[data>10] = np.nan

# 4. Plot matrix
# THIS VALUE HAS TO BE ADAPTED TO THE MAXIMUM VALUE THE EVER OCCURS. IT IS
# NECCESSARY FOR SIMILAR SCALING OF ALL IMAGES
vmax = 4

ylabels = ["2", "2.5", "3", "3.5", "4", "4.5", "5", "5.5", "6", "6.5",
     "7", "7.5", "8", "9", "10", "11", "12", "15", "22", "32",
     "52", "72", "102"]
xlabels = ["-80", "0", "80"]

data = np.flipud(data)
ax = sns.heatmap(data, vmin=0, vmax=vmax)
ax.set(yticklabels = ylabels)
plt.yticks(rotation=0)

plt.xticks([0, 215, 429])
ax.set(xticklabels = xlabels)
plt.title(datafile)
plt.xlabel("angle in degree")
plt.ylabel("distance in cm")
plt.show()
