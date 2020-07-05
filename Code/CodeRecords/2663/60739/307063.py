def getlist(target):
    list1 = []
    list2 = []

    ans = 0
    for i in range(target * 3):
        ans = ans + i
        if i % 2 == 0:
            list1.append(ans)
        else:
            list2.append(ans)
    
    return list1[target]

n = int(input())
for i in range(n):
    t = int(input())
    print(getlist(t))