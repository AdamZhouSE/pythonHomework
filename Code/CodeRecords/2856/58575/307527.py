n=int(input())
tree=[]
tree.append([-9999999,0])
for i in range(n):
    temp=list(map(int,input().split(" ")))
    tree.append(temp)
tree.append([9999999,0])
num=0
i=1
while i<=n:
    if tree[i][0]-tree[i][1]>tree[i-1][0]:
        num+=1
    elif tree[i][0]+tree[i][1]<tree[i+1][0]:
        tree[i][0]+=tree[i][1]
        num+=1
    i+=1

print(num)