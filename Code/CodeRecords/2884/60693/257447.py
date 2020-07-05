from collections import defaultdict


def spy_unit(heights,n,k):
    dict=defaultdict(list)
    for i in range(n-1):
        for j in range(i+1,n):
            if abs(heights[i]-heights[j])<=k:
                dict[heights[i]].append(heights[j])
                dict[heights[j]].append(heights[i])
    res=0
    for key in dict.keys():
        res+=len(dict.get(key))
    return res

n_k=input().split()
n,k = int(n_k[0]),int(n_k[1])
heights=list(map(int,input().split()))
print(spy_unit(heights,n,k))