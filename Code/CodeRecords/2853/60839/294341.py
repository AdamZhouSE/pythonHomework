n=int(input())
lis=list(map(int,input().split(" ")))

total=sum(lis)
even=0
odd=0
for i in lis:
    if i%2==0:
        even+=1
    else:
        odd+=1
if total%2==0:
    print(even)
else:
    print(odd)