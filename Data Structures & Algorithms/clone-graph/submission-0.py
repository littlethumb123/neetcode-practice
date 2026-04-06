"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# Use a hashmap to save node

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return node
        hashmap = {}
        def dfs(node):
            hashmap[node] = Node(val = node.val)
            for i in node.neighbors:
                if i not in hashmap: dfs(i)
                hashmap[node].neighbors.append(hashmap[i])
        dfs(node)
        return hashmap[node]
        