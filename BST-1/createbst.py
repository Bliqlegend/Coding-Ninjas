class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
bst1 = BinaryTreeNode(1)
bst2 = BinaryTreeNode(2)
bst3 = BinaryTreeNode(3)

bst1.left = bst2
bst1.right = bst3
