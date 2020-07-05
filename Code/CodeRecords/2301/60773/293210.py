class Node:
    def __init__(self,str,next):
        self.val=str
        self.next=next
def add(node,str):
    node1=Node(str,None)
    while(node.next!=None):
        node=node.next
    node.next=node1
def delect(node,str):
    while(node!=None):
        if node.next !=None and node.next.val==str:
            node1=node.next.next
            node.next=node1
            break
        else:
            node=node.next
def isIn(node,str):
    while(node!=None):
        if node.val==str:
            return True
        else:
            node=node.next
    return False
def count(node,str):
    sum=0
    while node!=None:
        if node.val[0:len(str)]==str:
            sum=sum+1
        node=node.next
    return sum

num=int(input())
node=Node("0000",None)
for i in range(num):
    #print(i)
    s=input().split(" ")
    n=int(s[0])
    str=s[1]
    if n==1:
        add(node,str)
    elif n==2:
        delect(node,str)
    elif n==3:
        if isIn(node,str):
            print("YES")
        else:
            print("NO")
    else:
        print(count(node,str))

