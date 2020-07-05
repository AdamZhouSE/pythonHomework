def getBin(a,max_len):
    b=""
    while(a>0):
        b+=str(a%2)
        a=int(a/2)
    while(len(b)<max_len):
        b+="0"
    return b
n=int(input())
for i in range(0,n):
    conti=True
    m=int(input())
    num=list(map(int,input().split()))
    if(0 in num):
        print("Yes")
        conti=False
    else:
        for i in num:
            if i <0:
                break
            if i==num[-1]:
                print("No")
                conti=False
    if(conti):
         max_len=pow(2,m)
         for i in range(1,max_len):
             total=0
             current_bin=getBin(i,max_len)
             for j in range(0,len(current_bin)):
                 if(current_bin[j]=='1'):
                     total+=num[j]
             if(total==0):
                 print("Yes")
                 break
         if(i==max_len-1):
                 print("No")