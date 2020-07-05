def count(s, sorts):
    a = 0
    for i in range(len(s) - 8):
        temp = s[i: i+9]
        temp = sor(temp)
        if temp == sorts:
            a+=1
    return a

def sor(s):
    s = list(s)
    s.sort()
    t = ''
    for i in s:
        t+=i
    return t


s = input()
n = int(input())

ans = 0
for i in range(n):
    code = input()
    ans += count(s, sor(s))
    
print(ans)