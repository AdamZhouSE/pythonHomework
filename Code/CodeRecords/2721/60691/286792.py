def multiply(s1, s2):
    n1 = int(s1, 2)
    n2 = int(s2, 2)
    return n1 * n2


n = int(input())
string = []
for i in range(n):
    string.append(input())

for i in range(n):
    l = string[i].split(' ')
    print(multiply(l[0], l[1]))