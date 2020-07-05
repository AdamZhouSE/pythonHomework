class CircularNode:
    next = None
    data = None

    def __init__(self, data, next):
        self.data = data
        self.next = next

    def Next(self):
        return self.next

    def getData(self):
        return self.data

class LinkedList:

    head = CircularNode(None, None)

    def isEmpty(self):
        if self.head.next == None:
            return True
        else:
            return False

    def insert(self, data):
        node = CircularNode(data, None)
        if self.isEmpty():
            self.head.next = node
            node.next = None
        else:
            temp = self.head.next
            if temp.next == None:
                temp.next = node
                node.next = self.head.next
            else:
                itr = self.head.next
                while itr.next != self.head.next:
                    itr = itr.next
                node.next = self.head.next
                itr.next = node

    def getFirst(self):
        return self.head.next

    def setData(self, node, data):
        node.data = data

    def next(self,node):
        return node.Next()

    def find(self):
        node = self.head.next
        while node.data == 0:
            node = self.next(node)
        print(node.data)

    def getHead(self):
        return self.head

    #多次使用同一个循环链表，clear将除了头节点的next设为None，此时链表仅剩head
    def clear(self):
        self.head.next = None

test_num = int(input())
people = LinkedList()
for i in range(test_num):
    dead = 0
    line = input().split(" ")
    n = int(line[0])
    k = int(line[1])
    for j in range(n):
        people.insert(j+1)
    item = people .getHead()
    while dead < n-1:
        count = 0
        j = 0
        while j < k:
            item = item.Next()
            if item.getData() == 0:
                j -= 1
            j += 1
        people .setData(item, 0)
        dead += 1
    people .find()
    people.clear()

