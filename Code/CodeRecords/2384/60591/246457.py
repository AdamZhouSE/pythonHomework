def find(nums):
    nums = list(map(int,nums.split(" ")))
    i = 1
    while(True):
        if(not i in nums):
            return i
        i = i + 1

n = eval(input())
while(n != 0):
    n = n - 1
    input()
    print(find(input()))