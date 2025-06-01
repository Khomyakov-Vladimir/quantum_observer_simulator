# cognitive_dimension.py

import os
import numpy as np
import matplotlib.pyplot as plt

def cognitive_dimension(d_real, d_imag):
    d = np.abs(complex(d_real, d_imag))
    return 2 / (1 + d**2)

# Ensure the 'results' directory exists
os.makedirs("results", exist_ok=True)

# Visualization
d_values = np.linspace(0, 1, 100)
dim_values = [cognitive_dimension(d, 0) for d in d_values]

plt.figure(figsize=(10, 6))
plt.plot(d_values, dim_values, 'b-')
plt.axvline(x=1/4.6, color='r', linestyle='--', label='Critical |d| = 1/Λ_c')
plt.xlabel(r'$|\langle \mathrm{obs}_0 | \mathrm{obs}_1 \rangle|$')
plt.ylabel(r'dim $\mathcal{C}_{\mathrm{obs}}$')
plt.title('Cognitive dimension vs. distinguishability')
plt.legend()
plt.grid(True)

# Save in high resolution and vector format to 'results' directory
plt.savefig("results/cognitive_dimension.png", dpi=600, bbox_inches='tight')
plt.savefig("results/cognitive_dimension.pdf", bbox_inches='tight')
plt.show()
