s = input()
r_count = 0
l_count = 0
res = []
for i in range(len(s)):
    if s[i] == '(':
        l_count += 1
    elif s[i] == ')':
        r_count += 1
        if r_count > l_count and i != 0:
            for j in range(i-1,-1,-1):
                if s[j] == ')' and s[0:j] + s[j+1:len(s)] not in res:
                    res.append(s[0:j] + s[j+1:len(s)])
if res == []:
    res.append('')
print(res)
            
