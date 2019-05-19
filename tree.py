
class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

class binaryTree:
    def __init__(self):
        self.root = None

    def printBranch(self, branch):
        root = branch
        print "Root: ", root.data
        if root.left is not None:
            print "Left: ", root.left.data
        else:
            print "Left: NULL"
        if root.right is not None:
            print "Right: ", root.right.data
        else:
            print "Right: NULL"

    def printTree(self):
        root = self.root
        if self.isEmpty():
            print "Tree is empty"
        else:
            self.printBranch(root)

    def isEmpty(self):
        root = self.root
        empty = True
        if root is not None:
            empty = False
        return empty

    def createNode(self, data):
        node = Node(data)
        return node

    def createRoot(self, data):
        root = self.root
        if self.isEmpty():
            self.root = self.createNode(data)
        else:
            print "Root already exists"

    def addNode(self, data):
        root = self.root
        newNode = self.createNode(data)
        if self.isEmpty():
            print "Your tree is empty, but I'll create the root for you this time"
            self.createRoot(data)
        else:
            if root.right is None and data > root.data:
                root.right = newNode
                root.right.parent = root
            elif root.left is None and data < root.data:
                root.left = newNode
                root.left.parent = root
            elif root.right is not None and data > root:
                root = root.right
            elif root.left is None and data < root:
                root = root.left
            while root.left is not None and root.right is not None:
                if root.right is None and data > root:
                    root.right = newNode
                elif root.left is None and data < root:
                    root.left = newNode
                elif root.right is not None and data > root:
                    root = root.right
                elif root.left is None and data < root:
                    root = root.left
