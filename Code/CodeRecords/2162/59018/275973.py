result=1
x=float(input())
n=int(input())
if n==0:
    print(1)
elif n>0:
    for i in range(n):
        result=result*x
    print(result)    
        
        