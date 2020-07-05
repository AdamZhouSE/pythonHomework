t=int(input())
while t>0:
    t=t-1
    N=int(input())
    s=input().split(' ')
    num=0
    for i in range(1,N):
        for j in range(0,i):
            if int(s[j])>int(s[i]):
                num=num+1
    print(num)