class Node:
    
    def __init__(self, inputdata):
        self.data = inputdata
        self.next = None

    def display(self):
        print(self.data)

head = Node(5)
N2 = Node(4)
N3 = Node(1)
N4 = Node(10)
N5 = Node(15)

head.next = N2
N2.next = N3
N3.next = N4
N4.next = N5


def countNodes(head):
    count = 1
    current = head
    while current.next != None:
        count = count + 1
        current = current.next
    print (count)

countNodes(head)