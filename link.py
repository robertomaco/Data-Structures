class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
        self.tailval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            if printval is self.headval:
                print "Head"
            print printval.dataval
            printval = printval.nextval

    def createHead(self, value):
        self.headval = Node(value)

    def addVal(self, value):
        head = self.headval
        temp = head
        if head is None:
            self.createHead(value)
        else:
            while temp.nextval is not None:
                temp = temp.nextval
            temp.nextval = Node(value)
    
    def prepend(self, value):
        head = self.headval
        temp = head
        if head is None:
            self.createHead(value)
        else:
            prependval = Node(value)
            prependval.nextval = self.headval
            self.headval = prependval
