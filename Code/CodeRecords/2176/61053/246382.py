str = input()
dict = {}
for i in range(0,len(str)):
    dict[i] = str[i:len(str)]
dict = sorted(dict.items(),key = lambda e:e[1])
for i in range(0,len(str)):
    if i != len(str)-1:
        print(dict[i][0]+1,end=" ")
    else:
        print(dict[i][0]+1)
