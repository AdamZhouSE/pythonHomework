class Node():
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkList():
    def __init__(self, node = None):
        self.head = node

    def isEmpty(self):
        return self.head == None

    def append(self, newItem):
        newNode = Node(newItem)
        if self.isEmpty():
            self.head = newNode
            newNode.next = self.head
        else:
            nowNode = self.head
            while nowNode.next != self.head:
                nowNode = nowNode.next

            nowNode.next = newNode
            newNode.next = self.head

    def add(self, newItem):
        newNode = Node(newItem)
        if self.isEmpty():
            self.head = newNode
        else:
            nowNode = self.head
            while nowNode.next != None:
                nowNode = nowNode.next
            nowNode.next = newNode

questNum = int(input())

for quest in range(questNum):
    n = int(input())
    s = input().split(' ')
    for i in range(n):
        s[i] = int(s[i])

    p = LinkList()

    for i in range(n):
        p.add(s[i])

    p1 = p.head
    odd = LinkList()
    ou = LinkList()

    while p1 != None:
        if p1.item % 2 == 0:
            ou.add(p1.item)
        else:
            odd.add(p1.item)
        p1 = p1.next

    ou1 = ou.head
    odd1 = odd.head

    while ou1 != None:
        print(ou1.item, end=' ')
        ou1 = ou1.next

    while odd1 != None:
        print(odd1.item, end = ' ')
        odd1 = odd1.next

    print()