numlist=input().split(' ')
s=int(numlist[0])
n=int(numlist[1])
tree=[1 for x in range(s+1)]
for i in range(n):
    numlist=input().split(' ')
    l=int(numlist[0])
    r=int(numlist[1])
    for j in range(l,r+1):
        tree[j-1]=0
  
print(tree.count(1))