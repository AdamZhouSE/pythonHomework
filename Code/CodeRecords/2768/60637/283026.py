tests=(int)(input())
for i in range(tests):
    a,b,m=map(int,input().split(' '))
    sum=0
    for j in range(a,b+1):
        if(j%m==0):
            sum+=1
    print(sum)