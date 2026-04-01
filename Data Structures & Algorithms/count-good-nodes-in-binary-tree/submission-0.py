# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution:
# DFS - preorder
# prev_node mark the previous value
# keep an local max for each branch and update hte max
# keep self.res to keep the number of times that node > max
# self.res = 0
# max_val = root.val
# # dfs(root, root.val)
# dfs(node, max_val):

#     if not node: return

#     # preocess current node and collect results
#     if node.val > max_val:
#         self.res += 1
#         max_val = node.val

#     dfs(node.left, max_val)
#     dfs(node.right, max_val)



class Solution:
    def __init__(self):
        self.res = 0
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return None
        if root and not root.left and not root.right: return 1
        self.res = 0
        def dfs(node, max_val):
            if not node: return
            if node.val >= max_val:
                self.res += 1
                max_val = node.val
            dfs(node.left, max_val)
            dfs(node.right, max_val)
        dfs(root, root.val)
        return self.res






        