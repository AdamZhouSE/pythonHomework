t = int(input())
while t:
    n = int(input())
    a = [int(i) for i in input().split( )]
    b = [int(i) for i in input().split( )]
    c = [int(i) for i in input().split( )]
    count = 0
    for i in range(n):
        for k in range(n):
            if a[i] == b[i] +c[k]:
                count += 1
    print(count)
    t -= 1
    