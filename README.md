# Telephone Game Simulation - Deployment Instructions

## Overview
This package contains a complete agent-based modeling simulation of the Telephone game with trust dynamics. The simulation models 1,000 agents in a chain, each potentially altering a 6-character string based on their trust in other agents.


## Simulation Parameters

You can modify the simulation parameters in the code:

- `NUM_AGENTS`: Number of agents in the chain (default: 1,000)
- `NUM_TIMESTEPS`: Number of simulation rounds (default: 100)
- Learning rates and trust update mechanisms can be adjusted in `simulation.py`

## Key Features

### Trust Dynamics
- Agents start with trust values in all other agents which is based on user specified trust score distirbution in params.py
- Trust is updated based on observed deviations between input and output
- Agents adjust their behavior based on average trust levels

### Adaptive Behavior
- Agents with low trust in others are more likely to alter messages
- Agents with high trust in others are less likely to alter messages
- Behavior changes gradually over time (humanistic behavior)

### Memory System
- Each agent remembers past interactions and outcomes
- Memory is used to evaluate performance and update trust

## Understanding the Results

The simulation typically shows one of three patterns:

1. **Trust Decline**: Trust decreases over time as agents observe message distortion
2. **Trust Increase**: Trust increases as agents prove reliable
3. **Trust Stabilization**: Trust reaches an equilibrium


## License and Citation

This simulation is provided for educational and research purposes. If you use this code in academic work, please cite appropriately.

