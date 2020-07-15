import numpy

chi_cubed = [0.104, 0.038]
chi = []

for i in range(len(chi_cubed)):
	chi.append(chi_cubed[i]**(1/3))

print("1GeV_chi: ")
print(chi)
