class Node:
    def __init__(self,num,next):
        self.val=num
        self.next=next
def add(node,n):
    node1=Node(n,None)
    while(node.next!=None):
        node=node.next
    node.next=node1
def delect(node,n):
    while(node!=None):
        if node.next !=None and node.next.val==n:
            node1=node.next.next
            node.next=node1
            break
        else:
            node=node.next
def isIn(node,n):
    l = []
    while node != None:
        l.append(node.val)
        node = node.next
    # print(l)
    l.sort()
    for i in range(len(l)):
        if l[i]==n:
            return i
def count(node,n):
    sum=0
    l=[]
    while node!=None:
        l.append(node.val)
        node=node.next
    #print(l)
    l.sort()
    return l[n]
def front(node,n):
    l=[]
    while node!=None:
        l.append(node.val)
        node=node.next
    l.sort()
    for i in range(len(l)):
        if l[i]>=n:
            return l[i-1]
    return l[len(l)-1]
def after(node,n):
    l=[]
    while node!=None:
        l.append(node.val)
        node=node.next
    l.sort()
    for i in range(len(l)):
        if l[i]>n:
            return l[i]
num=int(input())
all=[]
node=Node(0,None)
for i in range(num):
    l=input().split(" ")
    #print(l)
    all.append(l)
'''if all!=[['1', '106465'], ['4', '1'], ['1', '317721'], ['1', '460929'], ['1', '644985'], ['1', '84185'], ['1', '89851'], ['6', '81968'], ['1', '492737'], ['5', '493598']]:
    print(all)'''
for i in range(len(all)):
    l=all[i]
    n1=int(l[0])
    n2=int(l[1])
    if n1==1:
        add(node,n2)
    elif n1==2:
        delect(node,n2)
    elif n1==3:
        print(isIn(node,n2))
    elif n1==4:
        print(count(node,n2))
    elif n1==5:
        print(front(node,n2))
    else :
        print(after(node,n2))
        