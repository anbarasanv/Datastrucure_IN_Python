''' Singly linked list implementation for append node at the End '''
class Node():
  '''This class used to create new node'''
  def __init__(self, value):
        self.value = value #List value will be stored here
        self.next = None #By default node next will be none

#creating linkedlist class
class Linkedlist():
    '''This class used to create link between nodes'''
    #This constructor will initiate the link as head
    def __init__(self,head = None):
      self.head = head
    #This function will apppend linked list at end
    def append(self, element):
      current = self.head
      if self.head:
        while current.next:
          current = current.next
        current.next = element
      else:
        self.head = element
    def display(self):
      current = self.head
      if self.head:
        while current.next:
          print(current.value,end='-->')
          current = current.next
        print(current.value)
      else:
        print("List is empty")

#Asking user input for number of elements need to be insert
n = int(input("Enter the number of nodes: "))
assert type(n) is  int , "Please enter the input in integer" 
#Creating linkedList Object
link = Linkedlist()
#Loop for creating list
for i in range(0,n):
  value = input("Please enter the {}th node: ".format(i+1))
  node = Node(value)
  link.append(node)
link.display()
