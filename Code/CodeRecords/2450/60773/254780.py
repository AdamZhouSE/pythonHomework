s=input()
#print(s)
l=s.split(",")
n=input()
#print(n)
head=0
sum=0
for i in range(len(l)):
    if l[i]==n and i==0:
        head=i
        sum=sum+1
    elif l[i]==n and l[i-1]!=n:
        head=i
        sum=sum+1
    elif l[i]==n:
        sum=sum+1
    else:
        continue
if sum==0: print([-1, -1])
else:
    print("["+str(head)+", "+str(head+sum-1)+"]")
