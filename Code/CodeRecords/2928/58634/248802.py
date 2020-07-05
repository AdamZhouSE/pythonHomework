v = int(input())
nums = [int(i) for i in input().split(" ")]
sortedNums = nums.copy()
nums.reverse()
sortedNums.sort()
over = False
for i in range(9):
    if(v%sortedNums[i])==0:
        number = 9-nums.index(sortedNums[i])
        times = v//sortedNums[i]
        for j in range(times):
            print(number,end="")
        print()
        over = True
        break
if(not over):
    print(-1)

