import timeit
class Node:
  '''This Class Creates node's for Tree'''
  def __init__(self, data=None):
    self.left = None
    self.right = None
    self.data = data
#Node Insertion function
def insertNode(root,node):
  '''This function insert the nodes to the Tree'''
  #Base case
  if root is None:
    root = node
  else:
    #if data greater than or equal to root data will be inserted at the right side of the root
    if root.data <= node.data:
      if root.right is None:
        root.right = node
      else:
        insertNode(root.right,node)
    else:
     #if data smaller than the root data will be inserted at the left side of the root
      if root.left is None:
        root.left = node
      else:
        insertNode(root.left,node)

#Inorder treversal function 
def inOrder(root):
  '''This function treverse to the node's as inorder Left-Root-Right'''
  if root:
    inOrder(root.left)
    print(root.data)
    inOrder(root.right)
#Function for searching a value in the Tree
def search(root, data):
  '''This function return the data node or None if not found'''
  #Base Case
  if (root == None or root.data == data):
    return root
  #If data greater than root, will search right side of the root 
  if root.data < data:
    return search(root.right,data)
  #If data smaller than root, will search left side of the root 
  return search(root.left,data)

def findMin(node):
  '''This function finds the left most value of the right sub tree'''
  current = node
  while (current.left is not None):
    current = current.left
  return current
  
#Function for delete a node from the tree
def deleteNode(root, data):
  '''This function deletes a Node in a tree if passed data found'''
  #Base Case
  if root is None:
    return root
  if data < root.data:
    #data less than root data search will begin from left
    root.left = deleteNode(root.left,data)
  elif data > root.data:
    #data greater than root data search will begin from right
    root.right = deleteNode(root.right,data)
  
  else:
    #Case:01 No child
    if root.left is None and root.right is None:
      root = None
      return root
    
    #Case:02 only one child
    if root.left is None:
      temp = root.right
      root = None
      return temp
    elif root.right is None:
      temp = root.left
      root = None
      return temp
    
    #Case:03 Two children
    temp = findMin(root.right)
    root.data = temp.data
    root.right = deleteNode(root.right,temp.data)
  return root
  

    
 
    


root = Node(50)
insertNode(root, Node(30))
insertNode(root, Node(20))
insertNode(root, Node(40))
insertNode(root, Node(70))
insertNode(root, Node(60))
insertNode(root, Node(80))
strtime = timeit.timeit()
res = search(root, 30)
stptime = timeit.timeit()
print("Searching for key: 30")
if res:
  print("\nKey has been found: {}".format(res.data))
  print("\nSearch Time: {}".format(strtime-stptime))
else:
  print("Key does not found!")
  print("\nSearch Time: {}".format(strtime-stptime))
print("\nBefore the deletion:")
inOrder(root)
strtime = timeit.timeit()
deleteNode(root,70)
stptime = timeit.timeit()
print("\nAfter the deletion:")
print("\nDelete Time: {}".format(strtime-stptime))
inOrder(root)


