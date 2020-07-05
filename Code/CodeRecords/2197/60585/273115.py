class Node(int):
    def __init__(self,num):
        self.num = num
        self.next = None
class CircularLinkedList(int):
    def firstNode(self):
        return self.__head
    def __init__(self):
        self.__head = None
    def is_empty(self):
        return self.__head==None
    def append(self, num):
        node = Node(num)
        if self.is_empty():
            self.__head = node
            node.next=self.__head
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next=self.__head
t=eval(input())
for _ in range(t):
    n=eval(input())
    soldiers=CircularLinkedList()
    for i in range(n):
        soldiers.append(i+1)
    p=soldiers.firstNode()
    for i in range(1,n):
        p.next=p.next.next
        p=p.next
    print(p.num)