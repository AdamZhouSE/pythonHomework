n =int(input())
cards = list(map(int,input().split()))
min1 = 99999
for i in range(n):
    sum1=0
    for j in range(n):
        if abs(cards[i]-cards[j])%2==1:
            sum1=sum1+1
    if sum1<min1:
        min1=sum1
print(min1)