import numpy as np
import matplotlib.pyplot as plt

# Wavelength grid (microns)
wavelength = np.linspace(0, 20, 400)

# Transmission array initialized to 0
T = np.zeros_like(wavelength)

# Optical pass: narrow peak from 0.3 to 1 micron at 0.8
T[(wavelength >= 0.3) & (wavelength <= 1.0)] = 0.8

# Radio pass: from 10 to 20 microns at 0.2
T[(wavelength >= 10.0) & (wavelength <= 20.0)] = 0.2

plt.figure(figsize=(8, 6))
plt.plot(wavelength, T, linewidth=2)

plt.title('X-ray blocked, Radio + Optical pass', fontsize=18)
plt.xlabel('Wavelength (microns)', fontsize=14)
plt.ylabel('Transmission', fontsize=14)

plt.xlim(0, 20)
plt.ylim(0, 0.85)

plt.tight_layout()
plt.show()
