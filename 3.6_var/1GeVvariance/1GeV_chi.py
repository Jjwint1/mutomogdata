import numpy

chi_cubed = [0.401, 0.157, 0.04]
chi = []

for i in range(len(chi_cubed)):
	chi.append(chi_cubed[i]**(1/3))

print("1GeV_chi: ")
print(chi)
