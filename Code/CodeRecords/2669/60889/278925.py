def printAllNum(nums,summary):
    if len(nums)==0:
        if summary == 0:
            print(0,end=" \n")
        else:
            print(summary,end = " ")
    else:
        newNums = nums.copy()
        del newNums[0]
        printAllNum(newNums.copy(),summary+nums[0])
        printAllNum(newNums.copy(),summary)

numOfInput = int(input())
for i in range(numOfInput):
    num = int(input())
    locOf2 = []
    j = 1
    while num != 0:
        if num % 2 == 1:
            locOf2.insert(0,j)
        num = int(num/2)
        j = j * 2
    printAllNum(locOf2,0)