###  Optical Filter Spectrum Simulation
Models an idealized, step-function transmission profile for a custom dual-band optical filter across the electromagnetic spectrum from $0$ to $20\text{ }\mu\text{m}$.

* **Mathematical Approach:** Piecewise logic mapping over discrete NumPy grids.
* **Key Insight:** Simulates an optical element that blocks high-energy wavelengths (X-rays/UV) entirely, allows high transmission ($80\%$) in the optical window ($0.3 - 1.0\text{ }\mu\text{m}$), and a lower transmission ($20\%$) inside a band of longer infrared/radio wavelengths ($10.0 - 20.0\text{ }\mu\text{m}$).
