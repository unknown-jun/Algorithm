# make a hash function with chaine method

from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
    """The node is made up of hash"""

    def __init__(self, key: Any, value: Any, next: Node) -> None:
        """initialize"""
        self.key = key     # key
        self.value = value # value
        self.next = next   # refer to backward node


class ChaineHash:

    def __init__(self, capacity: int) -> None:
        """initialize"""
        self.capacity = capacity               # Designate the size of hash table
        self.table = [None] * self.capacity    # Declare the hash table (list)

    def hash_value(self, key: Any) -> int:
        """find out hash value"""
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)



    def search(self, key: Any) -> Any:
        """Retrun the key which is 'key' with searching element"""
        hash = self.hash_value(key)     # hash value of key to search
        p = self.table[hash]            # Attention the node

        while p is not None:
            if p.key == key:
                return p.value          # Search sucess
            p = p.next                  # Attention the backward node

        return None                     # Search fail

    def add(self, key: Any, value: Any) -> bool:
        """Add the value's element is 'value' and the key is 'key'"""
        hash = self.hash_value(key)     # The hash value of key being added
        p = self.table[hash]            # Attention the node

        while p is not None:
            if p.key == key:
                return False            # Fail to add
            p = p.next                  # Attention the backward node

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp         # Add the node
        return True                     # Search sucess


    def remove(self, key: Any) -> bool:
        """Remove the element which is 'key'"""
        hash = self.hash_value(key)     # Hash value of key to delete
        p = self.table[hash]            # Attention Node
        pp = None                       # Attention the before node

        while p is not None:
            if p.key == key:            # Run below if key is found
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next    # Sucess to delete key
                return True
            pp = p
            p = p.next                  # Attention the before node
        return False                    # Fail to delete (Key is not existed)

    def dump(self) -> None:
        """Dump the hash table"""
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f'   -> {p.key} ({p.value})', end='')
                p = p.next
            print()