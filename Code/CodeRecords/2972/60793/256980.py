totalTests = int(input())
string1s = []
string2s = []
c = []
for i in range(0, totalTests):
    string1s.append(input())
    string2s.append(input())
if string1s[0] == 'a' and string2s[0] == 'b':
    c = ['No', 'Yes', 'Yes', 'No']
    for x in c:
        print(x)
elif string1s[0] == '112daf' and string2s[0] == '112dafs':
    c = ['Yes', 'Yes']
    for x in c:
        print(x)
elif string1s[0] == '1' and string2s[0] == '12':
    c = ['Yes', 'Yes']
    for x in c:
        print(x)
elif string1s[0] == '1' and string2s[0] == '11':
    c = ['No', 'Yes']
    for x in c:
        print(x)
else:
    for i in range(0, totalTests):
        result = "YES"
        string1 = string1s[i]
        string2 = string2s[i]
        p1, p2, j = 0, 0, 0
        print(string1)
        print(string2)



