import collections


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k < 1 or t < 0:
            return False
        numDict = collections.OrderedDict()
        for x in range(len(nums)):
            key = nums[x] / max(1, t)
            for m in (key, key - 1, key + 1):
                if m in numDict and abs(nums[x] - numDict[m]) <= t:
                    return "true"
            numDict[key] = nums[x]
            if x >=  k:
                numDict.popitem(last=False)
        return "false"

t=Solution()
s=input()
T=int(s[len(s)-1])
num=[]
i=0
check=0
k=0
already=0
while (i<len(s)):
    if s[i]=='[':
        check=1
        while(s[i]!=']'):
            num.append(s[i])
            i+=1
    c=s[i]
    if check==1 and '0'<=s[i]<='9' and already==0:
        k=int(s[i])
        already+=1
    i+=1
nums="".join(num)+']'
print(t.containsNearbyAlmostDuplicate(eval(nums),k,T))