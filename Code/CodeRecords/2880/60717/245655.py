list1=input().split()
n=int(list1[0])
k=int(list1[1])
list2=input().split()
for i in range(0,n):
    list2[i]=int(list2[i])
left=0
right=n-1
count=0
while list2[left]<=k and left<n-1:
    left+=1
    count+=1
while list2[right]<=k and right>=0:
    right-=1
    count+=1
if(count>=n):
    print(n)
else:
    print(count)