import matplotlib.pyplot as plt
import numpy as np
from map import *

a=np.linspace(0,6*np.pi,30)
x,y=np.meshgrid(a,a)
f=np.cos(x)+np.cos(y)
name_list=['Diana','Bloom','Normal','Donkey']

plt.rcParams.update({'font.size': 10})
fig,axes=plt.subplots(2,2,figsize=(8,7))
plt.subplots_adjust(top=0.9, bottom=0.1, right=0.9, left=0.1,
                    hspace=0.3, wspace=0.25)
for index,name in enumerate(name_list):
    ax1=axes[index%2,index//2]
    pic1=ax1.contourf(x/np.pi,y/np.pi,f,cmap=Diana_cmap(name),
                    levels=np.linspace(-2,2,15))
    bar1=plt.colorbar(pic1)
    bar1.ax.set_title(r'$f(x,y)$')
    bar1.set_ticks([-2,0,2])
    bar1.set_ticklabels([-2,0,2])
    ax1.set_xlabel(r'$x/\pi$')
    ax1.set_ylabel(r'$y/\pi$')
plt.show()