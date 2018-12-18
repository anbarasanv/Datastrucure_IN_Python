class Node():
  '''This class creates node for liked list'''
  def __init__(self, data):
    self.data = data;
    self.next = None;

  def get_data(self):
    return self.data

  def get_next(self):
    return self.next

  def set_data(self, new_node):
    self.next = new_node
