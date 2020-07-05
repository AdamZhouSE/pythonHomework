m = int(input())
n = list(map(int, input().split()))
n = list(set(n))
n = sorted(n)
if len(n) == 1:
    print(0)
elif len(n) == 2:
    if abs(n[0]-n[1])%2==0:
        print(int(abs(n[0]-n[1])/2))
    else:    
        print(abs(n[0]-n[1]))
elif len(n) == 3:
    if abs(n[0]-n[1]) == abs(n[2]-n[1]):
        print(abs(n[0]-n[1]))
    else:
        print(-1)
else:
    print(-1)
