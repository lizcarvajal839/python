class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def append(self, data):
    new_node = Node(data)
    if self.head is None :
      self.head=new_node
      return
    lastNode= self.head
    while lastNode.next:
        lastNode=lastNode.next
    lastNode.next= new_node
    
      



