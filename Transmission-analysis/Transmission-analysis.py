import numpy as np
import matplotlib.pyplot as plt

# Wavelength in microns. This is a schematic, not a radiative-transfer model.
wavelength = np.linspace(0.1, 25.0, 2000)
T = np.zeros_like(wavelength)


def set_window(wmin, wmax, height):
    mask = (wavelength >= wmin) & (wavelength <= wmax)
    T[mask] = np.maximum(T[mask], height)


# Optical window
set_window(0.3, 0.9, 0.85)
# Near-IR water-vapour gaps
set_window(1.5, 1.8, 0.55)
set_window(2.0, 2.4, 0.50)
# Mid-IR windows used in ground-based astronomy
set_window(3.0, 5.0, 0.45)
set_window(8.0, 13.0, 0.50)
# 10-20 um is thermal IR, NOT radio. Radio is cm--m wavelengths.

plt.figure(figsize=(9, 5))
plt.plot(wavelength, T, lw=2, color="steelblue")
plt.axvspan(0.3, 0.9, alpha=0.12, color="C0", label="Optical")
plt.axvspan(8.0, 13.0, alpha=0.12, color="C1", label="N-band IR")
plt.title("Schematic: Earth's atmospheric windows (ground-based)")
plt.xlabel("Wavelength (\u03bcm)")
plt.ylabel("Relative transmission")
plt.xlim(0.1, 25.0)
plt.ylim(0.0, 1.0)
plt.legend()
plt.grid(True, linestyle=":", alpha=0.5)
plt.tight_layout()
plt.show()
