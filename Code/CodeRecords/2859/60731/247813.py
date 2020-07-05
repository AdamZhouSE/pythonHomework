num=int(input())
str1=input()
alpha=str1[0]
beta=str1[1]
judge=True
for i in range(1,num):
    str=input()
    for j in range(num):
        if j==i or j==num-1-i:
            if str[j]!=alpha:
                judge=False
                break
        else:
            if str[j]!=beta:
                judge=False
                break
if judge:
    print('YES')
else:
    print('NO')