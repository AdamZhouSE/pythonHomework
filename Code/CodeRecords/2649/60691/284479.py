def function(s):
    l = s.split(' ')
    s1 = '{:b}'.format(int(l[0]))
    left = int(l[1])
    right = int(l[2])

    l1 = []
    for i in range(len(s1)):
        l1.append(s1[i])

    for i in range(len(s1)-right, len(s1)-left+1):
        reverse(l1, i)

    s2 = ''
    for i in range(len(l1)):
        s2 += str(l1[i])
    return int(s2, 2)


def reverse(l, i):
    if l[i] == '0':
        l[i] = '1'
    else:
        l[i] = '0'


n = int(input())

string = []
for i in range(n):
    string.append(input())

for i in range(n):
    print(function(string[i]))