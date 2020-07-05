import collections
s=list(map(int,input().split(',')))
count = collections.Counter(s)
n= len(s)
judge=0
for x in range(2, n+1):
    if n % x == 0:
        if all(v % x == 0 for v in count.values()):
            judge=1
if(judge==0):
    print(False)
else:
    print(True)