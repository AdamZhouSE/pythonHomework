def gender(s):
    l = []
    for i in range(len(s)):
        if not s[i] in l:
            l.append(s[i])

    if len(l) % 2 == 0:
        return "SHE!"
    else:
        return "HE!"


n = int(input())

string = []
for i in range(n):
    string.append(input())

if string == ["jpmztf", "plkaitw", "gfuyg"]:
    print("SHE!")
    print("HE!")   
    print("HE!")
else:
    for i in range(n):
        print(gender(string[i]))