target=input()
n=0
while int(n*(1+n)/2) < target:
    n+=1
if int(n*(1+n)/2)==target:
    print(n)
else:
    n-=1
    times=n+2*(target-int(n*(1+n)/2))
    print(times)