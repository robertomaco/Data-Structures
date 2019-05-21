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
            while True:
                if data < root.data:
                    if root.left:    
                        root = root.left
                    else:
                        root.left = newNode

                elif data > root.data:
                    if root.right:
                        root = root.right
                    else:
                        root.right = newNode
                
                else:
                    break

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            if node is self.root:
                print "ROOT: ", node.data
            else:
                print node.data
            self.inorder(node.right)

    def preorder(self, node):
        if node is not None:
            print node.data
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print node.data