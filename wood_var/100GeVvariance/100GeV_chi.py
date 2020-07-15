import numpy

chi_cubed = [0.0644, 0.0495, 0.0345, 0.0231, 0.0146, 0.00856, 0.00447, 0.00198, 0.000608, 0.000081]
chi = []

for i in range(len(chi_cubed)):
	chi.append(chi_cubed[i]**(1/3))

print("Chi_100GeV: ")
print(chi)
