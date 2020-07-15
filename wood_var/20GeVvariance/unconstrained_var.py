import matplotlib.pyplot as plt
import numpy as np

unconstrained_vars = []

depths = range(0, 1010, 10)

u_vars = open("20GeVunconstrainedVars.txt", "r")
for item in u_vars:
    unconstrained_vars.append(float(item))

coeffs = np.polyfit(depths, unconstrained_vars, 3)

model = [coeffs[0]*depth**(3) for depth in depths]




plt.plot(depths, unconstrained_vars, '+b', label='GEANT4 data')
plt.plot(depths, model, '-r', label=f'{coeffs[0]:.3e}'+r'$\cdot d^{3}$')
plt.title(r'Variance of muon trajectories at $E = 20$GeV, $\rho=0.6$ kg m$^{-3}$')
plt.xlabel(r'depth / cm')
plt.ylabel(r'$\sigma^2$ / cm$^2$')
plt.legend()
plt.savefig('unconstrainedVariance.png', dpi=600)
plt.show()