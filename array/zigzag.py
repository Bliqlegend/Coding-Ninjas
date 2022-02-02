def swap(arr,i,j):
    arr[i],arr[j] = arr[j],arr[i]
    return arr


arr = [4,3,2,1]
arr.sort()
swap(arr,1,2)
print(arr)