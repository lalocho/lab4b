# Luis Ochoa
# 80508534
# 11:30


class Node(object):
    password = ""
    next = None

    def __init__(self, password, next):
        self.password = password
        self.next = next

# HashTable class using chaining.


class ChainingHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    # All insert and search methods are the same with exceot the actual hash function used
    def __init__(self, initial_capacity):
        # initialize the hash table with empty bucket list entries.
        self.table = [None]*initial_capacity
        self.collision_counter = 0  # used to calculate average collision in table
        self.input_counter = 0      # used to calculate load factor of table

    # Inserts a new item into the hashtable.
    # checks if item already exists in table if it does, it doesnt do anything
    # inserts into beginning of linked list for chaining
    def insert_a(self, item):
        # get the bucket list where this item will go.
        bucket = hash(item) % len(self.table)
        # inserts Node into the beginning setting whatever was already inside as .next
        temp_node = self.table[bucket]
        if temp_node is not None:
            self.collision_counter += 1
        # assuming input file has no repeats
        self.input_counter += 1
        self.table[bucket] = Node(item, self.table[bucket])
        return

    def insert_b(self, item):
        # get the bucket list where this item will go.
        bucket = (hash(item)+1)**3 % len(self.table)
        # inserts Node into the beginning setting whatever was already inside as .next
        temp_node = self.table[bucket]
        # assuming input file has no repeats
        self.table[bucket] = Node(item, self.table[bucket])
        return

    def insert_c(self, item):
        # get the bucket list where this item will go.
        bucket = (hash(item)-1)**2 % len(self.table)
        # inserts Node into the beginning setting whatever was already inside as .next
        temp_node = self.table[bucket]
        # assuming input file has no repeats
        self.table[bucket] = Node(item, self.table[bucket])
        return
    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.

    def search_a(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        temp_node = self.table[bucket]
        while temp_node is not None:
            if temp_node.password == key:
                return True
            temp_node = temp_node.next
        return False

    def search_b(self, key):
        # get the bucket list where this key would be.
        bucket = (hash(key)+1)**3 % len(self.table)
        temp_node = self.table[bucket]
        while temp_node is not None:
            if temp_node.password == key:
                return True
            temp_node = temp_node.next
        return False

    def search_c(self, key):
        # get the bucket list where this key would be.
        bucket = (hash(key)-1)**2 % len(self.table)
        temp_node = self.table[bucket]
        while temp_node is not None:
            if temp_node.password == key:
                return True
            temp_node = temp_node.next
        return False







