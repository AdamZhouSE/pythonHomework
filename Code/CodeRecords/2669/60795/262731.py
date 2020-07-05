T=int(input())
for i in range(0,T):
    num=int(input())
    re=[]
    for j in range(0,num+1):
        if num&j==j:
            re.insert(0,j)
    for j in range(0,len(re)):
        print(re[j],end=" ")
    print("")
