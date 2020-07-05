def solve():
    input()
    nums = list(map(int, input().split()))
    i=0
    total=len(nums)
    for i in range(total-1):
        if nums[i]>=nums[i+1]:
            break
    i+=1
    for i in range(i,total-1):
        if nums[i]>nums[i+1]:
            break
        if nums[i]<nums[i+1]:
            print("NO")
            return
    i+=1
    for i in range(i,total-1):
        if nums[i]<=nums[i+1]:
            print("NO")
            return
    print("YES")

if  __name__ == '__main__' :
    solve()