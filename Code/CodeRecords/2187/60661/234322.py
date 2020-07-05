t = int(input())
for i in range(t):
    nk = input()
    n = int(nk.split(' ')[0])
    k = int(nk.split(' ')[1])
    nums = input()
    nums=nums.split(' ')
    #求nums中最大的连续k个数
    nums_new = [int(x) for x in nums]
    temp = nums_new[0:k]
    res=0
    for l in range(k):
        res+=temp[l]
    max=res
    for j in range(n-k):
        res=res-temp[0]+nums_new[j+k]
        del temp[0]
        temp.append(nums_new[j+k])
        if(res>max): max=res
    print(max)
