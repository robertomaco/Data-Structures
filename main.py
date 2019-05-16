import link

llist = link.SLinkedList()

choice = 0
while choice != 5:
    choice = input("1: Create list\n2: Add to list\n3: Prepend list\n4: Print List\n5: Exit\n\nSelect One: ")
    print ("")
    if choice == 1:
        val = input("Enter the starting value of the list: ")
        llist.createHead(val)
    if choice == 2:
        val = input("Enter the value you would like to add to the list: ")
        llist.addVal(val)
    if choice == 3:
        val = input("Enter the value you would like to prepend to the list: ")
        llist.prepend(val)
    if choice == 4:
        llist.listPrint()
        print("")
    if choice == 5:
        break

