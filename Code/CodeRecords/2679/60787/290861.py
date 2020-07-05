t=int(input())
for ex in range(0,t):
    n=int(input())
    if n==0:
        print(0)
    elif n==1:
        print(3)
    elif n==2:
        print(8)
    elif n==3:
        print(19)
    else:
        #全a
        re=1
        #1b
        for i in range(0,n):
            re+=1
            #1b1c/1c
            for j in range(0,n):
                re+=1
        #2c
        for i in range(0,n-1):
            for j in range(i+1,n):
                re+=1
                #1b2c
                for k in range(0,n-2):
                    re+=1
        print(re)