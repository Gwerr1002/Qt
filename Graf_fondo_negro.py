# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 20:55:06 2022

@author: gerard
"""
import numpy as np
import scipy.signal as sp
import matplotlib.pyplot as plt

xi = [0.05, 0.2, 0.5, 2**(-1/2), 1, 1.6, 2.4]
xi = np.array(xi)
L, C = 100e-6, .1e-9
R = 2*np.sqrt(L/C)*xi

Sys = [([1],[L*C, C*Ri, 1]) for Ri in R] #Systemas
wr = np.sqrt(1-2*xi**2)/np.sqrt(L*C)
Max = 20*np.log10(1/(2*xi*np.sqrt(1-xi**2))) #Maximo de la respuesta en frecuencia
Tp = np.pi*np.sqrt(L*C)/np.sqrt(1-xi**2) #Momento del maximo pico en la respuesta al escalon
P = 1 + np.exp(-xi*np.pi/np.sqrt(1-xi**2)) #Pico de la respuesta al escalon

#%%
#---------------------------------------------------------------
#                     respuesta al escalon
#---------------------------------------------------------------
t = np.linspace(0, 2e-6,1000)
StepResp = [sp.step(H, T = t) for H in Sys]

fig, ax = plt.subplots(facecolor = '#3C3D3D')
ax.set_facecolor('#272928')


puntos = np.transpose([Tp,P])
puntos = ["({:.2e},{})".format(p[0],round(p[1],2)) for p in puntos]

ax.scatter(Tp,P, color = '#2DC291')
for i, label in enumerate(puntos):
    ax.text(Tp[i], P[i],label, color = "#929493", fontsize=12)
    
i = 0
for t,y in StepResp:
    ax.plot(t,y, label = "{}".format(round(xi[i],3)))
    i += 1

ax.set_title("Respuesta al escalón", color = '#929493', fontsize=15)
ax.set_xlabel('$t_{seg}$', color = '#929493',fontsize=12)
ax.set_ylabel('$V_{o}(t)$', color = '#929493',fontsize=12)
ax.grid(linestyle = ':', color = '#929493')
ax.legend(title="$ξ$")
ax.tick_params(labelcolor='#929493')
plt.show()

#%%

#---------------------------------------------------------------
#                     respuesta a entrada senoidal
#---------------------------------------------------------------

t = np.linspace(0,20*np.pi,1000)
w = [10**5, 10**7, 10**8]

for W in w:
    
    fig1, ax = plt.subplots(facecolor = '#3C3D3D')
    ax.set_facecolor('#272928')
    
    y = np.sin(t)
    ax.plot(t/W,y, label = "$Vin$", linestyle = ':')
    T, y, x = sp.lsim(Sys[1],y,t/W)
    ax.plot(T,y, label = "$Vo$")
    
    ax.set_title("Respuesta a entrada senoidal $\omega =$ {:.2e} rad/seg y $ξ = 0.2$".format(W), color = '#929493', fontsize=15)
    ax.set_xlabel('$t_{seg}$', color = '#929493', fontsize=12)
    ax.set_ylabel('$V(t)$', color = '#929493',fontsize=12)
    ax.grid(linestyle = ':', color = '#929493')
    ax.legend()
    ax.tick_params(labelcolor='#929493')
    plt.show()

#%%

#---------------------------------------------------------------
#                     respuesta en frecuencia
#---------------------------------------------------------------
w = np.logspace(4,10,1000)
FreqResp = [sp.freqresp(H,w) for H in Sys]
fig2, ax = plt.subplots(facecolor = '#3C3D3D')
ax.set_facecolor('#272928')

puntos = np.transpose([wr,Max])
puntos = ["({:.2e},{})".format(p[0],round(p[1],2)) for p in puntos]

ax.scatter(wr,Max, color = '#2DC291')

for i, label in enumerate(puntos):
    ax.text(wr[i], Max[i],label, color = "#929493", fontsize=12)

i=0
for w, H in FreqResp:
    ax.semilogx(w,20*np.log10(abs(H)), label = '{}'.format(round(xi[i],3)))
    i += 1

ax.set_title("Magnitud", color = '#929493',fontsize=15)
ax.set_xlabel('$\omega_{rad/seg}$', color = '#929493',fontsize=12)
ax.set_ylabel('$|H(j\omega)|_{dB}$', color = '#929493',fontsize=12)
ax.grid(linestyle = ':', color = '#929493')
ax.legend(title="$ξ$")
ax.tick_params(labelcolor='#929493')
ax.axis([6e5,2e8,-50,30])
plt.show()

fig3, ax = plt.subplots(facecolor = '#3C3D3D')
ax.set_facecolor('#272928')
i=0
for w, H in FreqResp:
    ax.semilogx(w,np.angle(H)*180/np.pi, label = '{}'.format(round(xi[i],3)))
    i +=1

ax.set_title("Fase", color = '#929493',fontsize=15)
ax.set_xlabel('$\omega_{rad/seg}$', color = '#929493',fontsize=12)
ax.set_ylabel('$\phi(j\omega)_{deg}$', color = '#929493',fontsize=12)
ax.grid(linestyle = ':', color = '#929493')
ax.legend(title="$ξ$")
ax.tick_params(labelcolor='#929493')
plt.show()
