s = input()
token = []
res = []
for i in range(len(s)):
    temp = ''
    for j in range(i,len(s)):
        temp  = temp + s[j]
        if temp in token:
            
            if len(temp) > len(res):
                res = temp
        else:
            token.append(temp)
print(''.join(res))
