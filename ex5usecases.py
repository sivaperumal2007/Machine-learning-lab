import numpy as np
from scipy.stats import binom

# Observed data (number of heads out of 10 tosses)
data = np.array([5, 9, 8, 4, 7])
n = 10  # number of tosses per trial

# Initial guesses for parameters
theta_A = 0.6
theta_B = 0.5

# Number of EM iterations
iterations = 10

for iteration in range(iterations):
    
    # -------------------
    # E-STEP
    # -------------------
    weights_A = []
    weights_B = []
    
    for heads in data:
        # Likelihood for Coin A and Coin B
        likelihood_A = binom.pmf(heads, n, theta_A)
        likelihood_B = binom.pmf(heads, n, theta_B)
        
        # Responsibility (posterior probability)
        weight_A = likelihood_A / (likelihood_A + likelihood_B)
        weight_B = likelihood_B / (likelihood_A + likelihood_B)
        
        weights_A.append(weight_A)
        weights_B.append(weight_B)
    
    weights_A = np.array(weights_A)
    weights_B = np.array(weights_B)
    
    # -------------------
    # M-STEP
    # -------------------
    theta_A = np.sum(weights_A * data) / (n * np.sum(weights_A))
    theta_B = np.sum(weights_B * data) / (n * np.sum(weights_B))
    
    print(f"Iteration {iteration+1}:")
    print(f"theta_A = {theta_A:.4f}")
    print(f"theta_B = {theta_B:.4f}")
    print("-" * 30)

print("\nFinal Estimates:")
print("θ_A =", round(theta_A, 4))
print("θ_B =", round(theta_B, 4))

output:
θ_A ≈ 0.80
θ_B ≈ 0.52
