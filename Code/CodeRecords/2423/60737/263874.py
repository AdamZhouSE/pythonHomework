t = int(input())
while t:
    cmd = [int(n) for n in input().split( )]
    a = [int(n) for n in input().split( )]
    b = [int(n) for n in input().split( )]
    print('Yes' if set(a).issuperset(set(b)) else 'No')
    t -= 1
    