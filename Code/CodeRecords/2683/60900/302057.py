n =int(input())
str = []
for i in range(0,n):
    str.append(input())
results=[]

for i in range(0,n):
    result = 1
    maxl=0
    for j in range(0,len(str[i])-1):
        line =str[i][j]
        for m in range(j+1,len(str[i])):
            if str[i][m]>line:
                result+=1
                line = str[i][m]
            else:
                continue
        maxl = max(maxl,result)
        result =1

    print(maxl)