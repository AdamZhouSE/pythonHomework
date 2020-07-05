X=int(input())
Y=int(input())
res=0
ans = 0
while Y > X:
    ans += 1
    if Y%2: Y += 1
    else: Y = int(Y/2)
res=ans + X-Y
print(res)