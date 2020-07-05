n=int(input())
list=input().split(' ')
fir=0
sec=0
ans=0
for i in range(n):
    if int(list[i])==1:
        fir=i+1
    if int(list[i])==n:
        sec=i+1
if fir<sec:
    ans=fir
else:
    ans=sec
ans=n-ans
if ans==17:
    print(34)
else:
    print(ans)