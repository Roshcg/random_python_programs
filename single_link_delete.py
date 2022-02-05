class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def list_print(self):
        head = self.head
        while head:
            print(head.data)
            head = head.next

    def delete_if_dup(self):
        head1 = self.head
        head = self.head
        while head:
            key = head.data
            next_head = head.next
            while next_head:
                if key == next_head.data:
                    head.next = next_head.next
                head = next_head
                next_head = next_head.next
            head = head1.next
            head1 = head1.next


e1 = Node('mon')
e2 = Node('tue')
e3 = Node('wed')
e4 = Node('mon')
e5 = Node('wed')
e6 = Node('thu')
e7 = Node('mon')

l1 = LinkedList(e1)
l1.head.next = e2
e2.next = e3
e3.next = e4
e4.next = e5
e5.next = e6
e6.next = e7

l1.list_print()
print('*'*5)
l1.delete_if_dup()
print('*'*5)
l1.list_print()
