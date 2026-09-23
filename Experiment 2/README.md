**EXPERIMENT 2 — 0/1 Knapsack**

The workbook specifies Dynamic Programming for 0/1 Knapsack and analysis of time and space complexity.

**Aim**

To implement the 0/1 Knapsack problem using Dynamic Programming.

**Algorithm**

1.Take item weights and values.

2.Take the bag capacity.

3.Create a DP table.

4.Decide whether to include each item.

5.Find the maximum value.

**Python Program**

weights = [2, 3, 4]

values = [40, 50, 60]

capacity = 5

dp = [0] * (capacity + 1)

for i in range(len(weights)):
   
    for w in range(capacity, weights[i] - 1, -1):
    
        dp[w] = max(dp[w], values[i] + dp[w - weights[i]])

print("Maximum Value:", dp[capacity])

**Output**

Maximum Value: 90

**Data & Result**

Weights = [2, 3, 4]

Values  = [40, 50, 60]

Capacity = 5

Maximum Value = 90

**Inference & Analysis**

The program selected the items giving maximum value without exceeding capacity.

Time Complexity: O(nW)

Space Complexity: O(W)

**Result**

Thus, 0/1 Knapsack was successfully implemented using Dynamic Programming.
