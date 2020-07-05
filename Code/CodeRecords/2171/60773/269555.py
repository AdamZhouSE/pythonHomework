class Node:
    def __init__(self,num,node):
        self.val=num
        self.next=node
def build(l):
    n=Node(l[0],None)
    p=n
    for i in range(1,len(l),1):
        n1=Node(l[i],None)
        n.next=n1
        n=n1
    return p
num=int(input())
for k in range(num):
    leng=int(input())
    l=input().split(" ")
    for i in range(len(l)):
        l[i]=int(l[i])
    no1=build(l)
    head=Node(0,None)
    p=head
    for i in range(len(l)):
        a=no1.val
        if a%2==0:
            head.next=no1
            head=head.next
        no1=no1.next
    no2=build(l)
    for i in range(len(l)):
        b=no2.val
        if b%2!=0:
            head.next=no2
            head=head.next
        no2=no2.next
    #print(head.val)
    #print(p.val)
    for i in range(len(l)):
        print(p.next.val,end=" ")
        p=p.next
    print("")


