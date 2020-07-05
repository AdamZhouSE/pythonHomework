odd=[]
n=int(input())
nums=list(map(int,input().split(' ')))
total=0
for num in nums:
    if num%2==0:
        total+=num
    else:
        odd.append(num)
odd=sorted(odd,reverse=True)
m=len(odd)
if m%2==1:
    m=m-1
for i in range(0,m):
    total+=odd[i]
print(total)