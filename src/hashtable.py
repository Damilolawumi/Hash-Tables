# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.
        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash
        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Fill this in.
        '''
        index = self._hash_mod(key) # create an index from the hash of the key
        
        if self.storage[index] is not None: #if storage index is not empty
            current = self.storage[index] #make the current node the strorage index
            while current.next is not None and current.key is not key: # while current node is not empty and current key is not key 
                current = current.next #go to the next
            if current.key == key: #if current key is equal to the key we assign the value to current value
                current.value = value 
                return
            else:
                current.next = LinkedPair(key, value) #creates a newnode in the key and value
                return
        else: #if the storage is empty
            self.storage[index] = LinkedPair(key, value) #creates a newnode in the key and value

    def remove(self, key):
        '''
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Fill this in.
        '''
        index = self._hash_mod(key) # create an index from the hash of the key

        if self.storage[index] is None: #if no key found
            print('Warning: key not found') 
            return 
        else:
            self.storage[index] = None 

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Fill this in.
        '''
        index = self._hash_mod(key)  # get the position in the array
        # print(f'HERE IS THE KEY: {key}')
       
        if self.storage[index] is None:
            return None
        else:
            current = self.storage[index] # get the node at the current position
          # Tranverse the linked list
            while current is not None:
                if current.key == key: # compare the key of the node in the linked list with the hashed key
                    #print(current.value)
                    return current.value # return the value of the current node
                    
                else: # move on to the next node
                    current = current.next 
            return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Fill this in.
        '''
        self.capacity *= 2  # double the existing capacity
        new_store = list(self.storage)  # copy the existing storage
        self.storage = [None] * self.capacity  # create new array

        for i in [item for item in new_store if item != None]:  # go through all the items in the copied list without the none value
            current_node = i  # set the current node to the current item
            
            while current_node is not None:  # if current node is not None
                self.insert(current_node.key, current_node.value) # Insert into the New storage
                current_node = current_node.next  # move to the next node


if __name__ == "__main__":
    ht = HashTable(2)
    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")
    print("")
    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))
    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)
    print(f"\nResized from {old_capacity} to {new_capacity}.\n")
    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))
    print("")
