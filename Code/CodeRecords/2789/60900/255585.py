n = input()
res=[]
for i in range (0,int(n)):
    p = input()
    res.append(input().split(" "))

result =0

for i in range(0,int(n)):
    for j in range(0,len(res[i])):
        res[i][j]=int(res[i][j])

for i in range(0,int(n)):
    while(len(res[i])!=0):
        if (len(res[i])>min(res[i])):
            del res[i][res[i].index(min(res[i]))]
        else:
            result = len(res[i])
            break
    print(result)
