def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not in the list

# Test the function
test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = linear_search(test_list, 6)
print(f"Linear Search: Index of 6 is {result}")


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Return the index if the target is found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Return -1 if the target is not in the list

# Test the function
test_list_sorted = sorted(test_list)
result = binary_search(test_list_sorted, 6)
print(f"Binary Search: Index of 6 in sorted list is {result}")

import time

def compare_search_algorithms(arr, target):
    # Linear Search
    start_time = time.time()
    linear_result = linear_search(arr, target)
    linear_time = time.time() - start_time
    
    # Binary Search (on sorted array)
    arr_sorted = sorted(arr)
    start_time = time.time()
    binary_result = binary_search(arr_sorted, target)
    binary_time = time.time() - start_time
    
    print(f"Linear Search: Found at index {linear_result}, Time: {linear_time:.6f} seconds")
    print(f"Binary Search: Found at index {binary_result}, Time: {binary_time:.6f} seconds")

# Test with a larger list
large_list = list(range(10000))
compare_search_algorithms(large_list, 8888)

def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Test the recursive function
result = binary_search_recursive(test_list_sorted, 6, 0, len(test_list_sorted) - 1)
print(f"Recursive Binary Search: Index of 6 in sorted list is {result}")

def main():
    # Create a list of 20 random integers between 1 and 100
    import random
    test_list = [random.randint(1, 100) for _ in range(20)]
    
    print("Original list:", test_list)
    print("Sorted list:", sorted(test_list))
    
    target = random.choice(test_list)  # Choose a random target from the list
    print(f"\nSearching for: {target}")
    
    # Linear Search
    result = linear_search(test_list, target)
    print(f"Linear Search: Found at index {result}")
    
    # Binary Search (iterative)
    sorted_list = sorted(test_list)
    result = binary_search(sorted_list, target)
    print(f"Binary Search (iterative): Found at index {result}")
    
    # Binary Search (recursive)
    result = binary_search_recursive(sorted_list, target, 0, len(sorted_list) - 1)
    print(f"Binary Search (recursive): Found at index {result}")
    
    # Compare performance
    print("\nPerformance Comparison:")
    compare_search_algorithms(list(range(100000)), 99999)

if __name__ == "__main__":
    main()


print('\nExercise1')

def linear_search(arr, target):
    indices = []  # List to store indices where the target appears
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)  # Add index to the list if target is found
    return indices if indices else -1  # Return indices if found, else -1

# Test the modified function
test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = linear_search(test_list, 5)
print(f"Linear Search: Indices of 5 are {result}")

print('\nExercise2')

def find_insertion_point(arr, target):
    # Initialize the left and right pointers
    left, right = 0, len(arr)
    
    # Perform binary search
    while left < right:
        # Calculate the middle index
        mid = (left + right) // 2
        # If the middle element is less than the target,
        # move the left pointer to mid + 1 to search in the right half
        if arr[mid] < target:
            left = mid + 1
        # Otherwise, move the right pointer to mid to continue searching in the left half
        else:
            right = mid
    # When left equals right, we have found the insertion point
    return left

# Test the function
sorted_list = [1, 3, 4, 7, 8, 10]
target = 5
insertion_point = find_insertion_point(sorted_list, target)
print(f"Insertion point for {target} is at index {insertion_point}")


print('\nExercise3')

# Linear Search with Comparison Counter
def linear_search_with_count(arr, target):
    comparisons = 0  # Initialize comparison counter
    for i in range(len(arr)):
        comparisons += 1  # Increment comparison counter
        if arr[i] == target:
            return i, comparisons  # Return index and comparisons if found
    return -1, comparisons  # Return -1 and comparisons if not found

# Iterative Binary Search with Comparison Counter

def binary_search_with_count(arr, target):
    left, right = 0, len(arr) - 1
    comparisons = 0  # Initialize comparison counter
    
    while left <= right:
        comparisons += 1  # Increment comparison counter
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid, comparisons  # Return index and comparisons if found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1, comparisons  # Return -1 and comparisons if not found

# Recursive Binary Search with Comparison Counter

def binary_search_recursive_with_count(arr, target, left, right, comparisons=0):
    if left > right:
        return -1, comparisons  # Return -1 and comparisons if not found
    
    comparisons += 1  # Increment comparison counter
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid, comparisons  # Return index and comparisons if found
    elif arr[mid] < target:
        return binary_search_recursive_with_count(arr, target, mid + 1, right, comparisons)
    else:
        return binary_search_recursive_with_count(arr, target, left, mid - 1, comparisons)


# Test the Functions with Comparison Counting

# Test list
test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_test_list = sorted(test_list)
target = 5

# Linear Search Test
index, comparisons = linear_search_with_count(test_list, target)
print(f"Linear Search: Index of {target} is {index}, Comparisons made: {comparisons}")

# Iterative Binary Search Test (on sorted list)
index, comparisons = binary_search_with_count(sorted_test_list, target)
print(f"Binary Search (iterative): Index of {target} is {index}, Comparisons made: {comparisons}")

# Recursive Binary Search Test (on sorted list)
index, comparisons = binary_search_recursive_with_count(sorted_test_list, target, 0, len(sorted_test_list) - 1)
print(f"Binary Search (recursive): Index of {target} is {index}, Comparisons made: {comparisons}")


print('\nExercise4')

import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))  # Block size to jump
    comparisons = 0  # Initialize comparison counter
    
    # Finding the block where the target is present
    prev = 0
    while min(step, n) < n and arr[min(step, n) - 1] < target:
        comparisons += 1
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1, comparisons  # Return -1 if not found
    
    # Linear search within the identified block
    while prev < min(step, n):
        comparisons += 1
        if arr[prev] == target:
            return prev, comparisons  # Return index and comparisons if found
        prev += 1
    
    return -1, comparisons  # Return -1 and comparisons if not found


import time

def compare_search_algorithms(arr, target):
    # Linear Search
    start_time = time.time()
    linear_result, linear_comparisons = linear_search_with_count(arr, target)
    linear_time = time.time() - start_time
    
    # Binary Search (on sorted array)
    start_time = time.time()
    binary_result, binary_comparisons = binary_search_with_count(arr, target)
    binary_time = time.time() - start_time
    
    # Jump Search (on sorted array)
    start_time = time.time()
    jump_result, jump_comparisons = jump_search(arr, target)
    jump_time = time.time() - start_time
    
    # Print Results
    print("Linear Search: ", f"Index: {linear_result}, Comparisons: {linear_comparisons}, Time: {linear_time:.6f} seconds")
    print("Binary Search: ", f"Index: {binary_result}, Comparisons: {binary_comparisons}, Time: {binary_time:.6f} seconds")
    print("Jump Search:  ", f"Index: {jump_result}, Comparisons: {jump_comparisons}, Time: {jump_time:.6f} seconds")

# Test the function with a sorted list and a target
sorted_list = list(range(1, 10001))
target = 8888
compare_search_algorithms(sorted_list, target)