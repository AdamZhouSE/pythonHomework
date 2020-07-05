def judgeRepeated(array):
    nums={}
    for i in array:
        if i  not in nums:
            nums[i]=True
        else:
            return True
    return False


T = int(input())
for i in range(T):
    N = int(input())
    s = list(map(int,(''+input()).split(' ')))
    count = 0
    for j in range(len(s)):
        for k in range(j+1,len(s)+1):
            # print(s[j:k])
            if  not judgeRepeated(s[j:k]):
                count += k-j
    print(count)