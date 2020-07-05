s = input()
res = 0
temp = ''
for i in range(len(s)-1):
    if(s[i] == s[i+1]):
        pass
    else:
        res+=1
        temp = s[i+1]
print(res+1,end = '') if temp == '0' else print(res,end = '')