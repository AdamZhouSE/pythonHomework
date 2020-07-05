n=int(input())
l=[]
for i in range(n):
    tmp=list(map(int,input().split()))
    l.append(tmp[0]*60+tmp[1])
Max=0
for i in list(set(l)):
    Max=max(Max,l.count(i))
print(Max)
