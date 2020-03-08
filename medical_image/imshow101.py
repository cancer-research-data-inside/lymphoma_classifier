import matplotlib.pyplot as plt
import numpy as np

n = 2

# create an nxn numpy array
a = np.reshape(np.linspace(0,1,n**2), (n,n))

plt.figure(figsize=(12,4.5))

#use imshow to plot the array
plt.subplot(141)
plt.imshow(a,                         #numpy array generating the image
           cmap = 'gray',             #color map used to specify colors
           interpolation='nearest'    #algorithm used to blend square colors; with 'nearest' colors will not be blended
          )
plt.xticks(range(n))
plt.yticks(range(n))
plt.title('Gray color map, no blending', y=1.02, fontsize=12)

#the same array as above, but with different color map
plt.subplot(142)
plt.imshow(a, cmap = 'viridis', interpolation='nearest')
plt.yticks([])
plt.xticks(range(n))
plt.title('Viridis color map, no blending', y=1.02, fontsize=12)

#the same array as above, but with blending
plt.subplot(143)
plt.imshow(a, cmap = 'viridis', interpolation='bicubic')
plt.yticks([])
plt.xticks(range(n))
plt.title('Viridis color map, bicubic blending', y=1.02, fontsize=12)

#the same array as above, but with blending
plt.subplot(144)
plt.imshow(a, cmap = 'gray', interpolation='bicubic')
plt.yticks([])
plt.xticks(range(n))
plt.title('gray color map, bicubic blending', y=1.02, fontsize=12)

plt.show()
