m,q = [int(i) for i in input().split(' ')]
arr = [int(i) for i in input().split(' ')]
arr = sorted(arr)
arr.reverse()
c,n = [],[]
x = 0
while(x < q):
    x+=1
    c1,n1 = [int(i) for i in input().split(' ')]
    c.append(c1)
    n.append(n1)
for i in range(len(c)):
    if c[i] == 1:
        print(arr[n[i]-1])
    elif c[i] == 2:
        arr.append(n[i])
        arr = sorted(arr)
        arr.reverse()
