# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = [0 for i in range(len( arrA ) + len( arrB ))]
    # merged_arr = [0] * elements
    print()
    # TO-DO
    a = 0 
    b = 0 
    c = 0

    arrC = []

    
    while arrA[a] < len(arrA) and arrB[b] < len(arrB): 
        if arrA[a] < arrB[b]:
            arrC[c] = arrA[a]
            c = c + 1
            a = a + 1
        else: 
            arrC[c] = arrB[b]
            c = c + 1
            b = b + 1 
        
    while a < len(arrA): 
        arrC[c] = arrA[a]
        c = c + 1
        a = a + 1 

    while b < len(arrB):
        c = c + 1
        b = b +1 



    print(arrC)
    return arrC

merge([1, 2], [3, 4])

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
