import random
import string
import numpy as np
from params import TRUST_DISTRIBUTION, TRUST_PARAMS

class Agent:
    def __init__(self, agent_id):
        self.agent_id = agent_id
        self.memory = []
        self.mu = 0.0 # Mean of the normal distribution for altering the string
        self.sigma = 0.1 # Standard deviation of the normal distribution

    def alter_string(self, input_string):
        # The agent alters the string based on its normal distribution
        if np.random.normal(self.mu, self.sigma) > 0.5:
            pos = random.randint(0, len(input_string) - 1)
            char = random.choice(string.ascii_lowercase)
            return input_string[:pos] + char + input_string[pos+1:]
        return input_string

    def update_memory(self, original_input, final_output, own_output):
        # Agent evaluates its own performance and stores it
        self.memory.append({
            'original_input': original_input,
            'final_output': final_output,
            'own_output': own_output
        })

    def update_trust(self, global_trust_scores, final_output):
        # Agents update their trust in others based on the global trust scores.
        # This method will be called by the Simulation class, which manages the global trust scores.
        pass

    def update_distribution(self, global_trust_scores):
        # Agents change their distribution over timesteps, but not easily.
        # This reflects their humanist behavior.
        # If the average trust in other agents is high, the agent might become less likely to alter the message.
        # If the average trust is low, the agent might become more likely to alter the message.

        # This agent needs to know the global trust scores to update its distribution.
        # For simplicity, let's assume the agent considers the average trust of all other agents.
        if not global_trust_scores: # If no trust scores yet, do nothing
            return

        # Calculate average trust in other agents (excluding self)
        total_trust = 0
        num_trusted_agents = 0
        for agent_id, trust_score in global_trust_scores.items():
            if agent_id != self.agent_id:
                total_trust += trust_score
                num_trusted_agents += 1
        
        if num_trusted_agents == 0:
            return # No other agents to trust

        avg_trust = total_trust / num_trusted_agents

        # Adjust mu and sigma based on average trust
        learning_rate_dist = 0.01 # Small learning rate for distribution change

        target_mu = 1.0 - avg_trust
        target_sigma = 1.0 - avg_trust

        self.mu += learning_rate_dist * (target_mu - self.mu)
        self.sigma += learning_rate_dist * (target_sigma - self.sigma)

        self.mu = max(0.0, min(1.0, self.mu))
        self.sigma = max(0.01, min(1.0, self.sigma))


class Simulation:
    def __init__(self, num_agents):
        self.agents = [Agent(i) for i in range(num_agents)]
        self.global_trust_scores = self._initialize_trust_scores(num_agents)
        self.current_input = ""
        self.final_output = ""
        self.timesteps = 0

    def _initialize_trust_scores(self, num_agents):
        scores = {}
        dist = TRUST_DISTRIBUTION.lower()
        params = TRUST_PARAMS.get(dist, {})

        if dist == "uniform":
            val = params.get("value", 0.5)
            scores = {i: val for i in range(num_agents)}

        elif dist == "normal":
            mu = params.get("mu", 0.5)
            sigma = params.get("sigma", 0.1)
            raw_scores = np.random.normal(mu, sigma, num_agents)
            scores = {i: float(np.clip(s, 0, 1)) for i, s in enumerate(raw_scores)}

        elif dist == "gamma":
            shape = params.get("shape", 2.0)
            scale = params.get("scale", 0.2)
            raw_scores = np.random.gamma(shape, scale, num_agents)
            # Normalize to [0,1] if needed
            max_val = max(raw_scores)
            scores = {i: float(s / max_val) for i, s in enumerate(raw_scores)}

        elif dist == "gamma-inverted":
            shape = params.get("shape", 2.0)
            scale = params.get("scale", 0.2)
            raw_scores = np.random.gamma(shape, scale, num_agents)
            max_val = max(raw_scores)
            normalized = np.array([s / max_val for s in raw_scores])
            scores = {i: float(1 - val) for i, val in enumerate(normalized)}

        elif dist == "bounded":
            min_val = params.get("min", 0.3)
            max_val = params.get("max", 0.8)
            scores = {i: random.uniform(min_val, max_val) for i in range(num_agents)}

        else:
            raise ValueError(f"Unknown trust distribution: {dist}")
        
        scores = {i: float(np.clip(s, 0, 1)) for i, s in scores.items()}

        return scores

    def generate_input(self, length=6):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

    def run_timestep(self):
        self.current_input = self.generate_input()
        message = self.current_input
        agent_outputs = []
        for agent in self.agents:
            message = agent.alter_string(message)
            agent_outputs.append(message)

        self.final_output = message

        # Update global trust scores
        for i, agent in enumerate(self.agents):
            own_output = agent_outputs[i] if i < len(agent_outputs) else ""
            agent.update_memory(self.current_input, self.final_output, own_output)

            # Update global trust score for this agent based on its performance
            # This is a simplified model. A more complex model would involve
            # comparing the deviation caused by each agent relative to the overall deviation.
            # For now, let's assume an agent's trustworthiness is inversely proportional to its deviation from the original input.
            deviation_from_original = string_distance(self.current_input, own_output)
            reliability_score = 1.0 - (deviation_from_original / 6.0) # Max deviation is 6

            learning_rate = 0.05
            current_global_trust = self.global_trust_scores.get(agent.agent_id, 0.5)
            new_global_trust = current_global_trust + learning_rate * (reliability_score - current_global_trust)
            self.global_trust_scores[agent.agent_id] = max(0.0, min(1.0, new_global_trust))

        # Agents update their distributions based on global trust scores
        for agent in self.agents:
            agent.update_distribution(self.global_trust_scores)

def string_distance(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))


