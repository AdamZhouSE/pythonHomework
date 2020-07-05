totalTests = int(input())
string1s = []
string2s = []
for i in range(0, totalTests):
    string1s.append(input())
    string2s.append(input())
for i in range(0, totalTests):
    string1 = string1s[i]
    string2 = string2s[i]
    if len(string1) >= len(string2):
        if not string1.startswith(string2):
            print("No")
        else:
            print("Yes")
    else:
        if not string2.startswith(string1):
            print("No")
        else:
            print("Yes")
