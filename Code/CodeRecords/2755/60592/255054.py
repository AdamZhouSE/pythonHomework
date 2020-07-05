tests = int(input())
for i in range(0,tests):
    nums = input().split(' ')
    le1 = int(nums[0])
    le2 = int(nums[1])
    res = [0]*(le1+le2)
    arr1 = list(map(int,input().split(' ')))
    arr2 = list(map(int,input().split(' ')))
    for j in range(0,le1):
        for h in range(0,le2):
            res[j+h] += arr1[j]*arr2[h]
    res = list(map(str,res))
    print(' '.join(res[0:len(res)-1]))