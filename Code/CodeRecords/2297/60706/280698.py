n=int(input())
list1=input().split(' ')
Tree=[]
Tree.append(0)
for i in range(len(list1)):
    Tree.append(int(list1[i]))
d=int(input())
start=1
ans=''
while d>1:
    start=start*2
    d=d-1
if start*2-1<=n:
    ans=ans+str(Tree[start])+' '
    for i in range(start+1,start*2):
        ans=ans+str(Tree[i])+' '
    ans=ans[:-1]
elif start<=n and start*2-1>n:
    ans=ans+str(Tree[start])+' '
    for i in range(start+1,n+1):
        ans=ans+str(Tree[i])+' '
    ans=ans[:-1]
else:
    ans='EMPTY'

print(ans)
