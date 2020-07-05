num=int(input())
sum=0
k=input().split(' ')
k=list(map(int,k))
for i in range(num):
    sum=sum+k[i]
print('%.6f' %(sum/num))