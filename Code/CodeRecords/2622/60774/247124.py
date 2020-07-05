s = input().replace(',','')
maxNum = 0
maxEle = ''
for i in range(0,len(s)):
    if(s.count(s[i]) > maxNum):
        maxNum = s.count(s[i])
        maxEle = s[i]
print(maxEle)