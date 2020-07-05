def reversegroup(nums,k):
    i = 0
    while i < len(nums):
        nums[i:i+k] = nums[i:i+k][::-1]
        i = i + k

if __name__ == "__main__":
    testNo = int(input())
    ans = []
    for i in range(0,testNo):
        N,K = map(int,input().split())
        nums = list(map(int,input().split()))
        reversegroup(nums,K)
        ans.append(nums)
    for lst in ans:
        for no in lst:
            print(no,end=" ")
        print()
