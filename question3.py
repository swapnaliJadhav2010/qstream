
def sum_pair(int_array, target):
  for index, num in enumerate(int_array):
    # as only 1 pair will be there in list so no need to go through all
    # if we get the pair at the beginning
    difference = target - num
    if difference in int_array:
      return [index, int_array.index(difference)]

print(sum_pair([1, 2, 3, 7], 8)) # [0,3]
print(sum_pair([1, 2, 3, 6], 8)) # [1,3]
print(sum_pair([1, 2, 3, 5], 8)) # [2,3]