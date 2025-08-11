NUM_AGENTS = 1000
NUM_TIMESTEPS = 100

# Trust score distribution configuration
TRUST_DISTRIBUTION = "normal"  # options: "uniform", "normal", "gamma", "gamma-inverted", "bounded"

# Parameters for each distribution
TRUST_PARAMS = {
    "uniform": {"value": 0.5},               # fixed trust for all
    "normal": {"mu": 0.4, "sigma": 0.15},     # mean and standard deviation
    "gamma": {"shape": 2.0, "scale": 0.2},   # k (shape), θ (scale) | skewed to left
    "gamma-inverted": {"shape": 3, "scale": 1},   # k (shape), θ (scale) | # skewed to right
    "bounded": {"min": 0.3, "max": 0.8}      # min and max bounds
}