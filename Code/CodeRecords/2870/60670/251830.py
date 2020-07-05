even=[]
n=int(input())
nums=list(map(int,input().split(' ')))
total=0
for num in nums:
    if num%2==0:
        total+=num
    else:
        even.append(odd)
even=sorted(even,reverse=True)
m=len(even)
if m%2==1:
    m=m-1
for i in range(0,m):
    total+=even[i]
print(total)