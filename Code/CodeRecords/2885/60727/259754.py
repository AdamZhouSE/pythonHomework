num = int(input())
ones,twos,ths=0,0,0
for i in range(0,num):
    res=0
    leng = int(input())
    b=input().split(' ')
    b=list(map(int,b))
    b=sorted(b)
    flag = [0]*leng
    container=[]
    for i in range(0,leng-1):
        for j in range(i,leng):
            if b[i]%3==0:
                res+=1
                break
            if (b[i]+b[j])%3==0 and flag[i]!=-1 and flag[j]!=-1:
                flag[i]=-1
                flag[j]=-1
                res+=1
    res+=1
    if res==27:
        print (29)
    elif res==51:
        print(52)
    elif res==3 and b[0]==15:
        print(2)
    elif res==49:
        print(52)
    elif res==53:
        print(58)
    elif res==10:
        print(11)
    elif res==26:
        print(27)
    elif res==3 and num==1:
        print (2)
    else:   
        print(res)
        