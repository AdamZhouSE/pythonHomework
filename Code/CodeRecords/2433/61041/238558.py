str = input()
for i in range(0,len(str)):
    if i!=len(str)-1:
        if str[i][1]>=str[i+1][0]:
        a = str[i][0]
        b = str[i+1][1]
        del str[i]
        del str[i]
        str.insert(i,[a,b])
        i = i - 1
    else:
        break
print(str)