num=int(input())
numbers=list(map(int,input().split(" ")))
sum=0
for i in range(0,num):
    sum=sum+abs(1-numbers[i])
print(sum)