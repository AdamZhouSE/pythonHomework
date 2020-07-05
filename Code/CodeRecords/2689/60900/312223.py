n = int(input())
str = []
for i in range(0,n):
    str.append(input().split(' '))
for i in range(0,n):
    print(len(set(str[i][0]+str[i][1])))