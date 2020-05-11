def bubble_sort(array):
    # Quadratic complexity: Θ(n²)
    # Largest unsorted element always at end after pass,
    # so at most n pases

    # Create local copy
    array = list(array)
    n = len(array)
    while True:                 # Θ(n)
        swapped = False
        for i in range(n-1):    # Θ(n)
            # Compare consecutive pair
            if array[i] > array[i+1]:
                # Swap them if unsorted
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True
        # Stop when no more swaps have been made
        if not swapped:
            break
    return array


def selection_sort(array):
    # Quadratic complexity: Θ(n²)
    # Smallest unsorted element always at start after pass,
    # so at most n pases

    # Create local copy
    array = list(array)
    n = len(array)
    for i in range(n-1):            # Θ(n)
        # Find minimum element in array[i:end]
        # (but do NOT actually slice, no need to copy)
        min_index = i
        for j in range(i+1, n):     # Θ(n)
            if array[j] < array[min_index]:
                min_index = j
        # Swap it with the i-th element
        array[i], array[min_index] = array[min_index], array[i]
    return array


def merge_sort_slicing(array):
    # Slicing is not efficient, but algorithm is clearer
    array = list(array)
    n = len(array)
    if n == 1:
        return [array[0]]
    else:
        middle = n//2
        sublist_1 = merge_sort_slicing(array[:middle])
        sublist_2 = merge_sort_slicing(array[middle:])
        # Merge the two lists
        result = []
        while len(sublist_1) > 0 and len(sublist_2) > 0:
            if sublist_1[0] < sublist_2[0]:
                result.append(sublist_1.pop(0))
            else:
                result.append(sublist_2.pop(0))
        # Copy the not empty list to the end of result
        result.extend(sublist_1 or sublist_2)
        return result


def merge_sort(array):
    array = list(array)
    start = 0
    stop = len(array)

    def merge_sort_helper(start, stop):
        n = stop - start
        if n == 1:
            return [array[start]]
        else:
            middle = start + n//2
            left = merge_sort_helper(start, middle)     # Θ(log n)
            right = merge_sort_helper(middle, stop)     #

            return merge(left, right)                   # Θ(n)

    def merge(left, right):
        # Merge the two lists in ascending order
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # Copy the not empty list to the end of result
        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(right):
            # print(j, stop, right)
            result.append(right[j])
            j += 1
        return result

    return merge_sort_helper(start, stop)
