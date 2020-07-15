import matplotlib.pyplot as plt
import numpy as np

constrained_vars = []
unconstrained_vars = []
unconstrained_vars_trunc = []
bridged_vars = []
depths = range(0, 110, 10)

u_vars = open("500GeVunconstrainedVars.txt", "r")
for item in u_vars:
    unconstrained_vars.append(float(item))

for i in range(len(unconstrained_vars)):
    if (i < 11):
        unconstrained_vars_trunc.append(unconstrained_vars[i])

c_vars = open("500GeVconstrainedVars_100cm.txt", "r")
for item in c_vars:
    constrained_vars.append(float(item))

unconstrained_vars_rev = list(reversed(unconstrained_vars_trunc))

for i in range(len(unconstrained_vars_trunc)):
    bridged_vars.append(unconstrained_vars_trunc[i]*unconstrained_vars_rev[i]/0.0000125)




plt.plot(depths, bridged_vars, '+g')
plt.plot(depths, constrained_vars, '+r')
plt.show()


