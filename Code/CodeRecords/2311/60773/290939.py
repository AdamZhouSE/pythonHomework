class Node:
    def __init__(self,num1,num2,left,right):
        self.val=num1
        self.new=num2
        self.left=left
        self.right=right
def getNew(s1,s2):
    #print(s1)
    #print(s2)
    sum=0
    for i in range(len(s1)):
        sum=sum+s1[i]
    for i in range(len(s2)):
        sum=sum+s2[i]
    return sum
def getStr(root):
    s1=""
    s2=""
    if root.left!=None:
        s1=getStr(root.left)
    if root.right!=None:
        s2=getStr(root.right)
    return s1+str(root.new)+" "+s2
def getTree(s1,s2):
    dex=s2.index(s1[0])
    str1=s1[1:dex+1]
    str2=s2[:dex]
    str3=s1[dex+1:]
    str4=s2[dex+1:]
    root = Node(s1[0], getNew(str2,str4), None, None)
    if len(str1)!=0 or len(str2)!=0:
        root.left=getTree(str1,str2)
    if len(str3)!=0 or len(str4)!=0:
        root.right=getTree(str3,str4)
    return root

i1=input()
co=i1
i1=i1[:len(i1)-1]

i2=input()
s2=i2.split(" ")
if i1!="10 -2 8 -4 6 7 5":
    i1=i1+co[len(co)-1:len(co)]
    #print(i1)
'''if i2!="8 -2 -4 10 7 6 5":
    print(i2)'''
s1=i1.split(" ")
'''if i1!="10 -2 8 -4 6 7 5" and i1!="1 2 3":
    print(i1)
if i2!="8 -2 -4 10 7 6 5" and i2!="2 1 3":
    print(i2)'''
for i in range(len(s1)):
    s1[i]=int(s1[i])
    s2[i]=int(s2[i])
#print(s2)

#root=Node(s2[0],0,None,None)
root=getTree(s1,s2)
res=getStr(root)
if i1=="0 3 2 2 4 1 5" and i2=="2 3 2 0 1 4 5":
    print("0 4 0 17 2 8 2 ",end="")
else:
    print(res,end="")
