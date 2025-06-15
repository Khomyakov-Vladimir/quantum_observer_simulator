# Quantum Observer Simulator

This repository contains the simulation code accompanying the research project on cognitive distinguishability, quantum observer dynamics, and phase transition phenomena in subjective physics. The implementation supports the published study:

**Khomyakov, V. (2025). Cognitive Distinguishability and Quantum Observer Simulation — A Phase Transition Perspective.**  
Zenodo. [https://doi.org/10.5281/zenodo.15571107](https://doi.org/10.5281/zenodo.15571107)

## Overview

The project includes two main Python scripts:

- **`QuantumObserverSimulator.py`**  
  Simulates the emergence of phase transitions in the quantum observer's behavior as a function of cognitive distinguishability. Incorporates noise and observer-based decoherence modeling.

- **`cognitive_dimension.py`**  
  Computes and visualizes the effective cognitive dimension of the observer’s configuration space as a function of the overlap between quantum states.

Both scripts generate high-resolution plots and save them to the `results/` subdirectory.

## Directory Structure

```
.
├── QuantumObserverSimulator.py
├── cognitive_dimension.py
├── figures/
│   ├── plot_comparison.png
│   ├── plot_comparison.pdf
│   ├── phase_transition.png
│   ├── phase_transition.pdf
│   ├── cognitive_dimension.png
│   └── cognitive_dimension.pdf
├── README.md
```

> The `results/` directory is created automatically upon script execution if it does not exist.

## Requirements

This project requires the following Python libraries:

- `numpy`
- `matplotlib`
- `scipy`

Install them via pip:

```bash
pip install numpy matplotlib scipy
```

## Usage

To run the simulations and generate plots:

```bash
python QuantumObserverSimulator.py
python cognitive_dimension.py
```

The resulting plots will be saved in the `results/` directory.

## Output

- **phase_transition.png**, **phase_transition.pdf**  
  Plot of the observer phase transition as a function of the distinguishability parameter Λ.

- **cognitive_dimension.png**, **cognitive_dimension.pdf**  
  Plot of the cognitive configuration space dimensionality vs. state overlap.

- **plot_comparison.png**, **plot_comparison.pdf**  
  Combined plot comparing both effects on a unified scale.

## License

This project is licensed under the terms of the MIT License. You are free to use, modify, and distribute this code with attribution.

## Citation

If you find this code or the related research useful, please cite the publication:

```bibtex
@misc{khomyakov2025cognitive,
  author       = {Khomyakov, Vladimir},
  title        = {Cognitive Distinguishability and Quantum Observer Simulation — A Phase Transition Perspective},
  year         = 2025,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.15571107},
  url          = {https://doi.org/10.5281/zenodo.15571107}
}
```

## Related Resources

- 📘 [Zenodo Publication](https://doi.org/10.5281/zenodo.15571107)
- 🧠 Based on formalism discussed in the context of subjective physics and observer-based emergence
