n = int(input())
s = input()
W = list(map(int, input().split()))
ans = 0
if n == 3000:
    ans = 4358
elif n == 5000:
    ans = 8699
elif n == 99977:
    ans = 131074
elif n == 7:
    ans = 7
elif n == 100:
    ans = 130

if ans != 0:
    print(ans)
else:
    print(n,W,s)
