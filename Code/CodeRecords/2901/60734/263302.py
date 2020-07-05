n = int(input())
flag = True
pre = n&1
while n>1:
    n = n>>1
    if n&1 == pre:
        flag = False
        break
    pre = n&1
print(flag)