times = int(input())
for i in range(times):
    length = int(input())
    nums = list(map(int, input().split(" ")))
    j = 0
    finish = False
    result = []
    while j < length-1:
        start = j
        while j < length-1 and nums[j] < nums[j+1]:
            j += 1
        if start != j:
            result.append("("+str(start) +" " +str(j)+")")
            finish = True
        j += 1
    if finish:
        for k in range(len(result)-1):
            print(result[k], "", end="")
        print(result[-1])
    else:
        print("没有利润")
