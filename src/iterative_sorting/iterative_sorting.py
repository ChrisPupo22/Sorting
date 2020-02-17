# TO-DO: Complete the selection_sort() function below 


arr = [81, 9, 22, 7, 1,]
def selection_sort(arr):
    # loop through n-1 elements
    for a in range(0, len(arr) -1):
        smallest_index = a 
        #must find the next smallest index through another for loop
        for j in range(a + 1, len(arr)):
            if arr[j] < arr[smallest_index]: 
                smallest_index = j
        if smallest_index != a: 
            arr[smallest_index], arr[a] = arr[a], arr[smallest_index]

    return arr

print(selection_sort(arr))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr