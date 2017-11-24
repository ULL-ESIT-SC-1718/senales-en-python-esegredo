import numpy as np
import matplotlib.pyplot as plt

t=np.arange(0.,1.,1./44100.)

y = np.cos(2*np.pi*t)*np.exp(-t**2)

plt.plot(t,y)
plt.show()
