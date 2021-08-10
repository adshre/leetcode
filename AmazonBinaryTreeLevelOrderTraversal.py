# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = [] #ans 
        
        def printLevelOrder(node, level):
            
            if node :
                if len(levels) == level:
                    levels.append([])   #create new level if ans level match level you create
                levels[level] += [node.val]
                
                printLevelOrder(node.left, level+1) #left tree and increment level by 1
                printLevelOrder(node.right, level+1)
                
        printLevelOrder(root, 0)
                
        return levels
                
