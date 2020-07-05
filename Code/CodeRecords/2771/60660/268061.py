t=int(input())
for i in range(t):
    n=int(input())
    flag=0
    for i in range(int(n**0.5)-1,int(n**0.5)+1):
        if i**2==n:
            print('1')
            flag=1
            break
    if flag==0:
        print('0')