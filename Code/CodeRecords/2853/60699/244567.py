cnt=int(input())
list1=list(map(int,input().split(' ')))
odd=0
even=0
res=0
for i in list1:
    if i%2==0:
        even+=1
    else:
        odd+=1
    res+=i
if res%2==0:
    print(even)
else:
    print(odd)