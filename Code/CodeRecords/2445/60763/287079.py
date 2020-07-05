s1 = input().split(',')
# print(s1)
s = s1[0][s1[0].find("=")+3:len(s1[0])-1]
t = s1[1][s1[1].find("=")+3:len(s1[1])-1]
# print(s,t)
isSame = True
for i in range(len(s)):
    if t.count(s[i]) != s.count(s[i]):
        isSame = False
        break
if isSame:
    print('true')
else:
    print('false')