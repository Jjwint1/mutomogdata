import numpy

chi_cubed = [1.411, 1.043, 0.737, 0.494, 0.315, 0.181, 0.091, 0.037, 0.0085]
chi = []

for i in range(len(chi_cubed)):
	chi.append(chi_cubed[i]**(1/3))

print("Chi_20GeV: ")
print(chi)
