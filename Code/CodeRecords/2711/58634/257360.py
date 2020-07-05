def isAnagram(x,y):
    d = 0
    if x == y:
        return True
    if len(x) != len(y):
        return False
    for i in range(len(y)):
        if x[i] != y[i]:
            d+=1
    if d>2 or d == 1:
        return False
    return True

strs = eval(input())
res = 0
for i in range(len(strs)-1):
    for j in range(i+1,len(strs)):
        if isAnagram(strs[i],strs[j]):
            res += 1
print(res)