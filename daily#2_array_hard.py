'''
This problem was asked by Uber.
Given an array of integers, return a new array such that each element at index i of the new array is the 
product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be 
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?
'''

def product_arr(array):
    new = []
    i = 0
    while i < len(array):
        total = 1
        for j, num in enumerate(array):
            total *= num
            if j == len(array)-1:
                new.append(int(total/array[i]))
        i += 1
    return new

array1 = [1, 2, 3, 4, 5]
array2 = [3, 2, 1]
print(product_arr(array2))



def product_arr_no_division(array):
    new = []
    i = 0
    while i < len(array):
        total = 1
        for j, num in enumerate(array):
            #Multiply if number is not the one at index i 
            if array[i] != num:
                total *= num
            if j == len(array)-1:
                new.append(int(total))
        i += 1
    return new


array1 = [1, 2, 3, 4, 5]
array2 = [3, 2, 1]
print(product_arr_no_division(array1))