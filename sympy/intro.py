# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 22:31:29 2024

@author: gerard
"""

import numpy as np
import sympy as sym

#%%Crear símbolos

s,x,y = sym.symbols("s x y")
expr = x+2*y

print(x**expr)

#%% Derivar e Integrar

x,t,z,nu = sym.symbols("x t z nu")
f1 = sym.sin(x)*sym.exp(x)
d = sym.diff(f1,x) #derivada

inte = sym.integrate(sym.sin(x**2),(x,-sym.oo, sym.oo))

#%% Límites

lim = sym.limit(sym.sin(x)/x,x,0)

#%% Matrices

mat1 = sym.Matrix([[1,2],[2,2]])
print(mat1.det()) #determinante
print(mat1.rref()) #matriz en su forma reducida
print(mat1**-1) #matriz inversa

R = sym.Matrix([[8,-4],[4,-8]])
V = sym.Matrix([9,-1])
I = R**-1*V

R1,R2,R3 = sym.symbols("R1 R2 R3")
Rmat = sym.Matrix([[R1,R2],[-R2,R2+R3]])


#%% imprimir con latex

sym.latex(sym.Integral(sym.cos(x)**2, (x, 0, sym.pi)))
#%%Transformada de laplace

lap = sym.laplace_transform(t**4, t, s)

#%% Graficas
x, y = sym.symbols('x, y')
sym.plot_implicit(y > x**2)
#%%
sym.plot((x**2, (x, -6, 6)), (x, (x, -5, 5)))
#%%x+y=1
sym.plot_implicit(sym.Eq(x + y, 1))
#%%
sym.plotting.plot3d(x + y, (x, -5, 5), (y, -5, 5))