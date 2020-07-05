n=(int)(input())
money=list(map(int,input().split(' ')))
sum=0
standard=max(money)
for i in money:
    sum+=standard-i
print(sum)