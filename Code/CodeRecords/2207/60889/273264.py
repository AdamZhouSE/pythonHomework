numOfInput = int(input())
for i in range(numOfInput):
    nums = input().split(" ")
    num1 = int(nums[0])
    num2 = int(nums[1])
    if num1 >= num2*(num2+1)/2:
        print(1)
    else:
        print(0)