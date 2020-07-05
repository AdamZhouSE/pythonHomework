n=int(input())
a=list(map(int,input().split(' ')))
a.sort()
count=0
while len(a)>1:
    if count%2==0:
        a.pop()
    else:
        a.pop(0)
    count+=1
print(a[0])