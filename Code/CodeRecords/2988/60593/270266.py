n=int(input())
s=input()
t=int(input())
r=[]
for i in range(t-1,len(s)):
    r.append(s[i])
print(''.join(r))