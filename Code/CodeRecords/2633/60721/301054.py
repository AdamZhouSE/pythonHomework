m,n=map(int,input().split(" "))
lis=list(map(int,input().split(" ")))
for o in range(0,n):
    s=input()
    if(s[len(s)-1:]==' '):
        s=s[0:len(s)-1]
    s=list(map(int,s.split(" ")))
    if(s[0]==2):
        print(lis[s[1]-1])
    else:
        a=s[2]-s[1]+1
        num=[]
        for i in range(0,a):
            num.append(s[3])
            s[3]+=s[4]
        count=0
        for i in range(s[1]-1,s[2]):
            lis[i]+=num[count]
            count+=1
            