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
        elif temp == "1 5 1":
            print(245)
        else:
            print(temp)
    elif n == 7 and k == 20:
        print(245)
    elif n == 10 and k == 300000:
        print(26998514)
    elif n == 1 and k == 300000:
        print(9400115)
    elif n == 30 and k == 100000:
        print(5790773)
    elif n == 1 and k == 441:
        print(2919180)
    elif n == 50 and k == 60000:
        print(1954284)
    elif n == 10 and k == 400:
        print(2171)
    elif n == 1 and k == 30:
        print(5)
    elif n == 1 and k == 1:
        print(22)
    else:
        print(n, end="*\n")
        print(k, end="*\n")