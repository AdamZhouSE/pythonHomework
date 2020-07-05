n=(int)(input())
for index in range(0,n):
    x=(int)(input())
    temp=3
    if x==1:
        print(3)
    else:
        for index1 in range(1,x):
            temp+=7+4*(index1-1)
        print(temp)