import matplotlib.pyplot as plt
import numpy as np


distance = np.array([1, 2, 5, 10, 20])


angular_size = 1 / distance
flux = 1 / distance**2


angular_size /= angular_size[0]
flux /= flux[0]


plt.figure(figsize=(10, 6))
plt.plot(distance, angular_size, 'o-', color='blue', label='Angular Size')
plt.plot(distance, flux, 'o--', color='green', label='Flux')


plt.title("Andromeda: Linear size & brightness vs Distance")
plt.xlabel("Distance Factor")
plt.ylabel("Relative value")
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)

plt.show()
