import numpy

chi_cubed = [5.7, 2.25, 0.62, 0.045]
chi = []

for i in range(len(chi_cubed)):
	chi.append(chi_cubed[i]**(1/3))

print("Chi_1GeV: )
print(chi)
