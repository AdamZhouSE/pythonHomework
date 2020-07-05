def function(s1, s2):
    l1 = s1.split(' ')
    l2 = s2.split(' ')

    for i in range(len(l1)):
        l1[i] = int(l1[i])
        l2[i] = int(l2[i])

    l1.sort()
    l2.sort()
    
    result = []
    for i in range(len(l1)):
        result.append(abs(int(l1[i])-int(l2[i])))
    return max(result)


n = int(input())
string = [[]for i in range(n)]
num = []
for i in range(n):
    num.append(input())
    string[i].append(input())
    string[i].append(input())

for i in range(n):
    print(function(string[i][0], string[i][1]))
