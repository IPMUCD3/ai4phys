#this program loads data from Nagele et al. 2023ApJ...947...30N
#   c.f. Sec. 3.2, Fig. 1, Fig. 7 (2nd panel) and Fig. 9

import numpy as np
import matplotlib.pyplot as plt

#load data from file
data = np.load('QSO_SFG_data.npy',allow_pickle=True)
images = data[1]
labels = data[0,:,0:9,0,0]

#labels
#for each image in the dataset, there are 9 labels:
#   0 --- 0 if SFG, 1 if QSO
#   1 --- RA
#   2 --- DEC
#   3 --- redshift
#   4 --- i magnitude
#   5 --- Log half light radius
#   6 --- Log stellar mass 
#   7 --- ellipticity
#   8 --- dimensionality of original cutout (Li et al. 2021ApJ...918...22L)
print ()
print ('here are the labels for the first image in the dataset:')
print ()
print (labels[0])
print ()

#images
#images are 40x40 pixels with a single channel, values varying between 0 and 1
cmap = 'coolwarm'
for i in range(50):
    plt.subplot(5,10,i+1)    
    plt.imshow(images[i,:,:,0],cmap=cmap,vmin = 0.0,vmax=1.0)
    plt.axis('off')

plt.show()
