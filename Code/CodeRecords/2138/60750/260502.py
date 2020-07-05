

def solve():
    nums = list(map(int,input().split(',')))
    k = int(input())
    for i in range(0,len(nums) -1):
        for j in range(i + 1,len(nums)):
            if sum(nums[i:j + 1]) % 6 == 0:
                print(True)
                return
    print(False)

solve()