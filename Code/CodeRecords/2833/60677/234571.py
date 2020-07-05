n=int(input())
cola=input().split()
cola=[int(x) for x in cola]
can=input().split()
can=[int(x) for x in can]
can.sort()
sum=can[-1]+can[-2]
n=0
for i in cola:
    n+=i
if n<=sum:
    print("YES")
else:
    print("NO")