'''
This problem was asked by Stripe.
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place.
'''

def smallest_linear_num(array):
    linear_array = [x for x in range(1, 50)]
    for num in array:
        if num in linear_array:
            linear_array.remove(num)
    return min(linear_array)

array1 = [3, 4, -1, 1]
array2 = [1, 2, 0]
print('First missing positive int:',smallest_linear_num(array2))