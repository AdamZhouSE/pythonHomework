def ans(nums):
    odd=[]
    even=[]
    for i in nums:
        if(i%2==0):
            even.append(i)
        else:
            odd.append(i)
    odd.sort(reverse=True)
    even.sort()
    return odd+even

numOfTests = int(input())
temp = []
for i in range(numOfTests):
    n = int(input())
    nums = []
    temp = input().split(" ")
    for t in temp:
        nums.append(int(t))
    res = ans(nums)
    for i in res:
        print(i,"",end="")
    print()
