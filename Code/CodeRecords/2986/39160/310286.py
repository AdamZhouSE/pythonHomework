import difflib

a = input()
b = input()

ans = 0
ans += abs(len(a)-len(b))

l = min(len(a), len(b))
for i in range(l):
    if a[i] != b[i]:
        ans+=1
        
print(ans)