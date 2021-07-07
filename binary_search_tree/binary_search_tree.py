import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack



# Questions:
# Only ints? 
# Negative numbers?

# Observations
# >= goes right
# Need to traverse to delete
# When deleting, the smallest child becomes parent


class BinarySearchTree:
  def __init__(self, value): # We're just using value, so key is value
    self.value = value
    self.left = None
    self.right = None

  # * `insert` adds the input value to the binary search tree, adhering to the
  # rules of the ordering of elements in a binary search tree.
  # Need to traverse to find spot to insert
  def insert(self, value):
    if self.value is None:
      self.value = value
    #Current node is self
    #Check if self.value is bigger or smaller than new value - left or right
    else:
      if value < self.value:
      #We go left or right, then check if node exists
        if not self.left:
        #if node does not exist than create a node there
          self.left = BinarySearchTree(value)
      #if node does exist use recursion! Call insert on that node
        else:
          self.left.insert(value)
        #we go right
      else:
        if not self.right:
          self.right = BinarySearchTree(value)
        else:
          self.right.insert(value)

  # * `contains` searches the binary search tree for the input value, 
  # returning a boolean indicating whether the value exists in the tree or not.
  # Start from root and traverse the tree
  # We can stop at the first instance of a value
  # We know it's not found if we get to a node that doesn't have children
  def contains(self, target):
    #Check if the current value is the target, if so, we're done
    if self.value == target:
      return True
    #Otherwise, left or right based on bigger or smaller, and then call contains again
    else:
      if target < self.value:
        #go left
        if not self.left:
          return False
        else:
          return self.left.contains(target)
      else:
        #go right
        if not self.right:
          return False
        else:
          return self.right.contains(target)
        
  # * `get_max` returns the maximum value in the binary search tree.
  def get_max(self):
    #max node is farthest to the right
    #base case:
    # if not self.right:
    #   return self.value
    # return self.right.get_max()
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value

  # * `for_each` performs a traversal of _every_ node in the tree, executing
  # the passed-in callback function on each tree node value. There is a myriad of ways to
  # perform tree traversal; in this case any of them should work. 
  def for_each(self, cb):
    cb(self.value) 
    if self.left:
      self.left.for_each(cb)
    if self.right:
      self.right.for_each(cb)




# DAY 2 Project -----------------------

  # Print all the values in order from low to high
  # Hint:  Use a recursive, depth first traversal
  def in_order_dft(self, node):
    if node.left:
      node.in_order_dft(node.left)
    print(node.value)
    if node.right:
      node.in_order_dft(node.right)



  # Print the value of every node, starting with the given node,
  # in an iterative breadth first traversal
  def bft_print(self, node):
    q = Queue()
    q.enqueue(node)
    current_node = node
    while q.size != 0:
      cur_node = q.dequeue()
      print(current_node.value)
      if cur_node.left:
        q.enqueue(current_node.left)
      if cur_node.right:
        q.enqueue(current_node.right)
      


  # Print the value of every node, starting with the given node,
  # in an iterative depth first traversal
  def dft_print(self, node):
    print(node.value)
    if node.right:
      self.dft_print(node.right)
    if node.left:
      self.dft_print(node.left)
          

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
    