def merge_sort(a):
    """Divide and conquer sorting algorithm
    Recursively divide array"""
    if len(a) <= 1:  # base case
        return a
    # Divide array down the middle
    mid = len(a) // 2
    left, right = a[:mid], a[mid:]
    # Recursively divide new arrays
    left = merge_sort(left)
    right = merge_sort(right)
    # Return merged arrays
    return merge(left, right)


def merge(left, right):
    """Merge left and right lists of numbers"""
    merged_list = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            j += 1
    while i < len(left):
        merged_list.append(left[i])
        i += 1
    while j < len(right):
        merged_list.append(right[j])
        j += 1
    return merged_list


def main():
    b = merge_sort([3, 2, 1, 6, 4, 5, 6])
    print(b)


if __name__ == "__main__":
    main()
