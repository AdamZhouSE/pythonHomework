N1=int(input())#水桶数
t=int(input())
T=int(input())
n=int(T/t)+1
N2=n
i=1
while(N2<N1):
    N2=N2*n
    i=i+1
print(i)