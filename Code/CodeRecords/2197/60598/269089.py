class LinkedList:
    num = 0
    nextNum = None

    def __init__(self, val):
        self.num = val


times = int(input())
for i in range(times):
    N = int(input())
    head = LinkedList(1)
    temp = head
    head.nextNum = temp
    for j in range(2,N+1):
        temp.nextNum = LinkedList(j)
        temp = temp.nextNum
    temp.nextNum = head
    while head.nextNum!=head:
        head.nextNum = head.nextNum.nextNum
        head = head.nextNum
    print(head.num)
