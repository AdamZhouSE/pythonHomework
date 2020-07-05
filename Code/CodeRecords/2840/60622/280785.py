def sum(s):
    c=0
    for i in range(len(s)):
        if s[i]=='4' or s[i]=='7':
            c+=1
    return c
l=list(map(int,input().split()))
n=l[0]
k=l[1]
arr=input().split()
count=0;
for number in arr:
    n=sum(number)
    if n<=k:
        count+=1
print(count)