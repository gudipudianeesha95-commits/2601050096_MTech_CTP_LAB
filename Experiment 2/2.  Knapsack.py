weights = [2, 3, 4]
values = [40, 50, 60]
capacity = 5

dp = [0] * (capacity + 1)

for i in range(len(weights)):
    for w in range(capacity, weights[i] - 1, -1):
        dp[w] = max(dp[w], values[i] + dp[w - weights[i]])

print("Maximum Value:", dp[capacity])