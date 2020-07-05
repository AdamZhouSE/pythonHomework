n1, n2 = map(int, input().split())
s1 = input()
s2 = input()
loc = []
count = 0
for i in range(0, n2 - n1+1):
    match = True
    s = s2[i:i + n1]
    for j in range(0, n1):
        if s[j] == s1[j] or s[j] == '*' or s1[j] == '*':
            continue
        else:
            match=False
            break
    if match:
        count += 1
        loc.append(i + 1)
print(count)
for i in loc:
    print(i,end=" ")
print()    