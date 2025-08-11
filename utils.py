import matplotlib.pyplot as plt

plt.ion()  # Enable interactive mode

def live_plot_trust_distribution(simulation, timestep, avg_trust):
    plt.clf()  # Clear current figure (reuse same window)
    plt.hist(
        simulation.global_trust_scores.values(),
        bins=20,
        range=(0, 1),
        alpha=0.7,
        color='orange',
        edgecolor='black'
    )
    plt.title(f"Trust Score Distribution at timestep {timestep} | Avg Trust: {avg_trust:.3f}")
    plt.xlabel("Trust Score")
    plt.ylabel("Number of Agents")
    plt.xlim(0, 1)
    plt.ylim(0, len(simulation.agents) // 2)  # Optional Y-axis scale
    plt.pause(0.01)  # Short pause for GUI update
