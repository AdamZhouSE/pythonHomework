n=int(input())
s=input()
r=[]
for i in range(n-1,len(s)):
    r.append(s[i])
print(''.join(r))