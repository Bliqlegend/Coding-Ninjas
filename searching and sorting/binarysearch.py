def binarySearch(arr,k):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            high = mid-1
        elif arr[mid] < k:
            low = mid + 1
    return -1

arr = [4,5,6,1,2,3]
k = 3
print(binarySearch(arr,k))