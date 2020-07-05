input()
biscuit=[int(x) for x in input().split()]
count=0
if sum(biscuit)%2==1:
    for i in biscuit:
        if i%2==1:
            count+=1
else:
    for i in biscuit:
        if i%2==0:
            count+=1
print(count)