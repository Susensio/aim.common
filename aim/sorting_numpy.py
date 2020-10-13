import numpy as np


def selection_sort(array):
    # Quadratic complexity: Θ(n²)
    # Smallest unsorted element always at start after pass,
    # so at most n pases

    array = np.array(array)
    n = array.size
    for i in range(n-1):                    # Θ(n)
        # Find minimum element in array[i:end]
        min_index = array[i:].argmin()+i    # Θ(n)
        # Swap it with the i-th element
        array[i], array[min_index] = array[min_index], array[i]
    return list(array)


def merge_sort(array):
    # SLOWER THAN REGULAR PYTHON!!!
    # TODO: without recursion??
    array = np.array(array)

    def helper(array):
        n = array.size
        if n == 1:
            return array[0:1]
        else:
            middle = n//2
            left = helper(array[:middle])
            right = helper(array[middle:])
            # Merge the two lists
            result = np.empty(left.size + right.size)
            i = i_r = i_l = 0
            while i_l < left.size and i_r < right.size:
                if left[i_l] < right[i_r]:
                    result[i] = left[i_l]
                    i_l += 1
                else:
                    result[i] = right[i_r]
                    i_r += 1
                i += 1
            # Copy the not empty list to the end of result
            if i_l < left.size:
                result[i:] = left[i_l:]
            elif i_r < right.size:
                result[i:] = right[i_r:]
            return result

    return list(helper(array))
