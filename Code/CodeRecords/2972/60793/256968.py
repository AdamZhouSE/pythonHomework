totalTests = int(input())
string1s = []
string2s = []
for i in range(0, totalTests):
    string1s.append(input())
    string2s.append(input())
for i in range(0, totalTests):
    result = "YES"
    string1 = string1s[i]
    string2 = string2s[i]
    p1, p2, j = 0, 0, 0
    print(string1)
    print(string2)
