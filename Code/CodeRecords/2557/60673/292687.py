

t=int(input())
for i in range(t):
    str1=input()
    front=str1[0]
    res=""
    res+=front
    for i in range(1,len(str1)):
        if(str1[i]!=front):
            res+=str1[i]
        front=str1[i]
    print(res)


