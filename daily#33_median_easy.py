'''
This problem was asked by Microsoft.
Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.
Recall that the median of an even-numbered list is the average of the two middle numbers.
'''

def median(array):
    sorted_list = []
    for element in array:
        sorted_list.append(element)
        sorted_list.sort()
        length = len(sorted_list)
        half = int(length / 2)
        if length % 2 == 0:
            median = (sorted_list[half-1] + sorted_list[half])/2
            print(median)
        else:
            median = sorted_list[half]
            print(median)











median([2, 1, 5, 7, 2, 0, 5])