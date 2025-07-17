from flask import Flask, render_template, jsonify, send_file
from flask_cors import CORS
import os
import json
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
from simulation import Simulation
import io
import base64

app = Flask(__name__, static_folder='static', template_folder='static')
CORS(app)

@app.route('/')
def index():
    return send_file('static/index.html')

@app.route('/api/run_simulation', methods=['POST'])
def run_simulation():
    try:
        # Parameters for simulation
        NUM_AGENTS = 1000  # Reduced for faster web response
        NUM_TIMESTEPS = 50  # Reduced for faster web response
        
        simulation = Simulation(NUM_AGENTS)
        trust_scores_over_time = []
        
        for t in range(NUM_TIMESTEPS):
            simulation.run_timestep()
            
            total_trust = sum(simulation.global_trust_scores.values())
            num_trust_relationships = len(simulation.global_trust_scores)
            
            if num_trust_relationships > 0:
                avg_trust = total_trust / num_trust_relationships
                trust_scores_over_time.append(avg_trust)
            else:
                trust_scores_over_time.append(0.5)
        
        # Generate plot
        plt.figure(figsize=(10, 6))
        plt.plot(trust_scores_over_time)
        plt.title("Average Trust Score Over Time")
        plt.xlabel("Timestep")
        plt.ylabel("Average Trust Score")
        plt.grid(True)
        
        # Save plot to base64 string
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()
        plt.close()
        
        return jsonify({
            'trust_scores': trust_scores_over_time,
            'plot': plot_url,
            'num_agents': NUM_AGENTS,
            'num_timesteps': NUM_TIMESTEPS
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

