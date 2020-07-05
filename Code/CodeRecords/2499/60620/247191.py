n=int(input())
result=[]
r=[]
for i in range(n):
    s=input().split()
    if(s[0]=="Add"):
        a=int(s[1])
        b=int(s[2])
        c=int(s[3])
        result.append([a,b,c])
        r.append([a,b,c])
    if(s[0]=="Query"):
        k=int(s[1])
        num=0
        for j in range(len(result)):
            if((result[j][0]*k+result[j][1])>result[j][2]):
                num+=1
        print(num)
    if(s[0]=="Del"):
        x=int(s[1])
        if(result):
            del(result[result.index(r[x-1])])
        else:
            break