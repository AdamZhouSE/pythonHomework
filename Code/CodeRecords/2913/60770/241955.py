def solve():
    input()
    nums = list(map(int, input().split()))
    nums.sort(reverse=True)
    while(nums[1]!=0):
        nums[0]-=1
        nums[1]-=1
        nums.sort(reverse=True)
    if nums[0]==0:
        print("YES")
    else:
        print("NO")

if  __name__ == '__main__' :
    solve()