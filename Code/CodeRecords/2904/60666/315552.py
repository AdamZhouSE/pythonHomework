N=int(input())
result=0
while(N):
    result=result*10+N%10
    N=N/10
print(result)