def BubbleSort(size,arr):

    for i in range(size):
        for j in range(size-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    
    for i in range(size):
        print(arr[i])

arr=[2,3,4,1,-3,2,2,-12]
size=len(arr)
BubbleSort(size,arr)
