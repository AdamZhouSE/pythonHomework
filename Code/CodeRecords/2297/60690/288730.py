n=int(input())
tree=input().split(" ")
for i in range(len(tree)):tree[i]=int(tree[i])
d=int(input())-1
if 2**d-1>=n: print("EMPTY")
else:
    res=[]
    index=2**d-1
    while index<2**(d+1)-1 and index<len(tree):
        res.append(tree[index])
        index+=1
    for i in range(len(res)-1):
        print(res[i],end=" ")
    print(res[-1])