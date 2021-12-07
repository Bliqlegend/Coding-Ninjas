def numofNodes(root):
    if root == None:
        return 0
    leftCount = numofNodes(root.left)
    rightCount = numofNodes(root.right)
    return 1 + leftCount + rightCount

