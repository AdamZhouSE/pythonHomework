numOfInput = int(input())
for i in range(numOfInput):
    length = input()
    nums = input().split(" ")
    nums = list(map(int,nums))
    product = 1
    for i in nums:
        product = product * i
    for i in nums:
        print(int(product/i),end=" ")
    print("")