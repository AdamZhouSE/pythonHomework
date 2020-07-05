nc=input().split(' ')
n=int(nc[0]);c=int(nc[1])
s=input().split(' ');s=[int(x) for x in s]
count=1
for i in range(1,n):
    if s[i]-s[i-1]<=c:
        count+=1
    elif c!=0:
        count=1
    else:
        count=0
print(count)
