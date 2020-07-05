N=int(input())
result=[]
while N>0:
    n=int(input())
    if n%2==0:
        result.append(1)
    else:
        result.append(0)
    N=N-1
 
for i in range(len(result)):
    print(result[i])