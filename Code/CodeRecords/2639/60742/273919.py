s = input()
k = int(input())
l = 0
r = 0
res = 0
d = {}
d[s[0]] = 1
while l<len(s):
    maxNum = max(list(d.values()))
    if maxNum+k>r+1-l or (maxNum+k==r+1-l and r+1<len(s) and s[r+1] in d and d[s[r+1]]==maxNum):
        r += 1
        if r<len(s):
            if s[r] in d:
                d[s[r]] += 1
            else:
                d[s[r]] = 1
        else:
            res = max(r-l,res)
            break
    else:
        res = max(r+1-l,res)
        d[s[l]] -= 1
        l += 1
print(res)