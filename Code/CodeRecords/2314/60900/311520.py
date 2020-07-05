n = int(input())
str = []
for i in range(0,n):
    str.append(input().split(' '))


def print1(tree):
    if (tree[1] != '0'):
        for i in range(0, n):
            if str[i][0] == tree[1]:
                print1(str[i])

    print(tree[0],end=' ')
    if (tree[2]!='0'):
        for i in range(0,n):
            if str[i][0]==tree[2]:
                print1(str[i])


print1(str[0])