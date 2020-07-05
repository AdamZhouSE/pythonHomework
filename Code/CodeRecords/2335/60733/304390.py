X=int(input())
Y=int(input())
ans = 0
while Y > X:
    ans += 1
    if Y%2:
        Y += 1
    else:
        Y =Y// 2
ans = ans + X-Y
print(ans)