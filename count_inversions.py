def sort_and_count(array):
    """Divide and conquer counting inversion algorithm"""
    if len(array) <= 1:  # base case
        return array, 0
    # Find mid point
    mid = len(array) // 2
    # Recursively divide new arrays
    left, inv_left = sort_and_count(array[:mid])
    right, inv_right = sort_and_count(array[mid:])
    merged_list, inv_split = merge_count_split(left, right)
    # Return merged arrays and number of inversions
    return merged_list, inv_split + inv_left + inv_right


def merge_count_split(left, right):
    """Merge left and right lists of numbers
    Keep track of number of split inversions
    """
    merged_list = []
    i, j = 0, 0
    count = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_list.append(left[i])
            i += 1
        elif right[j] < left[i]:
            merged_list.append(right[j])
            j += 1
            count += len(left) - i
    merged_list += left[i:]
    merged_list += right[j:]
    return merged_list, count


def main():
    result, inv_count = sort_and_count([1, 3, 5, 2, 4, 6])
    print(result)
    print(inv_count)


if __name__ == "__main__":
    main()
