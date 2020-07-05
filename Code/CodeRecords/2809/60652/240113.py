n=int(input())
l=list(map(int,input().split()))
l.sort()
wide,length=0,0
for i in l[0:int(n/2)]:
    wide+=i
for i in l[int(n/2):n]:
    length+=i
print(wide**2+length**2)