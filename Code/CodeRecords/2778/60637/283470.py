tests=(int)(input())
for i in range(tests):
    l,r=map(int,input().split(' '))
    sum=0
    for i in range(l,r+1):
        if((str)(i)[0]==(str)(i)[-1]):
            sum+=1
    print(sum)
