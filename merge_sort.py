def merge_sort(a):
    if len(a) <= 1:
        return a

    mid = len(a) // 2
    left, right = a[:mid], a[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    print(left, right)
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


b = merge_sort([3, 2, 1, 6, 4, 5, 6])
print(b)
