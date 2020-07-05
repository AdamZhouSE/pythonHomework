import collections
nums=input()
k=int(input())
maxlen,start,maxfre=0,0,0
freDict=collections.defaultdict(int)
for end in range(len(nums)):
    rightChar=nums[end]
    freDict[rightChar]+=1
    maxfre=max(freDict[rightChar],maxfre)
    if((end-start+1-maxfre)>k):
        leftChar=nums[start]
        start+=1
        freDict[leftChar]-=1
    maxlen=max(maxlen,end-start+1)
print(maxlen)