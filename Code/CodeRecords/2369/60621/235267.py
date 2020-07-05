class tree:
    value='a'
    leftree=None
    righttree=None

n=int(input())
Tree=[]
for i in range(n):
    temp=input()
    if(temp[0] not in Tree):
        Tree.append(temp[0])

    position=Tree.index(temp[0])
    if(temp[1]!="*"):
        Tree.insert(position+1,temp[1])
        if(temp[2]!="*"):
            Tree.insert(position+2,temp[2])
    else:
        if (temp[2] != "*"):
            Tree.insert(position + 1, temp[2])
ans=""
for i in Tree:
    ans=ans+i
print(ans,end="")