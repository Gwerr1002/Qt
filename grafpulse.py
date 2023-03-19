# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt

c = np.append(np.zeros(249),np.ones(150))
c = np.append(c,np.zeros(100))
c = np.append(c,np.append(-np.ones(150),np.zeros(249)))
c = np.append(c,c)

fig, ax = plt.subplots(facecolor = '#3C3D3D')
ax.set_facecolor('#272928')
ax.axvline(255,linestyle = "--",color = "gray",linewidth = .8)
ax.axvline(1150,linestyle = "--",color = "gray",linewidth = .8)
ax.axvline(500,linestyle = "--",color = "gray",linewidth = .8)
ax.axhline(1,linestyle = "--",color = "gray",linewidth = .8)
ax.plot(c,color='g',linewidth = 3)
ax.set_xlabel('$tiempo$', color = '#929493',fontsize=12)
ax.set_ylabel('$Corriente$', color = '#929493',fontsize=12)
ax.grid(linestyle = ':', color = '#929493')
ax.set_ylim(-1.5,1.5)
plt.xticks([])
plt.yticks([])
plt.text(410,.25,"$100\mu s$",color = 'w')
plt.text(280,.8,"Ancho", color='w')
plt.text(300,.7,"de",color = 'w')
plt.text(280,.6,"pulso",color = 'w')
plt.text(10,.5,"Amplitud",color= 'w')
plt.text(45,.4,"del",color = 'w')
plt.text(35,.3,"pulso",color='w')
plt.text(660,-1.2,"msi",color='w')
ax.annotate("", xy=(150, 1), xytext=(150, 0), 
            arrowprops=dict(arrowstyle="<->",color = '#117FC7'))
ax.annotate("", xy=(395, .940), xytext=(255, .940), 
            arrowprops=dict(arrowstyle="<->",color = '#117FC7'))
ax.annotate("", xy=(395, .940), xytext=(255, .940), 
            arrowprops=dict(arrowstyle="<->",color = '#117FC7'))
ax.annotate("", xy=(500, .10), xytext=(405, .10), 
            arrowprops=dict(arrowstyle="<->",color = '#117FC7'))
ax.annotate("", xy=(1150, -1.10), xytext=(255, -1.10), 
            arrowprops=dict(arrowstyle="<->",color = '#117FC7'))
plt.show()
