import random

def deterministic_partition(arr, low, high):
    pivot = low  # Choose the first element as the pivot
    i = low + 1

    for j in range(low + 1, high + 1):
        if arr[j] < arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[pivot], arr[i - 1] = arr[i - 1], arr[pivot]
    return i - 1

def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return deterministic_partition(arr, low, high)

def deterministic_quick_sort(arr, low, high):
    if low < high:
        pivot = deterministic_partition(arr, low, high)
        deterministic_quick_sort(arr, low, pivot - 1)
        deterministic_quick_sort(arr, pivot + 1, high)

def randomized_quick_sort(arr, low, high):
    if low < high:
        pivot = randomized_partition(arr, low, high)
        randomized_quick_sort(arr, low, pivot - 1)
        randomized_quick_sort(arr, pivot + 1, high)

def analyze_quick_sort_performance(arr):
    arr_copy = arr.copy()
    comparisons_deterministic = [0]  # To count the number of comparisons in deterministic quicksort
    comparisons_randomized = [0]  # To count the number of comparisons in randomized quicksort

    def counting_deterministic_partition(arr, low, high):
        pivot = low
        i = low + 1

        for j in range(low + 1, high + 1):
            comparisons_deterministic[0] += 1
            if arr[j] < arr[pivot]:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[pivot], arr[i - 1] = arr[i - 1], arr[pivot]
        return i - 1

    def counting_randomized_partition(arr, low, high):
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        return counting_deterministic_partition(arr, low, high)

    randomized_quick_sort(arr_copy, 0, len(arr_copy) - 1)
    deterministic_quick_sort(arr, 0, len(arr) - 1)

    print("Deterministic Quick Sort:")
    print("Number of comparisons:", comparisons_deterministic[0])
    print("Sorted array:", arr)

    print("\nRandomized Quick Sort:")
    print("Number of comparisons:", comparisons_deterministic[0])
    print("Sorted array:", arr_copy)

if __name__ == "__main__":
    arr = [5, 8, 2, 9, 1, 6, 3, 7, 4]
    analyze_quick_sort_performance(arr)

