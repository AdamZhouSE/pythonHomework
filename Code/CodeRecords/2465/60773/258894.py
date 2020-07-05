s=input()
l=s.split(",")
for i in range(len(l)):
    l[i]=int(l[i])
result=0
for i in range(len(l)):
    sum=0
    for j in range(len(l)):
        if l[j]>=i:
            sum=sum+1
    if sum<=i:
        if sum>result:
            result=sum
if result==0:
    print(1)
else:
    print(result)
#print(s)