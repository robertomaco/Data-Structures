import link, stack
st = stack.Stack()
llist = link.SLinkedList()

choice = 0
while choice != 3:
    choice = input("1: Linked List\n2: Stack\n3: Exit\nChoose a data structure to interact with: ")
    if choice == 1:
        while choice != 7:
            choice = input("1: Create list\n2: Add to list\n3: Prepend list\n4: Print List\n5: Pop\n6: Delete with key\n7: Exit\n\nSelect One: ")
            print ("")
            if choice == 1:
                val = input("Enter the starting value of the list: ")
                print ""
                llist.createHead(val)
            if choice == 2:
                val = input("Enter the value you would like to add to the list: ")
                print ""
                llist.addVal(val)
            if choice == 3:
                val = input("Enter the value you would like to prepend to the list: ")
                print ""
                llist.prepend(val)
            if choice == 4:
                llist.listPrint()
                print("")
            if choice == 5:
                llist.removeNode()
            if choice == 6:
                val = input("Enter a key to remove the matching Node: ")
                print ""
                llist.removeByKey(val)
            if choice == 7:
                break
    if choice == 2:
        while choice != 4:
            choice = input("1: Push\n2: Pop\n3: Print\n4: Exit\n\n")
            if choice == 1:
                val = input("Enter the value you'd like to push to the stack: ")
                print ""
                st.push(val)
            if choice == 2:
                st.pop()
                print "Top value removed"
            if choice == 3:
                print ""
                st.printStack()
                print ""
            if choice == 4:
                break

