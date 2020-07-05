def is_same(lst1,lst2):
    nums = {}
    for i in lst1:
        if i in nums:
            nums[i] = nums[i] + 1
        else:
            nums[i] = 1
    for j in lst2:
        if not j in nums:
            return False
        if j in nums:
            if nums[j]==0:
                return False
            else:
                nums[j] = nums[j] - 1
    return True

if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(testNO):
        N = int(input())
        lst1 = list(map(int,input().split()))
        lst2 = list(map(int, input().split()))
        ans.append(is_same(lst1,lst2))
    for res in ans:
        if res:
            print(1)
        else:
            print(0)