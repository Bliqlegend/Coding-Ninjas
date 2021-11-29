def printTree(root):
    if root == None:
        return
    print(root.data,end = ":")
    printTree(root.left)
    printTree(root.right)
 


def printTreeLR(root):
    if root == None:
        return
    print(root.data,end = ":")
    if root.left != None:
        print("L "+ root.left.data, end=',')
    if root.right!=None:
        print("R "+ root.right.data, end='')
    print()
    printTreeLR(root.left)
    printTreeLR(root.right)
 