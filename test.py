import matplotlib.pyplot as plt
import numpy as np

# Spannungs- und Stromdaten
U = [0, 0.1, 0.2, 0.3, 0.5, 0.7, 1.3, 3.2, 5.2, 7.2, 9.2, 11.2, 13.2, 15.2, 19.1, 21.1]  # Spannung in V
I = [-0.03e-9, 10e-9, 135.2e-9, 1.628e-6, 1.68e-6, 1.7591e-3, 3.668e-3, 12e-3, 22e-3, 32.56e-3, 
     42.37e-3, 52.282e-3, 62.136e-3, 72.06e-3, 91.87e-3, 101.81e-3]  # Strom in A

# Umwandeln der Stromwerte in ihren natürlichen Logarithmus
I_log = np.log10(np.abs(I))  # Logarithmus des Stroms

# Plot erstellen
plt.figure(figsize=(8, 6))
plt.plot(U, I_log, marker='o', linestyle='-', color='b', label="log(I) vs. U_{pn}")
plt.xlabel("Spannung U_{pn} (V)", fontsize=12)
plt.ylabel("log(I) (log(A))", fontsize=12)
plt.title("Logarithmische Strom-Spannungs-Kurve der Diode", fontsize=14)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.axhline(0, color='black', linewidth=0.8)  # Null-Linie für y
plt.axvline(0, color='black', linewidth=0.8)  # Null-Linie für x
plt.legend()
plt.show()
