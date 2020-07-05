s= input().split(' ')
n =int(s[0])
str = []
for i in range(0,n):
    str.append(input().split(' '))
    for j in range(0,3):
        str[i][j]=int(str[i][j])


def judge(tree):
    if tree[1] == tree[2] ==0:
        return 1
    elif tree[1]<tree[0] and tree[2]==0:
        for i in range(0, n):
            if str[i][0] == tree[1]:
                t =judge(str[i])
        if t==-1:return -1
        else: return t+1
    elif tree[1]==0 and tree[2]>tree[0]:
        for i in range(0, n):
            if str[i][0] == tree[2]:
                t = judge(str[i])
        if t == -1:
            return -1
        else:
            return t + 1
    elif tree[1]>=tree[0] or tree[2]<=tree[0]:
        return -1
    else:
        for i in range(0, n):
            if str[i][0] == tree[1]:
                a =judge(str[i])
        for i in range(0, n):
            if str[i][0] == tree[2]:
                b =judge(str[i])
        if a ==-1 or b ==-1:
            return -1
        else:
            return a+b+1

result = 0
for i in range(0,n):
    result = max(result,judge(str[i]))
print(result)