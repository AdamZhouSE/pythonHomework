def function(s1, s2):
    l1 = s1.split(' ')
    l2 = s2.split(' ')

    for i in range(len(l2)):
        l2[i] = int(l2[i])

    result = []
    for i in range(len(l2) - int(l1[1])):
        result.append(str(max(l2[i:i+int(l1[1])])))
        result.append(' ')
    result.append(str(max(l2[len(l2) - int(l1[1]):len(l2) - int(l1[1])+int(l1[1])])))
    return ''.join(result)


n = int(input())
num = []
string = []
for i in range(n):
    num.append(input())
    string.append(input())

for i in range(n):
    print(function(num[i], string[i]))