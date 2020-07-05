#main-----
n = int(input())
if n == 0:
    print(0)
else:
    temp = n%9
    if temp == 0:
        print(9)
    else:
        print(temp)