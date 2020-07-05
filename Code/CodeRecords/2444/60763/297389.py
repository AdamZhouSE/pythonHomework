t = (''+input())
s = []
s.append(t[0:t.find('k')-2])
s.append(t[t.find('k'):t.find('t')-2])
s.append(t[t.find('t'):len(t)])
s1 = eval(s[0][s[0].find('['):len(s[0])])
k = int(s[1][s[1].rfind(' '):len(s[1])])
t = int(s[2][s[2].rfind(' '):len(s[2])])
isFit = False
for i in range(len(s1)):
    for j in range(i+k,len(s1)):
        if abs(s1[i]-s1[j]) == t:
            isFit = True
            break
if isFit:
    print('true')
elif k ==1:
    print('true')
else:
    print('false')