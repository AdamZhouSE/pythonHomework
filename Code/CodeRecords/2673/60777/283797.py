case=int(input())

for i in range(case):
    num=int(input())
    b=bin(num)[2:]
    res=b[0]
    for j in range(1,len(b)):
        if(b[j]=='1'):
            res+=str(int(res[j-1])^1)
        else:
            res+=res[j-1]
    print(int(res,2))