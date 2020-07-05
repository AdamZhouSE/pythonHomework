aa = input()
a = input().split(" ")
for i in range(len(a)):
    a[i] = int(a[i])
numnotzero = 0
zero = 0
for i in range(len(a)):
    if a[i] == 5:
        numnotzero = numnotzero + 1
    if a[i] == 0:
        zero = zero + 1
x = numnotzero // 9
if zero == 0:
    print(-1)
else:
    if x == 0:
            print(0)
    else:
        for i in range(x*9):
            print(5, end="")
        for i in range(zero-1):
            print(0, end="")
        print(0)