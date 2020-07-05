orin = int(input())
str = list(map(int,input().split(' ')))
com = int(input())
for i in range(0,com):
    ls = input().split(' ')
    if ls[0]=='add':
        str.append(int(ls[1]))
    else:
        str.sort()
        if len(str)%2==1:
            print(str[int(len(str)/2)])
        else:
            print(str[int(len(str)/2)-1])