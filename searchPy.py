list1 = [64, 34, 25, 12, 22, 11, 90]

def linearSearch(list1, key):
    for i in list1:
        if i == key:
            return True
    return False

print(linearSearch(list1, 120))
print(linearSearch(list1, 12))


#interpolation search

# If x is present in list1[0..n-1], then returns
# index of it, else returns -1
def interpolationSearch(list1, n, key):
    # Find indexs of two corners
    lo = 0
    hi = (n - 1)

    # Since list is sorted, an element present
    # in array must be in range defined by corner
    while lo <= hi and key >= list1[lo] and key <= list1[hi]:
        if lo == hi:
            if list1[lo] == key:
                return lo
            return -1

        # Probing the position with keeping
        # uniform distribution in mind.
        pos = lo + int(((float(hi - lo) /
                         (list1[hi] - list1[lo])) * (key - list1[lo])))

        # Condition of target found
        if list1[pos] == key:
            return pos

        # If key is larger, key is in upper part
        if list1[pos] < key:
            lo = pos + 1
        # If key is smaller, key is in lower part
        else:
            hi = pos - 1

    return -1

list1 = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
n = len(list1)

key = 19.5  # Element to be searched
index = interpolationSearch(list1, n, key)

if index != -1:
    print("Element found at index", index)
else:
    print("Element not found")


def binarySearch(arr, l, r, x):
    # Check base case
    if r >= l:

        mid = l + int((r - l) / 2)

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

            # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

            # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1

list1 = [2, 3, 4, 10, 40]
x = 40

result = binarySearch(list1, 0, len(list1) - 1, x)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")