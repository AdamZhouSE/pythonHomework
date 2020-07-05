times = int(input())
for i in range(times):
    finish = False
    Set = set()
    length = int(input())
    nums = list(map(int, input().split(" ")))
    target = int(input())
    result = []
    for j in nums:
        if target-j in Set:
            finish = True
            result.append(str(target - j)+" "+str(j)+" "+str(target))
        else:
            Set.add(j)
    if not finish:
        print(-1)
    else:
        for m in range(len(result)):
            print(result[len(result)-m-1])
