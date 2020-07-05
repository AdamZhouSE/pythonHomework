def function(s):
    l = s.split(' ')

    if int(l[0]) % 2 == 0:
        return (int(l[0]) // 2) * int(l[1])
    else:
        return (int(l[0]) // 2 + 1)*int(l[1])


n = int(input())
string = []
for i in range(n):
    string.append(input())

for i in range(n):
    print(function(string[i]))