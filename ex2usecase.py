import math
from collections import Counter

# Dataset
data = [
    ['High', 'Yes', 'Yes', 'Old', 'Yes'],
    ['High', 'Yes', 'No', 'Young', 'Yes'],
    ['Normal', 'Yes', 'Yes', 'Old', 'Yes'],
    ['Low', 'No', 'No', 'Young', 'No']
]

attributes = ['Fever', 'Cough', 'Fatigue', 'Age']

# Entropy calculation
def entropy(dataset):
    labels = [row[-1] for row in dataset]
    count = Counter(labels)
    total = len(dataset)
    
    ent = 0
    for label in count:
        p = count[label] / total
        ent -= p * math.log2(p)
    return ent

# Information Gain
def information_gain(dataset, attr_index):
    total_entropy = entropy(dataset)
    total = len(dataset)
    
    values = set(row[attr_index] for row in dataset)
    weighted_entropy = 0
    
    for value in values:
        subset = [row for row in dataset if row[attr_index] == value]
        weighted_entropy += (len(subset)/total) * entropy(subset)
    
    return total_entropy - weighted_entropy

# ID3 Algorithm
def id3(dataset, attributes):
    labels = [row[-1] for row in dataset]
    
    # If all examples same class
    if labels.count(labels[0]) == len(labels):
        return labels[0]
    
    # If no attributes left
    if not attributes:
        return Counter(labels).most_common(1)[0][0]
    
    gains = [information_gain(dataset, i) for i in range(len(attributes))]
    best_attr_index = gains.index(max(gains))
    best_attr = attributes[best_attr_index]
    
    tree = {best_attr: {}}
    
    values = set(row[best_attr_index] for row in dataset)
    
    for value in values:
        subset = [row[:best_attr_index] + row[best_attr_index+1:]
                  for row in dataset if row[best_attr_index] == value]
        
        new_attrs = attributes[:best_attr_index] + attributes[best_attr_index+1:]
        
        subtree = id3(subset, new_attrs)
        tree[best_attr][value] = subtree
    
    return tree

# Build Tree
decision_tree = id3(data, attributes)

print("Decision Tree:")
print(decision_tree)


output:
Fever
 ├── High → Yes
 ├── Normal → Yes
 └── Low → No
