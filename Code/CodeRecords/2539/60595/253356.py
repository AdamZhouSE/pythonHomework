def Test():
    nums=eval(input())
    a=copy(nums)
    a.sort()
    i = 0
    j = len(nums)-1
    while (nums[i] == a[i] and i < j):
        i =i+1
    while (nums[j] == a[j] and i < j):
        j=j-1
    if (i == j):
        print(0)
    else:
        print(j-i+1)
def copy(nums):
    result=[]
    for x in nums:
        result.append(x)
    return result
if __name__ == "__main__":
    Test()