import numpy

chi_cubed = [0.00338, 0.00234, 0.001605, 0.00109, 0.000688, 0.000402, 0.000211, 0.0000904, 0.0000261]
chi = []

for i in range(len(chi_cubed)):
	chi.append(chi_cubed[i]**(1/3))

print("500GeV_chi: ")
print(chi)
