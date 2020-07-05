target=abs(int(input()))
i=0
while i*(i+1)//2<target:
    i+=1
if i*(i+1)//2==target or (i*(i+1)//2-target)%2==0:
    print(i)
elif i%2==0:
    print(i+1)
else:
    print(i+2)
