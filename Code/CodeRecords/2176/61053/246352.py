str = input()
dict = {}
str = str[::-1]
for i in range(0,len(str)):
    dict[len(str)-1-i] = str[i]
dict = sorted(dict.items(),key = lambda e:e[1])
for i in range(0,len(str)):
    if i != len(str)-1:
        print(dict[i][0]+1,end=" ")
    else:
        print(dict[i][0]+1)
