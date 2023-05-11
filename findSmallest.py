def findSmallest(arr):
    smallest= arr[0]
    smallest_index=0
    for i in range(1, len(arr)):
        if arr[i]< smallest:
            smallest_index=i 
            smallest= arr[i]
    return smallest_index

def sortArray(arr):
    sortArray= []
    for i in range(len(arr)):
        smallest=findSmallest(arr)
        sortArray.append(arr.pop(smallest))
    return sortArray

prueba = [12,1,7,3,6,0]
findSmallest(prueba)
print ( sortArray([2,5,3,1,8]))