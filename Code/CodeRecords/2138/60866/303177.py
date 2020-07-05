def subarraySum(nums, k):
    dict_s = {0:1}
    ret = 0 
    ans = 0
    for i in range(len(nums)):
        ans = ans + nums[i]   
        temp = ans - k   
        ret += dict_s.get(temp, 0) 
        dict_s[ans] = dict_s.get(ans, 0) + 1                   
    return ret!=0
a=input().split(',')
a=[int(x) for x in a]
k=int(input())
print(subarraySum(a,k))