def rotatelst(nums,d):
    nums = nums[d:] +nums[0:d]
    return nums

if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(0,testNO):
        numNo = int(input())
        numlst = list(map(int,input().split()))
        d = int(input())
        ans.append(rotatelst(numlst,d))
    for lst in ans:
        for i in lst:
            print(i,end=" ")
        print()