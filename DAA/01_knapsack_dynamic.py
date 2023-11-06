def knapsack_dynamic_programming(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = []
    i, j = n, capacity
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(i - 1)
            j -= weights[i - 1]
        i -= 1

    return dp[n][capacity], selected_items

# Example usage
weights = [1, 2, 3, 4, 5]
values = [10, 15, 40, 50, 60]
capacity = 7

max_value, selected_items = knapsack_dynamic_programming(weights, values, capacity)
print("Maximum value:", max_value)
print("Selected items:", selected_items)

