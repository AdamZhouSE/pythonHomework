n=int(input())
l=list(map(int,input().split()))
l.sort()
Sum=0
tmp=0
for i in l:
    if i<=tmp:
        Sum+=tmp-i+1
        i=tmp+1
    tmp=i
print(Sum)