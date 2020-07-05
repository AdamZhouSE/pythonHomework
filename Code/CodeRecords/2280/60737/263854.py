t = int(input())
while t:
    l = int(input())
    a = [int(n) for n in input().split( )]
    b = []
    for i in range(l):
        b.append(i+1)
    ret = list(set(b).difference(set(a)))
    print(ret[0])
    t -= 1
    