import math
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
        while cur.next != None:
            print(cur.num, end=" ")
            cur = cur.next
        print(cur.num,end="")
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
def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:return False
    return True
t=eval(input())
for _ in range(t):
    Range=list(map(int,input().strip().split(' ')))
    m=Range[0]
    if m==1:
        m=2 
    n=Range[1]
    primeList=SingleLinkedList()
    for i in range(m,n+1):
        if isPrime(i):
            primeList.append(i)
    primeList.travel()
    