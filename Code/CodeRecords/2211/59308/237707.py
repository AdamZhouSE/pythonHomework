import re
pattern = re.compile('[0-9]+')


def find_name(name):
    counts = 0
    for j in q_name:
        if j[:len(name)] == name:
            counts += 1
    return counts


a = pattern.findall(input())
n, k = int(a[0]), int(a[1])
c = list()
p = list()
q_name = list()
M = input().split(" ")
c.append(M[0])
p.append(int(M[1]))
q_name.append(c[0])
for i in range(1, n):
    M = input().split(" ")
    c.append(M[0])
    p.append(int(M[1]))
    q_name.append(c[i] + q_name[p[i]-1])

for i in range(k):
    q = input()
    print(find_name(q))

