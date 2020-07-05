def restDay(infor,n):
    a=[]#记录休息，健身，比赛时的休息天数
    s=[]
    if(infor[0]==0):
        a=[1,10000,10000]
    elif(infor[0]==1):
        a=[1,10000,0]
    elif(infor[0]==2):
        a=[1,0,10000]
    else:
        a=[1,0,0]
    s.append(a)
    for i in range(1,n):
        if(infor[i]==0):
            a=[min(s[i-1])+1,10000,10000]
        elif(infor[i]==1):
            a=[min(s[i-1])+1,10000,min(s[i-1][0],s[i-1][1]),]
        elif(infor[i]==2):
            a=[min(s[i-1])+1,min(s[i-1][0],s[i-1][2]),10000]
        else:#infor[i]==3
            a=[min(s[i-1])+1,min(s[i-1][0],s[i-1][2]),min(s[i-1][0],s[i-1][1])]
        s.append(a)
    return min(s[n-1])
    
n=int(input())
infor=list(map(int,input().split(" ")))
print(restDay(infor,n)) 