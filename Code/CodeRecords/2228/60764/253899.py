target=abs(int(input()))
s,i=0,0
while s<target:
    i+=1
    s+=i
if (s-target)%2==0:
    print(i)
elif (s-target+i+1)%2==0:
    print(i+1)
else:
    print(i+2)