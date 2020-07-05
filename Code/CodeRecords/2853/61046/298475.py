num=int(input())
test=input().split()
test=list(map(int,test))
odd=0
even=0
for x in test:
    if x%2==0:
        even+=1
    else:
        odd+=1
if odd==1:
    ans=1
elif odd>1 and odd%2==0:
    ans=num-odd
elif odd>1 and odd%2==1:
    ans=odd
else:
    ans=num
print(ans)