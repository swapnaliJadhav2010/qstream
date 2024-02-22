
def flatten_lists(nested_list):
  result = []
  for element in nested_list:
    # check if the element is a list
    if isinstance(element, list):
      # use recursion to check the presence of nested lists
      result.extend(flatten(element))
    else:
      result.append(element)
  return result

print(flatten_lists([[0, 1, [3,5,[6]]], [5, [7]]]))