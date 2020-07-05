numOfInput = int(input())
for i in range(numOfInput):
    nums = input().split(" ")
    num1 = int(nums[0])
    num2 = int(nums[1])
    loc = 0
    if num1==num2:
        print(-1)
        continue
    while num1%2 == num2%2:
        num1 = int(num1/2)
        num2 = int(num2/2)
        loc = loc + 1
    print(loc)