class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DLinkedList:
    def __init__(self):
        self.head = None

    def createNode(self, value):
        self.head = Node(value)

    def printList(self):
        head = self.head
        while head is not None:
            if head is self.head:
                print "Head"
            print head.data
            head = head.next
    
    def addNode(self, value):
        head = self.head
        if head  is None:
            self.createNode(value)
        else:
            while head.next is not None:
                head = head.next
            temp = Node(value)
            temp.prev = head
            head.next = temp

    def prepend(self, value):
        head = self.head
        if head is None:
            self.createNode(value)
        else:
            temp = Node(value)
            self.head = temp
            temp.next = head
            head.prev = temp

    def removeNode(self):
        head = self.head
        while head.next is not None:
            prev = head
            head = head.next
        head = None
        prev.next = head

    def removeByKey(self, key):
        head = self.head
        if head.data == key:
            temp = head.next
            self.head = temp
            head = None
            temp.prev = None
        else:
            while head is not None:
                head = head.next
                if head.next.data == key:
                    temp = head
                    ahead = temp.next.next
                    temp.next = ahead
                    ahead.prev = temp
                    head = None
                    break
    
    def insertByKey(self, key, value):
        head = self.head
        newNode = Node(value)
        if head.data is key:
            ahead = head.next
            head.next = newNode
            ahead.prev = newNode
            newNode.prev = head
            newNode.next = ahead
        else:
            while head.data != key and head is not None:
                temp = head
                head = head.next
                print temp.data, head.data
                if head.data == key:
                    break
            if head.next is None:
                self.addNode(value)
            else:
                temp = head.next
                print temp.data, head.data
                newNode.next = temp
                temp.prev = newNode
                newNode.prev = head
                head.next = newNode 

    def listLength(self): #lists length of list
        count = 0
        head = self.head
        while head is not None:
            head = head.next
            count+=1
        return count

    def sortListNodes(self):#Sorts using node and pointer swaps
        head = self.head
        val = 0
        count = self.listLength()
        if head is None:
            print "There are no elements in this list."
        while val <= count:
            while head is not None:
                if head is self.head and head is not None and head.next is not None and head.next.data < head.data:
                    temp = head
                    ahead = temp.next
                    temp.next = ahead.next
                    temp.prev = ahead
                    ahead.next = temp
                    ahead.prev = None
                    self.head = ahead
                elif head is not self.head and head is not None and head.next is not None and head.next.data < head.data:
                    ahead = head.next
                    temp.next = ahead
                    ahead.prev = temp
                    head.next = ahead.next
                    head.prev = ahead
                    ahead.next = head
                    
                temp = head
                head = head.next
            head = self.head
            val+=1

    def sortListData(self):#sorts with data allocations
        head = self.head
        val = 0
        count = self.listLength()
        if head is None:
            print "There are no elements in this list."
        while val <= count:
            while head is not None:
                if head is not None and head.next is not None and head.next.data < head.data:
                    ahead = head.next
                    temp1 = head.data
                    temp2 = ahead.data
                    head.data = temp2
                    ahead.data = temp1
                head = head.next

            head = self.head
            val+=1
            self.printList()