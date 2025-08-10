# plot_trust_distribution.py

import matplotlib.pyplot as plt
import numpy as np
import random
from params import NUM_AGENTS, TRUST_DISTRIBUTION, TRUST_PARAMS

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

def plot_and_save(scores):
    plt.figure(figsize=(8, 5))
    plt.hist(scores, bins=30, color='skyblue', edgecolor='black')
    plt.title(f"Initial Trust Scores Distribution ({TRUST_DISTRIBUTION.capitalize()})")
    plt.xlabel("Trust Score")
    plt.ylabel("Frequency")
    plt.xlim(0, 1)
    plt.grid(axis='y', alpha=0.75)
    plt.tight_layout()
    plt.savefig("trust_scores_distribution.png")
    print("Saved distribution plot as trust_scores_distribution.png")
    plt.show()

if __name__ == "__main__":
    trust_scores = generate_trust_scores(NUM_AGENTS)
    plot_and_save(trust_scores)
