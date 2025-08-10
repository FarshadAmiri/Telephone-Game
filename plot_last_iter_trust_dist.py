import matplotlib.pyplot as plt
from simulation import Simulation

def plot_trust_distributions(simulation):
    # Extract initial and current trust scores as lists of floats
    initial_scores = list(simulation._initialize_trust_scores(len(simulation.agents)).values())
    current_scores = list(simulation.global_trust_scores.values())

    plt.figure(figsize=(10, 5))

    plt.hist(initial_scores, bins=30, alpha=0.5, label='Initial Trust Scores', color='blue', density=True)
    plt.hist(current_scores, bins=30, alpha=0.5, label='Current Trust Scores', color='orange', density=True)

    plt.title("Trust Scores Distribution Comparison")
    plt.xlabel("Trust Score")
    plt.ylabel("Density")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("trust_scores_comparison.png")  # Save the figure if you want
    plt.show()

# Usage example:
if __name__ == "__main__":
    sim = Simulation(num_agents=100)
    # Run a few timesteps to update trust scores
    for _ in range(50):
        sim.run_timestep()
    
    plot_trust_distributions(sim)
