def fractional_knapsack(items, capacity):
    # Calculate the value-to-weight ratio for each item
    items_with_ratios = [(item[0], item[1], item[1] / item[0]) for item in items]
    # Sort the items in decreasing order of value-to-weight ratio
    items_with_ratios.sort(key=lambda x: x[2], reverse=True)
    total_value = 0.0
    knapsack = []
    for item in items_with_ratios:
        item_weight, item_value, ratio = item
        if capacity >= item_weight:
            # Take the whole item
            knapsack.append((item_weight, item_value))
            total_value += item_value
            capacity -= item_weight
        else:
            # Take a fraction of the item
            fraction = capacity / item_weight
            knapsack.append((capacity, fraction * item_value))
            total_value += fraction * item_value
            break  # The knapsack is full
    return knapsack, total_value

# Example usage:
items = [(10, 60), (20, 100), (30, 120)]
capacity = 50
knapsack, total_value = fractional_knapsack(items, capacity)
print("Items in the knapsack:")
for item in knapsack:
    weight, value = item
    print(f"Weight: {weight}, Value: {value}")
print("Total Value:", total_value)

