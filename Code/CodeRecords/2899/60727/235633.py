a=int(input())
flag =0
for i in range(1,100):
    for j in range(0,i):
        if(pow(4,j)==a):
            print('true')
            flag=1
            break
        if(pow(4,j)>a):
            print('false')
            flag=1
            break
    if(flag==1):break