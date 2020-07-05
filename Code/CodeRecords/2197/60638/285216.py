class Node(object):
    def __init__(self, val):
        self.val=val
        self.next=None
n=int(input())
for x in range(0,n):
    num=int(input())
    itr=Node(1)
    first=itr
    for i in range(2,num+1):
        itr.next=Node(i)
        itr=itr.next
    itr.next=first
    itr=first
    while itr.next!=itr:
        itr.next=itr.next.next
        itr=itr.next

    print(itr.val)