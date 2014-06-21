#!/usr/bin/python


class HashTable(object):
    def __init__(self):
        self.size = 11  # use a prime number for efficiency
        self.keys = [None] * self.size
        self.vals = [None] * self.size
    
    def hash_function(self, item):
        return (hash(item) & 0x7fffffff) % self.size
    
    def rehash(self, position):
        return (position + 3) % self.size
    
    def put(self, key, val):
        """
        Insert a key-value pair into the hash map
        
        Args:
            key: The key used for indexing into the hash
            val: Value associated with the key
        """
        hash_val = self.hash_function(key)
        if self.keys[hash_val] is None:
            # slot is empty, insert here
            self.keys[hash_val] = key
            self.vals[hash_val] = val
        else:
            # slot is not empty, use 3-step probing
            next_slot = self.rehash(hash_val)
            while self.keys[next_slot] is not None and self.keys[next_slot] != key:
                # keep computing rehash value (keep probing)
                next_slot = self.rehash(next_slot)
            # we now have a position!
            self.keys[next_slot] = key
            self.vals[next_slot] = val
    
    def get(self, key):
        """
        Find the value associated with a key in the hashtable
        
        Args:
            key: Key to find in hashtable
        """
        hash_val = self.hash_function(key)
        initial = self.keys[hash_val]  # keep track of initial, to stop iteration
        if self.keys[hash_val] == key:
            return self.vals[hash_val]
        else:
            next_slot = self.rehash(hash_val)
            while self.keys[next_slot] != key and self.keys[next_slot] != initial:
                next_slot = self.rehash(next_slot)
            # check if we have reached initial
            if self.keys[next_slot] == key:
                return self.vals[next_slot]
            else:
                return None
    
    # override to be able to index into hash
    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self, key, val):
        self.put(key, val)