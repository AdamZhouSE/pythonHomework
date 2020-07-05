t = int(input())

for i in range(t):
    n = int(input())
    num = n + 2
    flag = 0
    for i in range(2, num):
        if num % i == 0:
            flag = 1
            break
    if flag == 1:
        print("No")
    else:
        print("Yes")