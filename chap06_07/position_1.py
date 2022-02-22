from turtle import color
import matplotlib.pyplot as plt
from matplotlib import patches
import numpy as np
import math

th = np.linspace(0, 2*np.pi, 1000)
r=1
c=r*np.cos(th)
d=r*np.sin(th)
figure, axes = plt.subplots(1)

axes.plot(c,d)
axes.set_aspect(1)

plt.title("sensor position")
plt.plot(1,0,'o',color="blue",)
plt.plot(0.6234898,0.78183148,'o',color="blue")
plt.plot(-0.22252093,0.97492791,'o',color="blue")
plt.plot(-0.90096887,0.43388374,'o',color="blue")
plt.plot(-0.90096887,-0.43388374,'o',color="blue")
plt.plot(-0.22252093,-0.97492791,'o',color="blue")
plt.plot(0.6234898,-0.78183148,'o',color="blue")
plt.plot(c,d,color="red")
plt.plot([0,1],[0,0],color="red")
plt.show()
