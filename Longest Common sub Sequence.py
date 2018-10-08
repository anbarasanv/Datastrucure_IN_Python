__author__ = "Anbarasan"
def LCS(A,B):
  '''Function for Longest common Sub Sequence'''
  len_A = len(A)
  len_B = len(B)
  #Creating 2D resulting list with the length one more than two string.
  result = [[None]*(len_B+1) for i in range(len_A+1)]

  for i in range(len_A+1):
    for j in range(len_B+1):
      #filling 0th row and column with 0
      if i == 0 or j == 0:
        result[i][j] = 0
      #If any of the charecter matches from the two string
      elif A[i-1] == B[j-1]:
        #Adding 1 with diagonal cell value
        result[i][j] = 1+result[i-1][j-1]
      else:
        #If does not matches any of the charecter from two string
        #will select max of previous cell and top cell
        result[i][j] = max(result[i-1][j],result[i][j-1])
  return result[len_A][len_B]

if __name__ == '__main__':
#Test Cases 
  #Test Case: 01
  A = "AGGTAB"
  B = "GXTXAYB"
  result = LCS(A, B)
  assert result == 4, 'Test Case: 01 Failed'

  #Test Case: 02
  C= "STONE"
  D = "LONGEST"
  result = LCS(C, D)
  assert result == 3, 'Test Case: 02 Failed'

  print ("Cleared all the test cases!")
