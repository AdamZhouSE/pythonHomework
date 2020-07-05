N=int(input())
for i in range(N):
    num=int(input())
    if(num%3==0):
        print(str(num%3-1)+' '+str(num%3)+' '+str(num%3+1))
    else:
        print(-1)