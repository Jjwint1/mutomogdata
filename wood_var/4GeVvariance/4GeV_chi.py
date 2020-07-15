import numpy

chi_cubed = [22.2, 14.3, 8.95, 4.94, 2.44, 0.99, 0.275, 0.029]
chi = []

for i in range(len(chi_cubed)):
	chi.append(chi_cubed[i]**(1/3))

print("Chi_4GeV: ")
print(chi)
