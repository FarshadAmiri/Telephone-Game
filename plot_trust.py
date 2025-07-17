import matplotlib.pyplot as plt

# Read trust scores from file
trust_scores = []
with open("trust_scores.txt", "r") as f:
    for line in f:
        trust_scores.append(float(line.strip()))

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(trust_scores)
plt.title("Average Trust Score Over Time")
plt.xlabel("Timestep")
plt.ylabel("Average Trust Score")
plt.grid(True)
plt.savefig("average_trust_score.png")
print("Plot saved to average_trust_score.png")


