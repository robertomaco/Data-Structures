class Node: #initialises node
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.listHead = None#sets head value

    def createHead(self, value):#creates head node
        self.listHead = Node(value)

    def listPrint(self):#prints all nodes in a list
        printval = self.listHead
        while printval is not None:
            if printval is self.listHead:
                print "Head"
            print printval.data
            printval = printval.next

    def addVal(self, value): #adds value to the list
        head = self.listHead
        temp = head
        if head is None:
            self.createHead(value) #creates new head if there is none
        else:
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(value) #adds new node to end of list
    
    def prepend(self, value): #adds a node and sets it as the head 
        head = self.listHead
        if head is None:
            self.createHead(value) #creates new head if there is none
        else:
            prependval = Node(value) #creates new node
            prependval.next = self.listHead #sets current head node to the next of the new node
            self.listHead = prependval #sets new node to head

    def removeNode(self): #removes node from list
        head = self.listHead
        if head is None:
            print "There's no Nodes in the list"
        else:
            while head.next is not None:
                prev = head
                head = head.next
            prev.next = None #removes the latest node from list

    def removeByKey(self, key): #Looks within list for a node with a given key and removes it
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
    
    def insertAfterKey(self, key, value): #Insert value in front of key
        head = self.listHead
        newNode = Node(value) #Creates new node
        if head.data == key:
            temp = head.next #sets temp = head->next
            head.next = newNode #sets head->next to new node
            newNode.next = temp #sets newnode->next to temp head->newnode->temp
        else:
            while head.data != key and head is not None:
                head = head.next
                if head.data == key:
                    break
            if head.next is None:
                newNode = head.next
            else:
                temp = head.next
                newNode.next = temp
                head.next = newNode 

    def listLength(self): #lists length of list
        count = 0
        head = self.listHead
        while head is not None:
            head = head.next
            count+=1
        return count

    def sortList(self): #Sorts the list
        head = self.listHead
        val = self.listLength() #Gets length of list
        count = 0
        while count <= val: #Loops the list to 
            while head is not None:
                if head is not None and head == self.listHead and head.next.data < head.data: #checks if the head needs to be swapped
                    headtemp = head.next
                    self.listHead = headtemp
                    head.next = headtemp.next
                    headtemp.next = head
                elif head is not None and head != self.listHead:
                    if head.next is not None and head.next.data < head.data: #checks if the node needs swapped
                        ahead = head.next
                        head.next = ahead.next
                        ahead.next = head
                        temp.next = ahead
                    #temp->ahead->head

                temp = head
                head = head.next
            head = self.listHead
            count+=1