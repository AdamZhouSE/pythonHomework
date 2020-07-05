numOfInput = int(input())
for i in range(numOfInput):
    length = int(input())
    nums = input().split(" ")
    nums = list(map(int,nums))
    for j in range(length-1,0,-1):
        for k in range(length-j):
            if nums[k]<nums[k+j]:
                #就不是很理解
                print(j)
                break
        else:
            continue
        break