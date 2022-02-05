class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
        printval = self.head
        while printval:
            print(printval.dataval)
            printval = printval.nextval

e1 = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list1 = SLinkedList()
list1.head = e1

# Link first Node to second node
list1.head.nextval = e2

# Link second Node to third node
e2.nextval = e3

list1.listprint()