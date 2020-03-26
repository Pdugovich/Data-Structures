import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        """
        check if empty
        if empty put node here/at root
        else
            if new < node.value
                leftnode.insert value
            if > =
                rightnode.insert value
        """
        if value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        # elif value == self.value:
        #     self.value = value


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        """
        if node is none
            return false
        if node.value == findvalue
            return True
        else
            if find < node.value
                find on left node
            else
                find on right node
        """
        # if self.value == None:
        #     return False
        if target == self.value:
            return True
        else:
            if target < self.value:
                if self.left == None:
                    return False
                else:
                    return self.left.contains(target)
            elif target > self.value:
                if self.right == None:
                    return False
                else:
                    return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        """
        if there's a right
            get max on right
        else
            return node.value
        """
        if self.right != None:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.right !=None:
            return self.right.for_each(cb)
        elif self.left !=None:
            return self.left.for_each(cb)
        # else:
        #    cb(self.value)
        #    del self

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
