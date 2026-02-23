import numpy as np

# Observed data (number of heads in 10 tosses)
data = np.array([5, 9, 8, 4, 7])
n = 10

# Initial guesses
theta_A = 0.6
theta_B = 0.5

# Run EM for 5 iterations
for i in range(5):

    # E-step
    prob_A = (theta_A ** data) * ((1 - theta_A) ** (n - data))
    prob_B = (theta_B ** data) * ((1 - theta_B) ** (n - data))

    # Normalize to get weights
    total = prob_A + prob_B
    weight_A = prob_A / total
    weight_B = prob_B / total

    # M-step
    theta_A = np.sum(weight_A * data) / (np.sum(weight_A) * n)
    theta_B = np.sum(weight_B * data) / (np.sum(weight_B) * n)

    print(f"Iteration {i+1}: Theta_A = {theta_A:.4f}, Theta_B = {theta_B:.4f}")

print("\nFinal Result:")
print("Theta A =", round(theta_A, 3))
print("Theta B =", round(theta_B, 3))
