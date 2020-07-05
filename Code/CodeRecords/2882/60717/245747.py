n=int(input())

list1=input().split()

for i in range(0,n):
    list1[i]=int(list1[i])
    
tmp=max(list1)
left=0
right=n-1

while left<n-1and list1[left]<list1[left+1]:
    left+=1

while right>0and list1[right]>list1[right-1]:
    right-=1
    
flag=1

for i in range(left,right+1):
    if list1[i]!=tmp:
        flag=0

if flag==0:
    print('NO')
else:
    print('YES')
    