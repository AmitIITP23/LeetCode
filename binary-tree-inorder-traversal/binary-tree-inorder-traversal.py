# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dummy(self,root: TreeNode,res):
        if(root!=None):
            if(root.left!=None):
                self.dummy(root.left,res)
            res.append(root.val)
            if(root.right!=None):
                self.dummy(root.right,res)
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res=[]
        self.dummy(root,res)
        return res
    
        