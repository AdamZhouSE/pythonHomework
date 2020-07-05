n = int(input())
str = []
for i in range(0,n):
    str.append(input())


def print1(tree):
    print(tree[0],end='')
    if (tree[1]!='*'):
        for i in range(0,n):
            if str[i][0]==tree[1]:
                print1(str[i])
    if (tree[2]!='*'):
        for i in range(0,n):
            if str[i][0]==tree[2]:
                print1(str[i])


print1(str[0])