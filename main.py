from simulation import Simulation
from params import NUM_AGENTS, NUM_TIMESTEPS
from plots import plot_initial_trust_scores, plot_avg_trust_scores, plot_last_vs_initial_trust_dists
from utils import live_plot_trust_distribution 
import matplotlib.pyplot as plt
import json
import os

def main():
    os.makedirs("results", exist_ok=True)

    simulation = Simulation(NUM_AGENTS)

    # Save initial trust scores before simulation starts
    with open(r"results\trust_scores_initial.json", "w") as f:
        json.dump(simulation.global_trust_scores, f)

    # Store trust scores over time for analysis
    trust_scores_over_time = []

    for t in range(NUM_TIMESTEPS):
        simulation.run_timestep()

        # Calculate average trust score
        total_trust = sum(simulation.global_trust_scores.values())
        num_trust_relationships = len(simulation.global_trust_scores)
        
        if num_trust_relationships > 0:
            avg_trust = total_trust / num_trust_relationships
            trust_scores_over_time.append(avg_trust)
        else:
            trust_scores_over_time.append(0.5)  # Default if no trust relationships yet

        print(f"Timestep {t+1}: Average Trust = {trust_scores_over_time[-1]:.4f}")

        # Live plot
        live_plot_trust_distribution(simulation, timestep=t+1, avg_trust=avg_trust)

    # Save final trust scores
    with open(r"results\trust_scores_final.json", "w") as f:
        json.dump(simulation.global_trust_scores, f)

    # Save trust score trend
    with open(r"results\trust_scores_over_time.txt", "w") as f:
        for score in trust_scores_over_time:
            f.write(f"{score}\n")

    print("Initial and final trust scores saved to 'results' folder.")
    print("Trend of trust scores saved to 'trust_scores_over_time.txt'.")

    plt.ioff()
    plt.show()

if __name__ == "__main__":
    main()
    plot_initial_trust_scores()
    plot_avg_trust_scores()
    plot_last_vs_initial_trust_dists()
