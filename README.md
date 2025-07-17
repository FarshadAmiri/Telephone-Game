# Telephone Game Simulation - Deployment Instructions

## Overview
This package contains a complete agent-based modeling simulation of the Telephone game with trust dynamics. The simulation models 1,000 agents in a chain, each potentially altering a 6-character string based on their trust in other agents.

## Package Contents
- `telephone_game_app/` - Flask web application
- `simulation.py` - Core simulation logic
- `main.py` - Command-line simulation runner
- `plot_trust.py` - Visualization script
- `trust_scores.txt` - Sample simulation results
- `average_trust_score.png` - Sample visualization

## Quick Start (Web Interface)

### Prerequisites
- Python 3.8 or higher


## Simulation Parameters

You can modify the simulation parameters in the code:

- `NUM_AGENTS`: Number of agents in the chain (default: 1,000 for web, 10,000 for CLI)
- `NUM_TIMESTEPS`: Number of simulation rounds (default: 50 for web, 100 for CLI)
- Learning rates and trust update mechanisms can be adjusted in `simulation.py`

## Key Features

### Trust Dynamics
- Agents start with neutral trust (0.5) in all other agents
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

The web interface provides:
- Real-time visualization of trust evolution
- Statistical summary of simulation parameters
- Analysis of convergence patterns

## Customization

### Modifying Agent Behavior
Edit `simulation.py` to change:
- Trust update algorithms
- String alteration probability
- Learning rates
- Memory mechanisms

### Changing the Web Interface
Edit `telephone_game_app/src/static/index.html` to modify:
- Visual appearance
- User interface elements
- Analysis text

### Adding New Features
The Flask application in `telephone_game_app/src/main.py` can be extended with:
- Parameter controls
- Different visualization types
- Export functionality
- Real-time updates

## Deployment Options

### Local Development
Use the instructions above for local testing and development.

### Production Deployment
For production deployment, consider:

1. **Using a production WSGI server**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5001 main:app
   ```

2. **Docker deployment**
   Create a Dockerfile:
   ```dockerfile
   FROM python:3.11-slim
   WORKDIR /app
   COPY . .
   RUN pip install -r requirements.txt
   EXPOSE 5001
   CMD ["python", "src/main.py"]
   ```

3. **Cloud platforms**
   - Heroku: Add `Procfile` with `web: python src/main.py`
   - AWS/GCP: Use container services or serverless functions
   - DigitalOcean App Platform: Direct deployment from Git

## Troubleshooting

### Common Issues

1. **Port already in use**
   - Change the port in `main.py`: `app.run(host='0.0.0.0', port=5002)`

2. **Module not found errors**
   - Ensure you're running from the correct directory
   - Activate the virtual environment

3. **Slow simulation**
   - Reduce `NUM_AGENTS` or `NUM_TIMESTEPS` for faster results
   - The web interface uses smaller values by default

4. **Memory issues**
   - Reduce the number of agents for large simulations
   - Clear agent memory periodically if needed

### Performance Optimization

For large-scale simulations:
- Use numpy arrays instead of Python lists
- Implement parallel processing for agent updates
- Use database storage for large memory requirements
- Consider distributed computing for very large agent populations

## Research Applications

This simulation can be used to study:
- Trust dynamics in social networks
- Information propagation and distortion
- Collective behavior emergence
- Game theory applications
- Multi-agent system design

## License and Citation

This simulation is provided for educational and research purposes. If you use this code in academic work, please cite appropriately.

## Support

For questions or issues:
1. Check the troubleshooting section above
2. Review the code comments for implementation details
3. Modify parameters to suit your specific research needs

---

**Note**: This simulation demonstrates complex emergent behavior. Results may vary between runs due to the stochastic nature of agent decisions and random string generation.

