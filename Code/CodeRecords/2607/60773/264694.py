num=int(input())
for k in range(num):
    s=input()
    n=len(s)
    time=n//3
    sum=0
    for i in range(1,time+1,1):
        leng=i*3
        for j in range(n-leng+1):
            str=s[j:j+leng]
            n1=0
            n2=0
            n3=0
            for m in range(len(str)):
                if str[m]=='0':
                    n1=n1+1
                elif str[m]=='1':
                    n2=n2+1
                else:
                    n3=n3+1
            if n1==n2 and n2==n3:
                #print(str)
                sum=sum+1
    print(sum)