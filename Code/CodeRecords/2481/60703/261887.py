T = int(input())
for i in range(T):
    res = 0
    m = input()
    list1 = set([int(x) for x in input().split(" ")])
    list2 = set([int(x) for x in input().split(" ")])
    for i in list1:
        if i in list2:
            res+=1
    print(res)