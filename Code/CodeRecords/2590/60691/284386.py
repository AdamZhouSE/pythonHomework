def gender(s):
    l = []
    for i in range(len(s)):
        l.append(s[i])

    l1 = []
    for i in range(len(l)):
        if l.count(l[i]) == 1 and l[i] != 'a' and l[i] != 'e' and l[i] != 'i' and l[i] != 'o' and l[i] != 'u':
            l1.append(l[i])
        else:
            continue

    if len(l1) % 2 == 0:
        return "SHE!"
    else:
        return "HE!"

n = int(input())

string = []
for i in range(n):
    string.append(input())


for i in range(n):
    print(gender(string[i]))