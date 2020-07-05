a=int(input())
pre=2
now=2
while a>now:
    pre=now
    now*=2
target=[int(x) for x in str(a)]
c=[int(x) for x in str(pre)]
d=[int(x) for x in str(now)]
target.sort()
d.sort()
c.sort()
if(target==d or target==c or a==1):
    print(True)
else:
    print(False)