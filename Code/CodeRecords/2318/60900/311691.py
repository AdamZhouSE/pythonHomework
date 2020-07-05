s= input().split(' ')
n =int(s[0])
s = int(s[1])
str = []
for i in range(0,n):
    str.append(input().split(' '))
    for j in range(0,3):
        str[i][j]=int(str[i][j])


def judge(tree):
    if tree[1] == tree[2] ==0:
        return 1
    elif tree[1]<tree[0] and tree[2]==0:
        return 2
    elif tree[1]==0 and tree[2]>tree[0]:
        return 2
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
temp = 0
for i in range(0,n):
    if result <judge(str[i]):
        result = judge(str[i])
        temp = str[i][0]
if temp==s:
    result+=1
    
print(result)
