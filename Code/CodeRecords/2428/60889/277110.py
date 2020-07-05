numOfInput = int(input())
for i in range(numOfInput):
    length = int(input())
    nums = input().split(" ")
    nums = list(map(int,nums))
    oddNums = []
    evenNums = []
    for j in nums:
        if j%2==1:
            oddNums.append(j)
        else:
            evenNums.append(j)
    oddNums.sort()
    evenNums.sort()
    oddNums.reverse()
    nums = oddNums+evenNums
    for j in nums:
        print(j,end=" ")
    print("")