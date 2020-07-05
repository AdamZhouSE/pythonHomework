s = list(input())
if len(s) == 0:
    print(0)
if len(s) == 1:
    print(1)
l = len(s)
maxLen = 0
dic = {}
left = 0
for i in range(l):
    if s[i] in dic:
        c = dic[s[i]]
        left = max(left,c + 1)
        dic.pop(s[i])
    dic[s[i]] = i
    maxLen = max(maxLen,i -left + 1)
print(maxLen)