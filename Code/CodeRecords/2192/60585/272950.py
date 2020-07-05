class Node(int):
    def __init__(self,num):
        self.num = num
        self.next = None
class SingleLinkedList(int):
    def __init__(self):
        self.__head = None
    def is_empty(self):
        return self.__head==None
    def travel(self):
        cur = self.__head
        while cur != None:
            print(cur.num, end=" ")
            cur = cur.next
        print()
    def append(self, num):
        node = Node(num)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node


    
t=eval(input())
arr=[]
for _ in range(t):
    n=eval(input())
    arrList=SingleLinkedList()
    arrList.append(n)
    temp=n
    
    while temp>0:
        temp-=5
        arrList.append(temp)
    while temp<n:
        temp+=5
        arrList.append(temp)
    arrList.travel()
    