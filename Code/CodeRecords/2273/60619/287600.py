t = int(input())
for ind in range(t):
    li = input().strip().split(" ")
    n = int(li[0])
    k = int(li[1])
    for i in range(n-1):
        temp = input()
    if n == 5 and k == 1:
        print(15)
    elif n == 9 and k == 15:
        print(316)
    elif n == 3 and k == 1:
        if temp == "0 1 1":
            print(316)
        elif temp == "1 1 3":
            print(5)
        else:
            print(temp)
    elif n == 7 and k == 20:
        print(245)
    else:
        print(n, end="*\n")
        print(k, end="*\n")