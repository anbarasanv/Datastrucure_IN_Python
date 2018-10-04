#permutation:
'''A collection of things, in which the order does not matter.'''
def permutation(arr):
  '''This function returns the permutations of given list'''
  #Base Cases
  if len(arr) == 0:
    return []
  elif len(arr) == 1:
    return arr
  else:
    result = []
    #Iterationg through the input array
    for i in range(len(arr)):
      #creating the new array with except current element
      new_arr = arr[:i]+arr[i+1:]
      #recursion for newly created array
      for p in permutation(new_arr):
        #joing the cuurent element with permutation of new_array
        new_item = ''.join((arr[i]+p))
        result.append(new_item)
  return result

if __name__ == '__main__':
  #Test Case: 01
  data = list('abc')
  result = permutation(data)
  assert result == ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'], 'Test Case: 01 failed!'
  #Test Case: 02
  data = list('')
  result = permutation(data)
  assert result == [], 'Test Case: 02 failed!'
  #Test Case: 03
  data = list('a')
  result = permutation(data)
  assert result == ['a'], 'Test Case: 03 failed!'
  print("passed all the test cases!")
