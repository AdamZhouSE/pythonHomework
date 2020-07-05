def judge_sum(nums,target):
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return True
    return False

if __name__ == "__main__":
    testNo = int(input())
    ans = []
    for i in range(0,testNo):
        N,X = map(int,input().split())
        nums = list(map(int,input().split()))
        if judge_sum(nums,X):
            ans.append("Yes")
        else:
            ans.append('No')
    for str in ans:
        print(str)