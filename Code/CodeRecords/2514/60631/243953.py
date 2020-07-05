s = input()
t = input()
ps = 0
ans=0
for i in t:
    if i == s[ps:ps+1]:
        ps=ps+1
    if s[ps:ps+1]=='':
        ans = 1
if ans==1:
    print('True')
else:
    print('False')