def findlargest(arr):
    secondlargest = 0
    largest = min(arr)
    for i in range (len(arr)):
        if arr[i] > largest:
            secondlargest = largest
            largest =arr[i]
        else:
            secondlargest = max(secondlargest, arr[i])
    return secondlargest           
print(findlargest([10,40,60,70,90,76]))