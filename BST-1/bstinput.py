from createbst import BinaryTreeNode

def takeInput():
    print("Enter root data")
    rootData = int(input())
    if (rootData == -1) :
        return None
    root = BinaryTreeNode(rootData)
    root.left = takeInput()
    root.right = takeInput()
    return root

