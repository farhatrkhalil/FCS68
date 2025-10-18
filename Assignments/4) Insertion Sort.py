# Insertion sort how does it work?
# --------------------------------------------------------
# It works similarly to the way people often sort playing cards in their hands. 
# --------------------------------------------------------
# Here's how it works step-by-step:
# 1. Start with the second element of the array (the first element is considered sorted).
# 2. Compare the current element with the elements in the sorted portion (to its left).
# 3. Shift all elements in the sorted portion that are greater than the current element to the right.
# 4. Insert the current element into its correct position in the sorted portion.
# --------------------------------------------------------
def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)): #Because we start sorting from the second element in the list (index 1).
        key = arr[i]  # The current element to be inserted
        j = i - 1     # The last index of the sorted portion (start comparing backwards)

        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  # Shift element to the right (insertion step not replacing)
            j -= 1

        # Place the key in its correct position
        arr[j + 1] = key

    return arr

# Example usage:
if __name__ == "__main__":
    sample_array = [12, 11, 13, 5, 6]
    sorted_array = insertion_sort(sample_array)
    print("Sorted array is:", sorted_array)
# This will output: Sorted array is: [5, 6, 11, 12, 13]
# The time complexity of Insertion Sort is O(n^2) in the worst case,but it performs well on small 
# or nearly sorted datasets.