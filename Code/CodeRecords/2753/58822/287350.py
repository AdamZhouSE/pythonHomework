def find(k,a,b,c):
    res=0
    if(c==0):
        for i in range(len(k)):
            if (k[i][0] == a and k[i][1] == b):
                    return int(k[i][2])
        return -1
    for i in range(len(k)):
        if(k[i][0]==a):
            if  (find(k,k[i][1],b,c-1)) !=(-1):
                re=k[i][2]+find(k,k[i][1],b,c-1)
                if(res==0):
                    res=re
                else:
                    if(res>re):
                        res=re
    return res


num=int(input())
k=eval(input())
a=int(input())
b=int(input())
c=int(input())
val=0
for i in range(len(k)):
    k[i][0]=int(k[i][0])
    k[i][1]=int(k[i][1])
    k[i][2]=int(k[i][2])
for i in range(len(k)):
    if(int(k[i][0])==a and int(k[i][1])==b):
        if(c==0):
            print(k[i][2])
            exit()
        else:
            val=k[i][2]
if(c==0):
    print(-1)
    exit()
else:
    print(min(val,find(k,a,b,c)))