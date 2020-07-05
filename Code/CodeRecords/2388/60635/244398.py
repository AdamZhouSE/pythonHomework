num = int(input())
for n in range(num):
    l = int(input())
    a1 = [int(x) for x in input().split()]
    a2 = [int(x) for x in input().split()]
    a1.sort()
    a2.sort()
    if a1==a2:
        print(1)
    else:
        print(0)