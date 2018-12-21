import sys
def maxSubArray(arr, f, l):
  #Check for the base case
  if(f==l):
    return arr[l]

  #Finding the min
  m = (f+l)//2

  return(max(
    maxSubArray(arr,f,m),
    maxSubArray(arr,m+1, l),
    maxCrossSubArray(arr, f, m, l)
  ))
  


def maxCrossSubArray(arr, f, m, l):
  left_max = -sys.maxsize-1
  lsm = 0
  for j in range(m,f-1,-1):
    lsm +=arr[j]
    if(lsm>left_max):
      left_max = lsm

  right_max = -sys.maxsize-1
  rsm = 0

  for i in range(m+1, l+1):
    rsm +=arr[i]
    if(rsm > right_max):
      right_max = rsm


  return left_max+right_max



lst =  [2, 3, 4, 5, 7] 


l = len(lst)-1
maxSum = maxSubArray(lst, 0,  l)

print("\nMax sum of contigious sub Array: ",maxSum)
