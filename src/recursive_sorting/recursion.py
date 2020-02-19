
# Print every number starting at 'number', until you reach 0
# def recurse(number): 
#     if number == 0: 
#         return 
#     print(number)
#     number -= 1
#     recurse(number)

# recurse(5)

def fibonacci(n): 
    if n < 0: 
        print("negative numbers do not work")
    if n == 0:
        return 0 
    elif n == 1: 
        return 1
    else: 
        #return (n-1) + (n-2) 
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))