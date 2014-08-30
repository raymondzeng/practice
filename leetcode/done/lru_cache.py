# Design and implement a data structure for Least Recently Used (LRU) cache. 
# It should support the following operations: get and set.

# get(key) - Get the value (will always be positive) of the key if the 
# key exists in the cache, otherwise return -1.
# set(key, value) - Set or insert the value if the key is not already present. 
# When the cache reached its capacity, it should invalidate the least 
# recently used item before inserting a new item.

class LRUCache:
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
