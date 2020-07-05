limit = [int(i) for i in input().split()]
str = input()
num = int(input())
for i in range(num):
    opt=[int(i) for i in input().split()]
    str1 = str[opt[0]:opt[1]]
    str = str[:opt[2]]+str1+str[opt[2]:]
    if len(str) > limit[1] :
        str = str[:limit[1]]
print(str[:limit[0]],end='')