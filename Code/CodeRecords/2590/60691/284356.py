def gender(s):
    l = []
    for i in range(len(s)):
        l.append(s[i])
        
    l1 = []
    for i in range(len(l)):
        if l.count(l[i]) == 1:
            l1.append(l[i])

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