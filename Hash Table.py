#has Table implementation
class HashTable(object):
  '''Hash Table class'''
  def __init__(self,slot=10):
    '''constructor of the has table'''
    self.slot = slot
    self.table = []
    self.create_table()

  def create_table(self):
    '''Hash table create function'''
    for i in range(self.slot):
      #append the slot number of empty list to main table list
      self.table.append([])
  
  def hash_key(self,value):
    '''calculates the hash key using value and slot'''
    #using modulo because of get a round value for index of main table
    return hash(value)%self.slot

  def add_item(self,value):
    '''Adding new items to the has table'''
    key = self.hash_key(value)
    self.table[key].append(value)

  def find_item(self,value):
    '''Searc function for the has table'''
    #find has value and search according to that key value
    value_hash = self.hash_key(value)
    return value in self.table[value_hash]
  
  def print_table(self):
    for key in range(self.slot):
      print('key is {}, value is {}'.format(key,self.table[key]))

if __name__ == '__main__':
  dic = HashTable(5)
  for i in range(1,40,2):
    dic.add_item(i)
  dic.print_table()
#Test Cases
  #Test Case: 01
  assert dic.find_item(20) == False, 'Test Case: 01 failed!'
  #Test Case: 02
  assert dic.find_item(21) == True, 'Test Case: 02 failed!'
