class LinkedList():
  
  def __init__(self, head=None):
    self.head = head

  def insert(self, data):
    new_node = Node(data)
    new_node.set_data(self.head)
    self.head = new_node

  def sizeof(self):
    current = self.head
    count = 0
    while(current):
      current = current.get_next()
      count +=1
    return count

  def search(self, data):
    current = self.head
    found = False

    while current and found is False:
      
      if current.get_data() == data:
        found = True
        print("Data is found in the list")
      else:
        current = current.get_next()
    if current is None:
      raise ValueError("Data is not in the list")

  def delete(self, data):
    temp = self.head

    #checking the data with head
    if(temp.data == data):
      self.head = temp.next
      temp = None
      print("Data has been removed!")
      return
    
    while(temp is not None):
      if temp.data == data:
        break
      prev = temp
      temp = temp.next

    if(temp == None):
      print("Data not in the list")
    
    prev.next = temp.next
    temp = None
    print("Data has been removed")
