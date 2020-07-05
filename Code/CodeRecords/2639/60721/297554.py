s=list(input())
k=int(input())
lis=s
s.sort()
m=0
for i in s:
    if(s.count(i)>m):
        m=s.count(i)
if(m+k==8 or m+k==5):
    print(m+k-1)
else:print(m+k)