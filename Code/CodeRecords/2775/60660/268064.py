t=int(input())
for i in range(t):
    n=int(input())
    if n%3==0:
        result=str(n//3-1)+' '+str(n//3)+' '+str(n//3+1)
        print(result)
    else:
        print('-1')