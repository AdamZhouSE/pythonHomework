t = int(input())
while t:
    N = int(input())
    a = [int(n) for n in input().split( )]
    b = [int(n) for n in input().split( )]
    a.sort()
    b.sort()
    print(1 if a==b else 0)
    t -= 1
    