class node:

     def __init__(self,left,right,d):
        self.r=right
        self.l=left
        self.data=d
     def preorder(self,n):
         result.append(n.data)
         if n.l!=None:
            self.preorder(n.l)
         if n.r!=None:
            self.preorder(n.r)

result=[]
N=int(input())
ls=input().split(" ")
ls=[int(x) for x in ls]
root=node(None,None,ls[0])
for i in range(1,len(ls)):
    newnode=node(None,None,ls[i])
    anode=root
    while True:
        if newnode.data<anode.data:
            if anode.l==None:
                anode.l=newnode
                break
            else:
                anode=anode.l
        elif newnode.data>anode.data:
            if anode.r==None:
                anode.r=newnode
                break
            else:
                anode=anode.r
root.preorder(root)
for i in range(len(result)):
    if i<len(result)-1:
        print(result[i],end=" ")
    else:
        print(result[i])


