class node:
    def __init__(self,id):
        self.id=id
        self.next=self
def findSurvior(ptr):
    while ptr.next!=ptr:
        ptr.next=ptr.next.next
        ptr=ptr.next
    return ptr
t=int(input())
while t:
    n=int(input())
    first=node(1)
    tmp=first
    for id in range(2,n+1):
        newNode=node(id)
        tmp.next=newNode
        newNode.next=first
        tmp=tmp.next
    print(findSurvior(first).id)
    t-=1