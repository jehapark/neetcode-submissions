"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash = {None : None}

        curr = head
        while curr:
            copy = Node(curr.val)
            hash[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            new = hash[curr]
            new.next = hash[curr.next]
            new.random = hash[curr.random]
            curr = curr.next
        
        return hash[head]
