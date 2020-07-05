class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


list=input().split()
val=int(list[1])
n=int(list[0])
tree={}
for i in range(n):
    list1=input().split()
    a=int(list1[0])
    b=int(list1[1])
    c=int(list1[2])
    temp=[]
    temp.append(b)
    temp.append(c)
    tree[a]=temp

list2=[]
list3=[val]
list2.append(list3)
for l in range(n):
    list4=list2[-1]
    temp11=[]
    for i in range(len(list4)):
        temp1=list4[i]
        temp2=tree[temp1]
        for k in temp2:
            if k!=0:
                temp11.append(k)
    list2.append(temp11)

for i in range(len(list2)):
    if(len(list2[i])!=0):
        str='Level'
        print(str,end=' ')
        print(i+1,end=' : ')
        for j in range(len(list2[i])-1):
            print(list2[i][j],end=' ')
        print(list2[i][-1])

for i in range(len(list2)):
    if(len(list2[i])!=0):
        if i%2==0:
            str='Level'
            print(str,end=' ')
            print(i+1,end=' from left to right: ')
            for j in range(len(list2[i])-1):
                print(list2[i][j],end=' ')
            print(list2[i][-1])
        else:
            str = 'Level'
            print(str, end=' ')
            print(i + 1, end=' from right to left: ')
            for j in range(len(list2[i]) - 1):
                print(list2[i][len(list2[i])-j-1], end=' ')
            print(list2[i][0])