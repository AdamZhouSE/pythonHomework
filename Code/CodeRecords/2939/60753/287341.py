import sys
import re
def findset(arr, k):
    if len(arr) >= 10*k:
        return list(set(arr))
    else:
        copy=[]
        for p in arr:
            copy.append(p)
        for p in copy:
            arr.append(2 * p + 1)
            arr.append(4 * p + 5)
        arr=list(set(arr))
        return findset(arr, k)
def findmaxnum(res, arr, indx, standlen, isUsed):
    n = len(arr)
    if indx == n:
        ans = []
        for i in range(n):
            if isUsed[i] == 1:
                ans.append(arr[i])
        strans=""
        for j in range(len(ans)):
            strans+=ans[j]
        if len(strans) == standlen:
            numans = int(strans)
            res.append(numans)
    else:
        isUsed[indx] = 0
        findmaxnum(res, arr, indx + 1, standlen, isUsed)
        isUsed[indx] = 1
        findmaxnum(res, arr, indx + 1, standlen, isUsed)


s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums=[int(e) for e in digits]
k=nums[0]
m=nums[1]
arr = findset([1], k)
arr.sort()
origin = ""
for i in range(k):
    origin+=str(arr[i])
print(origin)
ans = []
maxnum = 9
l = len(origin)
orilist = list(origin)
isUsed = [0] * l
res = []
findmaxnum(res, orilist, 0, l - m, isUsed)
sys.stdout.write(str(max(res)))
