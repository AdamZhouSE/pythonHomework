s = input().strip()
s = s[:-1]
left = 0
match = True
for i in range(len(s)):
    if s[i]=='(':
        left += 1
    elif s[i]==')':
        left -= 1
    if left<0:
        match = False
        break
if left!=0:
    match = False
if match:
    print("YES",end='')
else:
    print("NO",end='')