n=(int)(input())
orange_juices=list(map(int,input().split(' ')))
sum=0
for i in range(n):
    sum+=orange_juices[i]
print("%.6f" %(sum/n))