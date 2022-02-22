from turtle import color
import matplotlib.pyplot as plt
from matplotlib import patches
import numpy as np
import math

th = np.linspace(0, 2*np.pi, 1000)
x=np.linspace(0, 2*np.pi, 7, endpoint=False)
r=1
c=r*np.cos(th)
d=r*np.sin(th)
e=r*np.cos(x)
f=r*np.sin(x)
figure, axes = plt.subplots(1)

axes.plot(c,d,e,f)
axes.set_aspect(1)



plt.plot(c,d,color="red")
plt.plot(e,f,color="blue")
plt.plot([0,1],[0,0],color="red")
plt.show()
