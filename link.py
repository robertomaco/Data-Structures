class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.listHead = None

    def createHead(self, value):
        self.listHead = Node(value)

    def listPrint(self):
        printval = self.listHead
        while printval is not None:
            if printval is self.listHead:
                print "Head"
            print printval.data
            printval = printval.next

    def addVal(self, value):
        head = self.listHead
        temp = head
        if head is None:
            self.createHead(value)
        else:
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(value)
    
    def prepend(self, value):
        head = self.listHead
        if head is None:
            self.createHead(value)
        else:
            prependval = Node(value)
            prependval.next = self.listHead
            self.listHead = prependval

    def removeNode(self):
        head = self.listHead
        if head is None:
            print "There's no Nodes in the list"
        else:
            while head.next is not None:
                prev = head
                head = head.next
            prev.next = None

    def removeByKey(self, key):
        head = self.listHead
        if head.data == key:
            temp = head.next
            self.listHead = temp
            head = None
        else:
            while head.data != key and head.next is not None:
                behind = head
                head = head.next
                if head.next is not None:
                    ahead = head.next
            behind.next = ahead

    def listLength(self):
        count = 0
        head = self.listHead
        while head is not None:
            head = head.next
            count+=1
        return count

    def sortList(self):
        head = self.listHead
        if head.next is not None and head.next < head:
            headtemp = head.next
            self.listHead = headtemp
            head.next = headtemp.next
            headtemp.next = head
        while head is not None:
            print "temp"
            temp = head.next
            if temp is not None and temp < head:
                head.next = temp.next
                temp.next = head
            head = head.next

llist = SLinkedList()
llist.addVal(5)
llist.addVal(4)
llist.addVal(3)
llist.addVal(2)
llist.listPrint()
print ""
print "List Length:",llist.listLength()
llist.sortList()
llist.listPrint()
