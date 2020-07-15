import numpy

chi_cubed = [0.485, 0.327, 0.204, 0.1175, 0.0572, 0.021]
chi = []

for i in range(len(chi_cubed)):
	chi.append(chi_cubed[i]**(1/3))

print("4GeV_chi: ")
print(chi)
