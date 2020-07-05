n = int(input())
s= []

for i in range(n):
    a, st = input().split()
    s.append(st)

ans = 0
for i in range(len(s)):
    for j in range(len(s)):
        if (s[i]+s[j]) == (s[i]+s[j])[::-1]:
            ans+=1
        if (s[j]+s[i]) == (s[j]+s[i])[::-1]:
            ans+=1
            
print(ans-n)