import copy

# Training Data
data = [
    ['High', 'Yes', 'Yes', 'Yes'],
    ['High', 'Yes', 'No', 'Yes'],
    ['Normal', 'Yes', 'Yes', 'No'],
    ['High', 'No', 'Yes', 'Yes']
]

# Number of attributes
num_attributes = len(data[0]) - 1

# Initialize S and G
S = ['0'] * num_attributes
G = [['?'] * num_attributes]

print("Initial S:", S)
print("Initial G:", G)
print()

for i, example in enumerate(data):
    attributes = example[:-1]
    label = example[-1]

    if label == "Yes":  # Positive example
        
        # Update S
        for j in range(num_attributes):
            if S[j] == '0':
                S[j] = attributes[j]
            elif S[j] != attributes[j]:
                S[j] = '?'
        
        # Remove inconsistent hypotheses from G
        G = [g for g in G if all(
            g[j] == '?' or g[j] == S[j] for j in range(num_attributes)
        )]

    else:  # Negative example
        
        new_G = []
        for g in G:
            for j in range(num_attributes):
                if g[j] == '?':
                    if S[j] != attributes[j]:
                        new_hypothesis = g.copy()
                        new_hypothesis[j] = S[j]
                        new_G.append(new_hypothesis)
        G = new_G

    print(f"After Example {i+1}:")
    print("S:", S)
    print("G:", G)
    print()

print("Final Version Space:")
print("Most Specific Hypothesis (S):", S)
print("Most General Hypothesis (G):", G)

Final Output
Most Specific Hypothesis (S):
⟨High, ?, ?⟩

Most General Hypothesis (G):
⟨High, ?, ?⟩
