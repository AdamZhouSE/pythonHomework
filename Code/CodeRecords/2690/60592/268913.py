tests = int(input())
for i in range(0,tests):
    res = 0
    chstr = []
    nums = list(map(int,input().split()))
    len1 = nums[0]
    len2 = nums[1]
    ls = input().split()
    str1 = list(ls[0])
    str2 = list(ls[1])
    for j in range(0,len1):
        if str1[j] in str2:
            chstr.append(str1[j])
    