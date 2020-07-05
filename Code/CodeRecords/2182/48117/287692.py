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

    def add(self, newNode):
        if self.isEmpty():
            self.head = newNode
        else:
            nowNode = self.head
            while nowNode.next != None:
                nowNode = nowNode.next
            nowNode.next = newNode

questNum = int(input())

for quest in range(questNum):
    nk = input().split(' ')
    n = int(nk[0])
    k = int(nk[1])
    p1 = LinkList()
    p2 = LinkList()

    for i in range(1, n + 1):
        p1.append(i)

    count = 1
    h1 = p1.head
    h2 = p2.head
    last = Node(0)
    last.next = p1.head
    while p1.head.next != p1.head:
        if count == k:
            count = 1
            last.next = h1.next
            temp = h1
            h1 = h1.next
            temp.next = None
            p2.add(temp)

        else:
            count += 1
            if last.next == None:
                break
            else:
                last = last.next
            h1 = h1.next

    print(h1.item)