def swap(arr,i,j):
    arr[i],arr[j] = arr[j],arr[i] 
    return arr

def bubbleSort(arr):
    counter = 1
    while counter<len(arr):
        for i in range(len(arr)-counter):
            if arr[i] > arr[i+1]:
                arr = swap(arr,i,i+1)
        counter+=1
    
    return arr

arr = [int(ele) for ele in input().split()]
print(bubbleSort(arr))
