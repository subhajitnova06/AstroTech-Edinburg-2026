### Optical Filter Spectrum Simulation
Models a step-function transmission profile for a custom dual-band optical filter across the electromagnetic spectrum from $0$ to $20\text{ }\mu\text{m}$.

* **Concept:** Multi-band Pass Filtering
* **Key Insight:** Demonstrates how step-functions are applied to numpy arrays to simulate idealized optical components. The filter profile blocks high-energy wavelengths (X-rays/UV) entirely, permits high transmission ($80\%$) in the optical window, and lower transmission ($20\%$) in the longer infrared/radio window.

#### Running this Simulation
```bash
python 03_Optical_Filter/optical_filter.py
