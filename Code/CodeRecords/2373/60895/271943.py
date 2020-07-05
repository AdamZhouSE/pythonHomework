t=int(input())
while t>0:
    t=t-1
    n=int(input())
    s=input().split(' ')
    max=0
    for i in range(0,n):
        sum=0
        sum=sum+int(s[i])
        for j in range(i+2,n,2):
            sum=sum+int(s[j])
        if sum>max:
            max=sum
    print(max)