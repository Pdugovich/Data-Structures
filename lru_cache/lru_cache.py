from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.order = DoublyLinkedList()
        self.storage = dict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # Key is not in cache - return none
        if key not in self.storage:
            return None
        else:
            # key is in cache
            # move it to recently used
            node = self.storage[key]
            self.order.move_to_end(node)
            # return value
            return node.value[1]



    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # Different scenarios

        # If item/key already exists
        if key in self.storage:
            # overwrite the value
            # Where is the value stored
            node = self.storage[key]
            node.value = (key, value)
            self.order.move_to_end(node)
            return

        # size at limit
        if len(self.order) == self.limit:
            # Evict the oldest one
            # We need to remove the references and the dictonary
            # The oldest is the head, and the value[0] is the key
            #in the tuple
            index_of_oldest = self.order.head.value[0]
            # This deletes that from the dict
            del self.storage[index_of_oldest]
            # Then we know it was the head, so we just remove the head
            self.order.remove_from_head()


        # add to order
        self.order.add_to_tail((key, value))
        # add to storage
        self.storage[key] = self.order.tail



