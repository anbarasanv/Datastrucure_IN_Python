from itertools import permutations,combinations

a = [1,2,3,4]
#Only one argument array or list
b = permutations(a)
#Will have Two arguments 1'st array or list, 2'nd length of combinations 
c = combinations(a,2)

for i in b:
  print(i)
print('-------------------')
for i in c:
  print(i)
