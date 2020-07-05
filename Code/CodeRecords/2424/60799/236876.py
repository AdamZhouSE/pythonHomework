T = int(input())
for hhh in range(0, T):
    input()
    aList = [int(i) for i in input().split()]
    dict1 = {}
    for i in aList:
        if i in dict1.keys():
            dict1[i] += 1
        else:
            dict1[i] = 1
    for i in dict1.items():
        if i[1] % 2 == 1:
            print(i[0])