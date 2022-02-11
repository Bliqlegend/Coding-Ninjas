def merge(arr,start,mid,end):
    n1 = arr[start:mid]
    n2 = arr[mid+1:end]
    a = []
    b = []
    for i in range(n1):
        a[i] = arr[start+i]
    for i in range(n2):
        b[i] = arr[mid+1+i]
    i , j,k = 0,0,0
    while i<n1 and j<n2:
        if a[i]<b[j]:
            arr[k] = a[i]
            k+=1
            i+=1
        else:
            arr[k] = b[j]
            k+=1
            j+=1
    # if any of the subarrays is not finished
    while i<n1:
        arr[k] = a[i]
        i+=1
        k+=1
    while j<n2:
        arr[k] = b[j]
        j+=1
        k+=1


def mergeSort(arr,start,end):
    mid = int(len(arr)/2)
    mergeSort(arr,start,mid)
    mergeSort(arr,mid+1,end)
    merge(arr,start,mid,end)


arr = [int(ele) for ele in input().split()]

mergeSort(arr,0,len(arr))