import numpy

chi_cubed = [30.7, 20.22, 12.58, 6.91, 3.32, 1.343, 0.3685]
chi = []

for i in range(len(chi_cubed)):
	chi.append(chi_cubed[i]**(1/3))

print("4GeV_chi: ")
print(chi)
