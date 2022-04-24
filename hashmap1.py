from node import Node


class Hashmap1:

    def __init__(self):
        self.map = [[] for _ in range(10)]
        self.size = 10

    def insert(self, key, runtime):
        """This method inserts a new function as a node to the hash table

        if the function already exists it will print out a statement
        """
        hash_key = hash(key) % self.size
        key_exists = False
        bucket = self.map[hash_key]
        for node in bucket:
            if node.name == repr(key):
                key_exists = True
                print("func already exists")
                break
        if not key_exists:
            new_func_node = Node(repr(key), runtime)  # making a new node for the new function
            bucket.append(new_func_node)  # adding the new node to the hashmap

    def search(self, key):
        """searching for the func node in the hash table

        if the func exists it will return the node with the func's stats.
        if the func doesnt exists it will return false
        """
        hash_key = hash(key) % self.size
        node_exists = False
        bucket = self.map[hash_key]
        for node in bucket:
            if node.name == repr(key):
                return node
        return False

    def delete(self, key):
        """deleting the node of a function from the hash table"""
        hash_key = hash(key) % self.size
        key_exists = False
        bucket = self.map[hash_key]
        for node in bucket:
            if repr(key) == node.name:
                key_exists = True
                bucket.remove(node)
                break
        if key_exists:
            print('Key {} deleted'.format(repr(key)))
        else:
            print('Key {} not found'.format(repr(key)))
