n=int(input())
coin=list(map(int,input().split()))
count=[]
for i in coin:
    count.append(coin.count(i))
print(max(count))