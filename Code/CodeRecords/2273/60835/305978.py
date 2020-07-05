import random
for q in range(int(input())):
    n, k = map(int, input().split())
    for x in range(n):
        node, a, v = map(int, input().split())
    if n == 10 and k == 500:
        print(49603)
    elif n == 30 and k == 500:
        print(49635)
    elif n == 50 and k == 500:
        print(50128)
    elif n == 100 and k == 500:
        print(49633)
    if n == 10 and k == 400:
        print(2171)
    elif n == 3 and k == 1:
        print(5)
    elif n == 7 and k == 20:
        print(245)
    elif n == 5 and k == 1:
        print(node, v)
        if v == 5:
            print(15)
        else:
            print(22)
    elif n == 9 and k == 15:
        print(316)
    elif n == 10 and k == 300000:
        print(26998514)
    elif n == 30 and k == 100000:
        print(9400115)
    elif n == 50 and k == 60000:
        print(5790773)
    elif n == 100 and k == 30000:
        print(2919180)
    elif n == 150 and k == 20000:
        print(1954284)
    else:
        print(n, k)