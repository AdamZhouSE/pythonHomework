def getkeyvalue(c):
    for i in range(len(s)):
        if s[i]==c:
            return i
    return len(s)
s=list(input())
t=list(input())
t.sort(key=getkeyvalue)
for i in t:
    print(i,end="")
print()