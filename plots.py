# plot_trust_distribution.py

import matplotlib.pyplot as plt
import numpy as np
import random, json
from params import NUM_AGENTS, TRUST_DISTRIBUTION, TRUST_PARAMS
from simulation import Simulation

#--------------------------------------
# 1. Plot Initial Trust Distribution
#--------------------------------------

def generate_trust_scores(num_agents):
    dist = TRUST_DISTRIBUTION.lower()
    params = TRUST_PARAMS.get(dist, {})

    if dist == "uniform":
        val = params.get("value", 0.5)
        scores = np.full(num_agents, val)

    elif dist == "normal":
        mu = params.get("mu", 0.5)
        sigma = params.get("sigma", 0.1)
        raw_scores = np.random.normal(mu, sigma, num_agents)
        scores = np.clip(raw_scores, 0, 1)

    elif dist == "gamma":
        shape = params.get("shape", 2.0)
        scale = params.get("scale", 0.2)
        raw_scores = np.random.gamma(shape, scale, num_agents)
        scores = raw_scores / max(raw_scores)  # Normalize to [0,1]

    elif dist == "gamma-inverted":
        shape = params.get("shape", 2.0)
        scale = params.get("scale", 0.2)
        raw_scores = np.random.gamma(shape, scale, num_agents)
        scores = raw_scores / max(raw_scores)  # Normalize to [0,1]
        scores = 1 - scores

    elif dist == "bounded":
        min_val = params.get("min", 0.3)
        max_val = params.get("max", 0.8)
        scores = np.array([random.uniform(min_val, max_val) for _ in range(num_agents)])

    else:
        raise ValueError(f"Unknown trust distribution: {dist}")

    return scores

def plot_initial_trust_scores():
    initial_trust_scores = generate_trust_scores(NUM_AGENTS)
    plt.figure(figsize=(8, 5))
    plt.hist(initial_trust_scores, bins=30, color='skyblue', edgecolor='black')
    plt.title(f"Initial Trust Scores Distribution ({TRUST_DISTRIBUTION.capitalize()})")
    plt.xlabel("Trust Score")
    plt.ylabel("Frequency")
    plt.xlim(0, 1)
    plt.grid(axis='y', alpha=0.75)
    plt.tight_layout()
    plt.savefig(r"results\initial_trust_dist.png")
    print("Saved distribution plot as trust_scores_distribution.png in result folder")
    plt.show()


#---------------------------------------
# 2. Plot Average Trust Distribution
#---------------------------------------

# Read trust scores from file

def plot_avg_trust_scores():
    avg_trust_scores = []
    with open(r"results\trust_scores_over_time.txt", "r") as f:
        for line in f:
            avg_trust_scores.append(float(line.strip()))

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(avg_trust_scores)
    plt.title("Average Trust Score Over Time")
    plt.xlabel("Timestep")
    plt.ylabel("Average Trust Score")
    plt.grid(True)
    plt.savefig(r"results\avg_trust_over_iterations.png")
    print("Plot saved to average_trust_score.png")
    plt.show()



#--------------------------------------------
# 3. Plot Last vs Initial Trust Distribution
#--------------------------------------------

def plot_last_vs_initial_trust_dists():
    # Load initial trust scores from file
    with open(r"results\trust_scores_initial.json", "r") as f:
        initial_scores_dict = json.load(f)
    initial_scores = list(initial_scores_dict.values())

    # Load final trust scores from file
    with open(r"results\trust_scores_final.json", "r") as f:
        final_scores_dict = json.load(f)
    final_scores = list(final_scores_dict.values())

    plt.figure(figsize=(10, 5))

    plt.hist(initial_scores, bins=30, alpha=0.5, label='Initial Trust Scores', color='blue', density=True)
    plt.hist(final_scores, bins=30, alpha=0.5, label='Final Trust Scores', color='orange', density=True)

    plt.title("Trust Scores Distribution Comparison")
    plt.xlabel("Trust Score")
    plt.ylabel("Density")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(r"results\last_vs_initial_trust_dist.png")
    plt.show()



if __name__ == "__main__":
    plot_initial_trust_scores()
    plot_avg_trust_scores()
    plot_last_vs_initial_trust_dists()