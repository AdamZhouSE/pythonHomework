s = input()
l_s = []
l_s.append(s)
for i in range(len(l_s)):
    if(l_s[i]==' '):
        del(l_s[i])
res = ''.join(l_s)
s_reverse = res[::-1]
print(s_reverse)