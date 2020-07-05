#10
s = input()
dup = []
for c in s:
    if c not in dup:
        dup.append(c)
dup.sort()
s = list(s)
s.reverse()
s = "".join(s)
outcome = []
for c in dup:
    for i in range(0,len(s)):
        if s[i] ==  c:
            outcome.append(len(s)-i)
for i in range(0,len(outcome)-1):
    print(outcome[i],end=" ")
print(outcome[len(outcome)-1])



