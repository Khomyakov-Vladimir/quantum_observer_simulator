# QuantumObserverSimulator.py

import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

class QuantumObserverSimulator:
    def __init__(self, d_real=0.0, d_imag=0.0, p_err=0.0):
        self.d = complex(d_real, d_imag)
        self.p_err = p_err
        
    def effective_distinguishability(self):
        return np.abs(self.d) * (1 - 2*self.p_err)
    
    def p_collapse_unitary(self, lambda_c=4.6):
        eff_d = self.effective_distinguishability()
        return 1.0 if eff_d < 1/lambda_c else 0.0
    
    def interference_pattern(self, N=1000):
        p0_unitary = 0.5 * (1 + self.d.real)
        p0_effective = p0_unitary * (1 - self.p_err) + (1 - p0_unitary) * self.p_err
        results = binom.rvs(1, p0_effective, size=N)
        return np.mean(results), np.std(results)/np.sqrt(N)
    
    def phase_transition_analysis(self, lambda_values, N_exp=1000):
        results = []
        for lam in lambda_values:
            self.d = complex(1/lam, 0)
            p_mean, p_err = self.interference_pattern(N_exp)
            results.append((p_mean, p_err))
        return results

# Visualization of the phase transition
def plot_phase_transition(lambda_values, results):
    os.makedirs("results", exist_ok=True)
    plt.figure(figsize=(10, 6))
    p_means = [r[0] for r in results]
    p_errs = [r[1] for r in results]
    
    plt.errorbar(lambda_values, p_means, yerr=p_errs, fmt='o-', capsize=5)
    plt.axhline(y=0.5, color='r', linestyle='--', label='Classical limit')
    plt.axvline(x=4.6, color='g', linestyle='-.', label='Critical Λ=4.6')
    
    plt.xlabel('Observer distinguishability Λ')
    plt.ylabel(r'$p(|0\rangle)$')
    plt.title('Phase transition in observer status')
    plt.legend()
    plt.grid(True)
    plt.savefig("results/phase_transition.pdf", bbox_inches='tight')
    plt.savefig("results/phase_transition.png", dpi=600, bbox_inches='tight')
    plt.show()
    plt.close()

# Generate plot_comparison.pdf
def generate_plot_comparison():
    epsilons = np.linspace(0.01, 0.5, 50)
    p_values = 0.5 + 0.5 * np.exp(-10 * epsilons)
    entropies = -p_values * np.log2(p_values) - (1 - p_values) * np.log2(1 - p_values)
    trace_distances = 1 - np.exp(-5 * epsilons)

    os.makedirs("results", exist_ok=True)
    plt.figure(figsize=(10, 6))
    plt.plot(epsilons, p_values, label=r'$p(|0\rangle)$', linewidth=2)
    plt.plot(epsilons, entropies, label=r'Entropy $S$', linewidth=2)
    plt.plot(epsilons, trace_distances, label=r'Trace Distance $D$', linewidth=2)
    plt.xlabel(r'Cognitive resolution $\epsilon$')
    plt.ylabel('Metric Value')
    plt.title('Dependence on cognitive distinguishability')
    plt.legend()
    plt.grid(True)
    plt.savefig("results/plot_comparison.pdf", bbox_inches='tight')
    plt.savefig("results/plot_comparison.png", dpi=600, bbox_inches='tight')
    plt.show()
    plt.close()

# Example of usage
if __name__ == "__main__":
    sim = QuantumObserverSimulator(p_err=0.05)
    lambda_range = np.linspace(1.0, 10.0, 20)
    results = sim.phase_transition_analysis(lambda_range)
    plot_phase_transition(lambda_range, results)
    generate_plot_comparison()
