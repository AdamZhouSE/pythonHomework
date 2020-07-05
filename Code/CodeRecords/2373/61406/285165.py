T = int(input())
for a in range(0,T):
    n = int(input())
    source = input().split(' ')
    sum1=sum2=0
    for i in range(0,n):
        if i%2==0:
            sum2+=int(source[i])
        elif i%2==1:
            sum1+=int(source[i])
    print(max(sum1,sum2))
    