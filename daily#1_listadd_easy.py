'''
This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
'''
def add_up_to(k, array):
    #Sorting and reverse sorting the list so that I'm sure to match up all the different nums
    sorted_array = sorted(array, reverse=False)
    reverse_array = sorted(array, reverse=True)
    #Looping through pairings
    for num1 in sorted_array:
        for num2 in reverse_array:
            #If they add up to K return True
            if num1 + num2 == k:
                return True
    return False
        
array = [10, 7, 2, 3]
k = 17
print(f'Does any two numbers in {array} add up to {k}?', add_up_to(k, array))