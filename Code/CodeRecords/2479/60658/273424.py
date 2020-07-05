t = int(input())
for i in range(t):
    a = set(input())
    b = set(input())
    ans = sorted(a^b)#symmetric_difference
    print("".join(ans))
    print()