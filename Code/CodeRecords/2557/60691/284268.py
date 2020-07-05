def function(s):
    l1 = []
    l1.append(s[0])

    for i in range(1, len(s)):
        if l1[len(l1)-1] != s[i]:
            l1.append(s[i])
        else:
            continue

    s1 = "".join(l1)
    return s1


n = int(input())
string = []
for i in range(n):
    s1 = input()
    string.append(s1)

string2 = []
for i in range(n):
    string2.append(function(string[i]))

for i in range(n):
    print(string2[i])

