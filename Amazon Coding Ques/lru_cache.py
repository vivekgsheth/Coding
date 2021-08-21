from collections import OrderedDict

class LRUCache:
      
    def __init__(self,cap):       
        self.cap = cap
        self.cache = OrderedDict()
               
    def get(self, key):        
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
          
    def set(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)
