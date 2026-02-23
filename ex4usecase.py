# Training Data
# Yes = 1, No = 0

data = [
    # Free, Win, Offer, Spam
    [1, 1, 1, 1],
    [1, 0, 1, 1],
    [0, 1, 0, 1],
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [1, 0, 0, 0]
]

# Separate features and target
X = [row[:3] for row in data]
y = [row[3] for row in data]

# Count total samples
total = len(y)

# Prior probabilities
p_spam = y.count(1) / total
p_not_spam = y.count(0) / total

# Function to calculate likelihood with Laplace smoothing
def likelihood(feature_index, feature_value, class_value):
    count_class = y.count(class_value)
    count_feature_class = 0
    
    for i in range(total):
        if y[i] == class_value and X[i][feature_index] == feature_value:
            count_feature_class += 1
    
    # Laplace smoothing (+1)
    return (count_feature_class + 1) / (count_class + 2)

# New Email: Free=Yes(1), Win=Yes(1), Offer=No(0)
new_email = [1, 1, 0]

# Calculate posterior for Spam
prob_spam = p_spam
for i in range(3):
    prob_spam *= likelihood(i, new_email[i], 1)

# Calculate posterior for Not Spam
prob_not_spam = p_not_spam
for i in range(3):
    prob_not_spam *= likelihood(i, new_email[i], 0)

print("Probability Spam:", prob_spam)
print("Probability Not Spam:", prob_not_spam)

if prob_spam > prob_not_spam:
    print("Prediction: Spam")
else:
    print("Prediction: Not Spam")

output:

Probability Spam: 0.0833...
Probability Not Spam: 0.0277...
Prediction: Spam
