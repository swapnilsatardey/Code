# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def postorderTraversal(self, A):
        l = []
        st = []
        st.append(A)
        while st:
            u = st[-1]
            if u.left == None and u.right == None: 
                l.append(u.val)
                st = st[:-1]
            if u.right:
                st.append(u.right)
                u.right = None
            if u.left:
                st.append(u.left)
                u.left = None
            
        
        return l    
                
                

