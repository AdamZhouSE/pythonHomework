def findSumPairs(nums,sum):
    i=0
    j=len(nums)-1
    ret=[]
    while i<j:
        a=nums[i]
        b=nums[j]
        if(a+b==sum):
            ret.append([a,b])
            i+=1
            j-=1
        elif a+b>sum:
            j-=1
        else:
            i+=1
    return ret
def printFormat(pairs,sum):
    if len(pairs)==0:
        print(-1)
    else:
        for pair in pairs:
            print(pair[0],pair[1],sum)
t=int(input())
while t:
    n=int(input())
    nums=[int(x) for x in input().split()]
    sum=int(input())
    printFormat(findSumPairs(nums,sum),sum)
    t-=1