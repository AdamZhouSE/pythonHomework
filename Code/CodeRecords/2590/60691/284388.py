def gender(s):
    l = []
    for i in range(len(s)):
        if not s[i] in l and s[i] != 'a' and s[i] != 'e' and s[i] != 'i' and s[i] != 'o' and s[i] != 'u':
            l.append(s[i])
        else:
            continue

    if len(l) % 2 == 0:
        return "SHE!"
    else:
        return "HE!"


n = int(input())

string = []
for i in range(n):
    string.append(input())


for i in range(n):
    print(gender(string[i]))