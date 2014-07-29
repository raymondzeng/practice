class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)
        
class LinkedList:
    """
    Singly linked-list
    
    Remove from head is O(1)
    Remove from tail is O(n) ** not supported
    Remove from middle is O(n) 
    Append at end is O(1)
    Append at head is O(1) ** not supported
    """
    
    def __init__(self, list):
        node = Node(list[0]) if list else None
        self.head = node
        self.tail = node
        
        curr = self.head
        for val in list[1:]:
            curr.next = Node(val)
            curr = curr.next

    def to_top(self, val):
        """
        move 'val' to tail of list; checks if it's already tail, otherwise has to remove it from the list
        """
        if self.tail == val:
            return

        self.remove(val)
        self.append(val)

    def pop_head(self):
        """ 
        removes the head of the list and returns the value of that node
        """
        val = self.head.val
        self.head = self.head.next
        return val

    def append(self, val):
        if self.tail is not None:
            self.tail.next = Node(val)
            self.tail = self.tail.next
        else:
            self.head = Node(val)
            self.tail = self.head

    def remove(self, val):
        """
        remove val from ll, throw error if does not exist
        """
        prev = None
        curr = self.head
        while curr is not None:
            if curr.val == val:
                if prev is None:
                    self.head = curr.next
                else:
                    prev.next = curr.next
                if curr == self.tail:
                    self.tail = prev
                return
            prev, curr = curr, curr.next

        raise KeyError(val)
        
    def __str__(self):
        """
        string rep. of the linked list
        """
        l = []
        curr = self.head
        while curr is not None:
            l.append(curr.val)
            curr = curr.next
        return str(l)








class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)
        
class LinkedList:
    """
    Singly linked-list
    
    Remove from head is O(1)
    Remove from tail is O(n) ** not supported
    Remove from middle is O(n) 
    Append at end is O(1)
    Append at head is O(1) ** not supported
    """
    
    def __init__(self, list):
        node = Node(list[0]) if list else None
        self.head = node
        self.tail = node
        
        curr = self.head
        for val in list[1:]:
            curr.next = Node(val)
            curr = curr.next

    def pop_head(self):
        """ 
        removes the head of the list and returns the value of that node
        """
        val = self.head.val
        self.head = self.head.next
        return val

    def append(self, val):
        if self.tail:
            self.tail.next = Node(val)
            self.tail = self.tail.next
        else:
            self.head = Node(val)
            self.tail = self.head



    def to_top(self, val):
        """
        move 'val' to tail of list; checks if it's already tail, otherwise has to remove it from the list
        """
        if self.tail == val:
            return

        self.remove(val)
        self.append(val)


    def remove(self, val):
        """
        remove val from ll, throw error if does not exist
        """
        prev = None
        curr = self.head
        while curr is not None:
            if curr.val == val:
                if prev is None:
                    self.head = curr.next
                else:
                    prev.next = curr.next
                    
                if curr == self.tail:
                    self.tail = prev
                return
            prev, curr = curr, curr.next

        raise KeyError(val)
        
    def __str__(self):
        """
        string rep. of the linked list
        """
        l = []
        curr = self.head
        while curr is not None:
            l.append(curr.val)
            curr = curr.next
        return str(l)

"""
LRU cache using a linkedlist to keep track of recency

get  -  O(n) (due to linkedlist removal)
set  -  O(n) (due to linkedlist removal)
"""
class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.store = {}
        self.queue = LinkedList([])

    # @return an integer
    def get(self, key):
        try:
            val = self.store[key]
            
            # update the recency queue
            self.queue.to_top(key)
        except:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if len(self.store) == self.capacity:
            del self.store[self.queue.pop_head()]

        self.store[key] = value
        try:
            self.queue.remove(key)
        except:
            pass
        self.queue.append(key)


"""
LRU cache using collections.OrderedDict so recency is kept track of by the container. 

Don't know how OrderedDict works so can't speak for hte efficiency but it's faster than the linkedlist 
"""
class LRUCache:
    import collections
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1

    def set(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value
