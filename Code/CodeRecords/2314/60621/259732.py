class tree:
    value=0
    left=None
    right=None
    pre=None
    next=None
    def __init__(self,v):
        self.value=v
def middle(node:tree):
    stack=[]
    pre=None
    now=node
    while True:

        while now!=None:
            stack.append(now)
            now=now.left
        if len(stack)!=0:
            now=stack.pop()
            now.pre=pre
            if pre!=None:
                pre.next=now
            pre=now
            now=now.right
        else:
            break
a=eval(input())
tr=[tree(i+1) for i in range(a)]
head=0
for i in range(a):
    temp=[int(x)-1 for x in input().split()]
    if i==0:
        head=tr[temp[0]]
    if temp[1]!=-1:
        tr[temp[0]].left=tr[temp[1]]
    if temp[2]!=-1:
        tr[temp[0]].right=tr[temp[2]]
middle(head)
while head.pre!=None:
    head=head.pre
while head!=None:
    print(head.value,end=" ")
    head=head.next


