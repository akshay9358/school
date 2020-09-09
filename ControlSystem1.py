import sympy as sym
from sympy.abc import s,t,x,y,z
from sympy.integrals import laplace_transform
from sympy.integrals import inverse_laplace_transform
#import sympy.physics.units as units
import matplotlib.pyplot as plt
import numpy as np
import math

# Laplace transform (t->s)
F1 = laplace_transform(4*sym.sqrt(2)*(t**2)*(sym.cos(3*t)) - 4*sym.sqrt(2)*(t**2)*(sym.sin(3*t)), t, s)
print('F1')
print(F1[0])
# Result: 8*sqrt(2)*(-9*s**2 - s*(27 - s**2) + 27)/(s**2 + 9)**3


# Laplace transform (t->s)
F2 = laplace_transform(1.5*t*sym.exp(-2*t)*(sym.sin(4*t)) + 1.5*t*sym.exp(-2*t)*sym.sqrt(3)*(sym.cos(4*t)), t, s)
print('F2')
print(F2[0])
# Result: (12.0*s + sqrt(3)*(1.5*(s + 2)**2 - 24.0) + 24.0)/((s + 2)**2 + 16)**2


f = 10  # Frequency, in cycles per second, or Hertz
f_s = 100  # Sampling rate, or number of measurements per second

s = np.linspace(0, 2, 2 * f_s, endpoint=False)
x = 8*np.sqrt(2)*(-9*s**2 - s*(27 - s**2) + 27)/(s**2 + 9)**3
y = (12.0*s + np.sqrt(3)*(1.5*(s + 2)**2 - 24.0) + 24.0)/((s + 2)**2 + 16)**2
fig, ax = plt.subplots()
ax.plot(s, x)
ax.set_xlabel('S')
ax.set_ylabel('F1(s)');

plt.show()

fig, ax = plt.subplots()
ax.plot(s, -y)
ax.set_xlabel('S')
ax.set_ylabel('F2(s)');

plt.show()



