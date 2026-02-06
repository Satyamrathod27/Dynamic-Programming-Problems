def max_subarray1(array):
    max_sum = array[0]
    curr_sum = array[0]

    for i in range(1,len(array)):
        curr_sum = max(curr_sum,curr_sum+array[i])
        max_sum = max(max_sum,curr_sum)
    return max_sum

numbers = [-1, 2, -4, 1, 4, 5, 6, -5, -2, 5]
print(max_subarray1(numbers))