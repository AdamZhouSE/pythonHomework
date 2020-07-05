ll=input()[1:-1].split(",")
l=[]
for i in range(len(l)):
    if l[i]!='':
        l.append(int(l[i]))
l.sort()
n=len(l)
if n<=2:print([0,0])
else:
    maximum=max(l[n-1]-l[1]+2-n,l[n-2]-l[0]+2-n)
    minimum=maximum
    r = 0
    for le in range(n):
        while r + 1 < n and l[r + 1] - l[le] + 1 <= n:
            r += 1
        unoccupied = n - (r - le + 1)
        if r - le + 1 == n - 1 and l[r] - l[le] + 1 == n - 1:
            unoccupied = 2
        minimum = min(minimum, unoccupied)
    print([minimum,maximum])
