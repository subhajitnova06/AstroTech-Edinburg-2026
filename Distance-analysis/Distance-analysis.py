import numpy as np
import matplotlib.pyplot as plt

# Relative distance factors (not parsecs, not Andromeda data)
distance = np.array([1.0, 2.0, 5.0, 10.0, 20.0])

angular_size = 1.0 / distance
flux = 1.0 / distance**2

angular_size /= angular_size[0]
flux /= flux[0]

plt.figure(figsize=(10, 6))
plt.plot(distance, angular_size, "o-", color="tab:blue", label=r"Angular size $\propto 1/d$")
plt.plot(distance, flux, "o--", color="tab:green", label=r"Flux $\propto 1/d^2$")

plt.title("Toy model: angular size and flux vs relative distance")
plt.xlabel("Relative distance")
plt.ylabel("Value relative to the nearest point")
plt.legend()
plt.grid(True, linestyle=":", alpha=0.6)
plt.tight_layout()
plt.show()
