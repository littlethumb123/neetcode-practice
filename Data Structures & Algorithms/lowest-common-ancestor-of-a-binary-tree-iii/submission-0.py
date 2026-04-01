"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""
# Strategy:
# collect the parent of p in a set()
# then from q find if the p or there is any parent in the set()

class Solution:
    def lowestCommonAncestor(self, p, q):
        
        p_parents = set()
        while p:
            p_parents.add(p)
            p = p.parent
        while q:
            if q not in p_parents:
                q = q.parent
            else:
                return q
        

        