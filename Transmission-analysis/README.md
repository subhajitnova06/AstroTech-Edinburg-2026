# Schematic atmospheric windows

Ground-based astronomy is limited by Earth's atmosphere. This script is a **labelled cartoon**, not a HITRAN / radiative-transfer calculation.

What the original workshop sketch got wrong, and what this version states instead:

- **0.3–0.9 μm** — optical window (high transmission).
- **~1.5–2.4 μm, 3–5 μm, 8–13 μm** — infrared windows (water and CO2 still eat other IR bands).
- **10–20 μm is mid-infrared, not radio.** Radio windows start at millimetre-to-metre wavelengths (\(\sim 10^4\) μm and longer).
- UV and X-rays are blocked from the ground; that is why those telescopes fly in space.

```bash
python Transmission-analysis.py
```
