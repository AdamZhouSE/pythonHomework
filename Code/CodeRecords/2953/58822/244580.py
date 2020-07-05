def calcu(a,b):
    if (b==1):
        return a-1
    if(a==0 or b==0 or a==b):
        return 10000000
    return calcu(b,a%b)+int(a/b)

num=int(input())
times=num-1
for i in range(int(num/2),num):
    m=calcu(num,i)
    if(m<times):
        times=m
print(times,end='')