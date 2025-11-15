def mergesort(arr):
    if len(arr) <= 1:
        return arr

    prev = len(arr) // 2
    left = mergesort(arr[:prev])
    right = mergesort(arr[prev:])

    return merge(left,right)

def merge(left,right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1



    result.extend(left[i:])
    result.extend(right[j:])


    return result



