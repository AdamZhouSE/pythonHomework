num = int(input())
pre = -1
while num > 0:
    if pre == -1:
        pre = num & 1
        num >>= 1
    else:
        if num&1 == pre:
            print("False")
            break
        else:
            pre = num&1
            num >>= 1
if num == 0:
    print("True")
