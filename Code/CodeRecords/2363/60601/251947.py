N = eval(input())
s = str(bin(N))
#print(s[2:])
s = list(s[2:])
for i in range(len(s)):
    if s[i]=='1':
        s[i] = '0'
    else:
        s[i] = '1'
print(int(''.join(s),2))