def function(s):
    l1 = []

    for i in range(len(s1)):
        if not s1[i] in l1:
            l1.append(s1[i])

    s = "".join(l1)
    return s


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
