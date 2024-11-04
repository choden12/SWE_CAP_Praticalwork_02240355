# Exercise 1

def in_place_quick_sort(arr, low=0, high=None):
    # Set the initial high value to the last index if not provided
    if high is None:
        high = len(arr) - 1

    # Base condition to stop recursion
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = partition(arr, low, high)
        # Recursively sort the left half
        in_place_quick_sort(arr, low, pivot_index - 1)
        # Recursively sort the right half
        in_place_quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    # Choose the last element as the pivot
    pivot = arr[high]
    i = low - 1  # Index of the smaller element

    # Iterate through the array and rearrange elements based on the pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1  # Increment the index of the smaller element
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements

    # Swap the pivot element to the correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # Return the pivot index

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
in_place_quick_sort(test_arr)
print("In-place Quick Sort Result:", test_arr)


# Exercise 2

def optimized_bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        swapped = False  # Track if any swapping happens in this pass
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            # Swap if the current element is greater than the next
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # Mark that a swap occurred

        # If no elements were swapped, the array is already sorted
        if not swapped:
            break
    return arr

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = optimized_bubble_sort(test_arr.copy())
print("Optimized Bubble Sort Result:", sorted_arr)


# Exercise 3

def hybrid_merge_sort(arr, threshold=10):
    # If the array size is below the threshold, use Insertion Sort
    if len(arr) <= threshold:
        return insertion_sort(arr)
    else:
        # Divide the array into two halves
        mid = len(arr) // 2
        # Recursively sort the left and right halves
        left = hybrid_merge_sort(arr[:mid], threshold)
        right = hybrid_merge_sort(arr[mid:], threshold)
        # Merge the sorted halves
        return merge(left, right)

def insertion_sort(arr):
    # Traverse from 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1] that are greater than key
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Place the key in the right position
    return arr

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = hybrid_merge_sort(test_arr)
print("Hybrid Merge Sort Result:", sorted_arr)


# Exercise 4

import matplotlib.pyplot as plt
import time

def visualize_bubble_sort(arr):
    # Set up the plot for interactive visualization
    plt.ion()
    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(len(arr)), arr, align="edge")
    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, int(1.1 * max(arr)))

    # Perform bubble sort with visualization
    for i in range(len(arr)):
        swapped = False  # Track if any swapping happens in this pass
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap elements
                swapped = True  # Mark that a swap occurred

                # Update the bar heights to show changes
                for rect, val in zip(bar_rects, arr):
                    rect.set_height(val)
                plt.pause(0.05)  # Pause to create the animation effect
        
        # If no swapping occurred, break early as the array is sorted
        if not swapped:
            break
    
    # Turn off interactive mode and display the final result
    plt.ioff()
    plt.show()

# Test the function with visualization
test_arr = [64, 34, 25, 12, 22, 11, 90]
visualize_bubble_sort(test_arr)
