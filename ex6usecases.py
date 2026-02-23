import math
from collections import Counter

# Training Data
# Format: [Study Hours, Attendance, Result]
data = [
    [2, 30, "Fail"],
    [3, 35, "Fail"],
    [5, 60, "Pass"],
    [6, 65, "Pass"],
    [8, 80, "Pass"],
    [1, 25, "Fail"]
]

# New student data
new_student = [4, 50]

# Value of K
k = 3

# Step 1: Calculate Euclidean Distance
distances = []

for student in data:
    distance = math.sqrt(
        (student[0] - new_student[0])**2 +
        (student[1] - new_student[1])**2
    )
    distances.append((distance, student[2]))

# Step 2: Sort by distance
distances.sort(key=lambda x: x[0])

# Step 3: Select K nearest neighbors
k_nearest = distances[:k]

# Step 4: Majority Voting
results = [neighbor[1] for neighbor in k_nearest]
prediction = Counter(results).most_common(1)[0][0]

print("K Nearest Neighbors:", k_nearest)
print("Predicted Result:", prediction)

output:

Predicted Result: Pass
