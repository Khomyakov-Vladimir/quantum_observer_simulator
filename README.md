# Quantum Observer Simulator

This repository contains simulation code supporting the research on cognitive observer models and phase transitions in subjective distinguishability. The implementation is based on the formalism developed in the corresponding [arXiv preprint](https://arxiv.org/abs/XXXXXXXX).

## Overview

The project includes two main Python scripts:

- **`QuantumObserverSimulator.py`**  
  Simulates the phase transition in the status of a quantum observer as a function of their effective distinguishability, incorporating noise and observer-dependent collapse probability.

- **`cognitive_dimension.py`**  
  Computes and visualizes the dependency between the cognitive dimension of the observer's configuration space and the distinguishability of quantum states.

Both scripts generate high-resolution plots and save them to the `results/` subdirectory.

## Directory Structure

```
.
├── QuantumObserverSimulator.py
├── cognitive_dimension.py
├── results/
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

Install them via pip if not already available:

```bash
pip install numpy matplotlib scipy
```

## Usage

To run the simulations and generate plots:

```bash
python QuantumObserverSimulator.py
python cognitive_dimension.py
```

After execution, the generated plots will be available in the `results/` directory.

## Output

- **phase_transition.png**, **phase_transition.pdf**  
  Plot of the observer phase transition vs. distinguishability parameter Λ.

- **cognitive_dimension.png**, **cognitive_dimension.pdf**  
  Plot of the cognitive dimension as a function of the overlap between observer states.

## License

This repository is released under the MIT License.

## Citation

If you find this code useful in your research, please cite the associated preprint:

```bibtex
@article{YourCitation2025,
  title     = {Title of the Article},
  author    = {Your Name},
  journal   = {arXiv preprint},
  year      = {2025},
  eprint    = {arXiv:XXXXXXXX},
  archivePrefix = {arXiv},
}
```
