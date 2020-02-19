my_list = [5, 9, 3, 7, 2, 8, 1, 6]

def partition(data):
    left = []
    pivot = data[0]
    right = []

    for item in data[1:]:
        if item < pivot: 
            left.append(item)
        else: #Handling > or = 
            right.append(item)

    return left, pivot, right

    

