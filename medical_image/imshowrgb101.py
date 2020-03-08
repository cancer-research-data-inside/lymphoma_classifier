import matplotlib.pyplot as plt
import numpy as np

n = 4

#create a 3-dimensional numpy array with randomly selected RGB coordinates
a = np.random.random((n,n,3))


plt.figure(figsize=(11,3))

plt.subplot(141)
r = a.copy()
r[:,:,[1,2]] = 0    #set green and blue coordinates to 0; this will display reds only
plt.yticks(range(n))
plt.xticks(range(n))
plt.title('Red component')
plt.imshow(r, interpolation='nearest')

plt.subplot(142)
g = a.copy()
g[:,:,[0,2]] = 0    #set red and blue coordinates to 0 to show greens
plt.xticks(range(n))
plt.yticks([])
plt.title('Green component')
plt.imshow(g, interpolation='nearest')

plt.subplot(143)
b = a.copy()
b[:,:,[0,1]] = 0    #set red and green coordinates to 0 to show blues
plt.yticks([])
plt.xticks(range(n))
plt.title('Blue component')
plt.imshow(b, interpolation='nearest')

plt.subplot(144)
plt.xticks(range(n))
plt.yticks([])
plt.title('RGB mixture')
plt.imshow(a, interpolation='nearest')

plt.show()
