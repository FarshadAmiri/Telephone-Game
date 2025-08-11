from simulation import Simulation
from params import NUM_AGENTS, NUM_TIMESTEPS
from utils import live_plot_trust_distribution
import matplotlib.pyplot as plt


def main():
    simulation = Simulation(NUM_AGENTS)

    # Store trust scores over time for analysis
    trust_scores_over_time = []

    for t in range(NUM_TIMESTEPS):
        simulation.run_timestep()

        # Collect average trust score at each timestep
        # This requires iterating through all agents and their trust dictionaries
        # For simplicity, let\'s calculate the average of all trust scores across all agents
        # This might be computationally intensive for 10,000 agents and 100 timesteps.
        # We might need to optimize this later if performance is an issue.
        total_trust = sum(simulation.global_trust_scores.values())
        num_trust_relationships = len(simulation.global_trust_scores)
        
        if num_trust_relationships > 0:
            avg_trust = total_trust / num_trust_relationships
            trust_scores_over_time.append(avg_trust)
        else:
            trust_scores_over_time.append(0.5) # Default if no trust relationships yet

        print(f"Timestep {t+1}: Average Trust = {trust_scores_over_time[-1]:.4f}")

        live_plot_trust_distribution(simulation, timestep=t+1, avg_trust=avg_trust)

    # After simulation, you can analyze trust_scores_over_time
    # For example, plot it to see the trend.
    print("Simulation finished.")
    
    # rounded_trust_scores_over_time = [round(score, 4) for score in trust_scores_over_time]
    # print(f"Average trust scores over time: {rounded_trust_scores_over_time}")

    with open("trust_scores.txt", "w") as f:
        for score in trust_scores_over_time:
            f.write(f"{score}\n")
    print("Trust scores saved to trust_scores.txt")

    plt.ioff()
    plt.show()


if __name__ == "__main__":
    main()


