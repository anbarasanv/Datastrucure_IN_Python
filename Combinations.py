#combination:
'''A collection of things, in which the order does not matter.'''
def combination(arr):
  '''This function returns the combinations of given list'''
  #Base Cases
  if len(arr) == 0:
    return set([''])
  elif len(arr) == 1:
    return set(arr)
  else:
    result = set()
    #enumerating the input array
    for index,item in enumerate(arr):
      #creating the new array with except current element
      new_arr = arr[:index]+arr[index+1:]
      #appending current element
      result.add(item)
      #recursion for newly created array
      for p in combination(new_arr):
        #joing the cuurent element with combination of new_array
        #sorted function will eliminate same kind of combinatiions
        new_item = ''.join(sorted(item+p))
        result.add(new_item)
  return result

if __name__ == '__main__':
  #Test case: 01
  array = list('abc')
  result = set(['b', 'a', 'ab', 'c', 'bc', 'ac', 'abc'])
  assert (combination(array)==result), 'Test case: 01 failed'
  #Test case: 02
  array = list('a')
  result = set(['a'])
  assert (combination(array)==result), 'Test case: 02 failed'
  #Test case: 03
  array = list('')
  result = set([''])
  assert (combination(array)==result), 'Test case: 03 failed'

  print("All the test cases has been passed!")

