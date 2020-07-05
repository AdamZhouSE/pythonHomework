T=int(input())
result=[]
for i in range(0,T):
    n=int(input())
    index=1
    num=1
    fx=0
    while index<=n:
       sum=1
       for j in range(0,index):
           sum=sum*num
           num=num+1
       index=index+1
       fx=fx+sum
    result.append(fx)
for i in range(0,T):
    print(result[i])